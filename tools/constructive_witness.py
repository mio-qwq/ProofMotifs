"""Extract ternary order-loss witnesses using exact square-defect queries.

The extractor uses O(m^2) queries to an additive-map oracle on F_(3^m).
This is an oracle-query bound, NOT a total runtime bound for this executable:
the existing Field class precomputes O(q^2) arithmetic tables, and the separate
verification routine computes complete q-entry moment vectors.  No randomness,
floating point arithmetic, or candidate order-classification formula is used
to verify an extracted witness.
"""
from itertools import product
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cancellation import Field, order
from order_preservers import additive_map
from ternary_differences import subset_weight


def _rank(f: Field, columns: tuple[int, ...]) -> int:
    """Prime-field Gaussian elimination, without enumerating the whole map."""
    rows = [[(x // f.p**i) % f.p for x in columns]
            for i in range(f.degree)]
    pivot_row = 0
    for j in range(len(columns)):
        pivot = next((i for i in range(pivot_row, f.degree) if rows[i][j]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][j], -1, f.p)
        rows[pivot_row] = [(x * inverse) % f.p for x in rows[pivot_row]]
        for i in range(f.degree):
            if i != pivot_row:
                factor = rows[i][j]
                rows[i] = [(x - factor*y) % f.p
                           for x, y in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == f.degree:
            break
    return pivot_row


def _validate(f: Field, columns: tuple[int, ...]) -> None:
    if f.p != 3:
        raise ValueError('the square-defect witness theorem requires characteristic three')
    if (len(columns) != f.degree or
            any(not isinstance(x, int) or not 0 <= x < f.q for x in columns)):
        raise ValueError('one valid image per standard prime-field basis vector is required')
    if _rank(f, columns) != f.degree:
        raise ValueError('the map must be an additive bijection')


class _ColumnOracle:
    """Evaluate T from its columns, caching and counting distinct oracle inputs."""
    def __init__(self, f: Field, columns: tuple[int, ...]):
        self.f, self.columns = f, columns
        self.cache: dict[int, int] = {}

    def __call__(self, x: int) -> int:
        if x not in self.cache:
            value = 0
            for j, image in enumerate(self.columns):
                digit = (x // self.f.p**j) % self.f.p
                value = self.f.add[value][self.f.mul[digit][image]]
            self.cache[x] = value
        return self.cache[x]


def conic_directions(f: Field, t: int) -> tuple[int, int, int]:
    """A(t)=(1-t^2+t, 1-t^2-t, -1-t^2), with sum of squares zero."""
    if f.p != 3 or not isinstance(t, int) or not 0 <= t < f.q:
        raise ValueError('require characteristic three and a valid field element')
    tt = f.mul[t][t]
    base = f.add[1][f.neg[tt]]
    return f.add[base][t], f.add[base][f.neg[t]], f.neg[f.add[1][tt]]


def _semilinear_exponent(f: Field, columns: tuple[int, ...]) -> int | None:
    scale = columns[0]
    return next((j for j in range(f.degree)
                 if all(columns[i] == f.mul[scale][f.pow(f.p**i, f.p**j)]
                        for i in range(f.degree))), None)


def construct_witness(f: Field, columns: tuple[int, ...]) -> dict:
    """Return a direct order-7 -> order-5 witness or an exact preserver label.

    Hypotheses: the supplied columns define an F3-linear bijection of F_(3^m).
    Query Q(t)=T(1)T(t^2)-T(t)^2 on the standard basis excluding 1, then
    its pair sums.  Polarization and B(1,x)=0 make these queries sufficient.
    If a detected parameter is degenerate, three further queries outside F9
    suffice.  F9 is explicitly classified as a preserver exception instead.

    Returned map_oracle_calls_extraction counts cached, distinct evaluations
    only during the defect search; evaluating the three final images is
    separately counted in map_oracle_calls_including_images.  Rank validation,
    arithmetic-table construction and independent verification are not oracle
    calls, and their runtime is not claimed to be quadratic.
    """
    columns = tuple(columns)
    _validate(f, columns)
    oracle = _ColumnOracle(f, columns)
    scale = oracle(1)
    query_log: list[dict] = []
    defects: dict[int, int] = {}

    def defect(t: int, phase: str) -> int:
        if t not in defects:
            value = f.add[f.mul[scale][oracle(f.mul[t][t])]][
                f.neg[f.mul[oracle(t)][oracle(t)]]]
            defects[t] = value
            query_log.append(dict(parameter=t, defect=value, phase=phase))
        return defects[t]

    basis = [f.p**i for i in range(1, f.degree)]
    candidates = basis + [f.add[a][b] for i, a in enumerate(basis)
                          for b in basis[i+1:]]
    parameter = next((t for t in candidates if defect(t, 'basis')), None)
    initial_parameter = parameter
    repair_used = False
    exponent = _semilinear_exponent(f, columns)
    result = dict(q=f.q, modulus=list(f.modulus), columns=list(columns),
                  basis_defect_query_bound=f.degree*(f.degree-1)//2,
                  defect_query_bound=f.degree*(f.degree-1)//2 +
                  (3 if f.degree >= 4 and f.degree % 2 == 0 else 0),
                  initial_parameter=initial_parameter, repair_used=False,
                  semilinear_exponent=exponent)

    if f.q == 9:
        result['status'] = 'semilinear' if exponent is not None else 'exceptional_preserver'
        # Every additive bijection of F9 preserves the ternary order.  Q can
        # nevertheless be nonzero, and all its detected parameters are bad.
    elif parameter is None:
        if exponent is None:
            raise AssertionError('zero basis defects contradict square-preserver classification')
        result['status'] = 'semilinear'
    else:
        if exponent is not None:
            raise AssertionError('a semilinear map cannot have a nonzero square defect')
        if not all(conic_directions(f, parameter)):
            if f.degree < 4 or f.degree % 2:
                raise AssertionError('a degenerate nonprime parameter requires an even extension')
            # Such a parameter lies in F9\F3.  A standard basis vector u
            # outside F9 exists because m>2, and u,t+u,t-u are all good.
            u = next(x for x in basis if f.pow(x, 9) != x)
            repair_candidates = (u, f.add[parameter][u], f.add[parameter][f.neg[u]])
            parameter = next((x for x in repair_candidates if defect(x, 'repair')), None)
            if parameter is None:
                raise AssertionError('quadratic parallelogram identity failed to repair parameter')
            repair_used = True
        directions = conic_directions(f, parameter)
        if not all(directions):
            raise AssertionError('extracted parameter has a zero conic coordinate')
        extraction_calls = len(oracle.cache)
        images = tuple(oracle(x) for x in directions)
        result.update(status='witness', parameter=parameter,
                      directions=list(directions), images=list(images),
                      repair_used=repair_used,
                      map_oracle_calls_extraction=extraction_calls)

    result['defect_query_count'] = len(defects)
    result['query_log'] = query_log
    result.setdefault('map_oracle_calls_extraction', len(oracle.cache))
    result['map_oracle_calls_including_images'] = len(oracle.cache)
    result['uncached_oracle_call_bound_extraction'] = 1 + 2*len(defects)
    assert len(defects) <= result['defect_query_bound']
    assert result['map_oracle_calls_extraction'] <= 1 + 2*len(defects)
    return result


def verify_witness(f: Field, columns: tuple[int, ...], result: dict) -> dict:
    """Verify by inclusion-exclusion and all q moments, independent of e1/e2.

    This deliberately builds the entire map table as a second evaluation path;
    its O(q) map values and full moment computation are outside extraction's
    oracle-query accounting. The complete q-moment range suffices to certify
    infinity; the smaller support-size moment range would also suffice.
    """
    _validate(f, tuple(columns))
    if result['status'] != 'witness':
        raise ValueError('verification requires an extracted witness')
    values = additive_map(f, tuple(columns))
    directions = tuple(result['directions'])
    images = tuple(values[x] for x in directions)
    if images != tuple(result['images']):
        raise AssertionError('column-oracle and full-table images disagree')
    before_mu, after_mu = subset_weight(f, directions), subset_weight(f, images)
    before_moments, after_moments = f.moments(before_mu), f.moments(after_mu)
    orders = order(before_moments), order(after_moments)
    if orders != (7, 5):
        raise AssertionError(f'expected order 7 -> 5, observed {orders}')
    return dict(before_order=orders[0], after_order=orders[1],
                before_moments=list(before_moments), after_moments=list(after_moments),
                before_support=[[x,w] for x,w in enumerate(before_mu) if w],
                after_support=[[x,w] for x,w in enumerate(after_mu) if w],
                complete_moments_per_side=f.q,
                independent_map_values=f.q)


def scan_normalized(f: Field) -> dict:
    """Exhaust all normalized additive bijections; intended for q<=27 only."""
    if f.q > 27:
        raise ValueError('exhaustive scan intentionally restricted to q <= 27')
    counts = {'semilinear': 0, 'exceptional_preserver': 0, 'witness': 0}
    max_queries = max_oracle_calls = repaired = 0
    first_witness = None
    for tail in product(range(f.q), repeat=f.degree-1):
        columns = (1, *tail)
        if _rank(f, columns) != f.degree:
            continue
        result = construct_witness(f, columns)
        counts[result['status']] += 1
        max_queries = max(max_queries, result['defect_query_count'])
        max_oracle_calls = max(max_oracle_calls, result['map_oracle_calls_extraction'])
        repaired += result['repair_used']
        if result['status'] == 'witness':
            verification = verify_witness(f, columns, result)
            if first_witness is None:
                first_witness = dict(extraction=result, verification=verification)
    return dict(q=f.q, modulus=list(f.modulus),
                normalized_bijections=sum(counts.values()), statuses=counts,
                maximum_defect_queries=max_queries,
                maximum_map_oracle_calls_extraction=max_oracle_calls,
                repairs=repaired, first_witness=first_witness)


def selected_transvections(f: Field) -> list[dict]:
    """Deterministically test elementary shears fixing 1, not all GL_m maps."""
    records = []
    for changed in range(1, f.degree):
        for added in range(f.degree):
            if changed == added:
                continue
            for coefficient in (1, 2):
                columns = [f.p**i for i in range(f.degree)]
                columns[changed] = f.add[columns[changed]][
                    f.mul[coefficient][columns[added]]]
                result = construct_witness(f, tuple(columns))
                verification = (verify_witness(f, tuple(columns), result)
                                if result['status'] == 'witness' else None)
                records.append(dict(columns=columns, status=result['status'],
                                    defect_queries=result['defect_query_count'],
                                    repair_used=result['repair_used'],
                                    directions=result.get('directions'),
                                    verified_orders=([verification['before_order'],
                                                      verification['after_order']]
                                                     if verification else None),
                                    complete_moments_per_side=f.q if verification else None))
    return records


def main() -> None:
    fields = [Field(3, (0,1)), Field(3, (1,0,1)), Field(3, (1,2,0,1))]
    f81 = Field(3, (2,0,1,0,1))
    columns81 = (1,4,16,27)
    repaired = construct_witness(f81, columns81)
    assert repaired['repair_used']
    controls = []
    for f in (*fields, f81):
        for scale in (1, 2):
            for j in range(f.degree):
                columns = tuple(f.mul[scale][f.pow(f.p**i, f.p**j)]
                                for i in range(f.degree))
                result = construct_witness(f, columns)
                assert result['status'] == 'semilinear'
                controls.append(dict(q=f.q, scale=scale, exponent=j,
                                     defect_queries=result['defect_query_count']))
    print(json.dumps(dict(schema=1, randomized=False,
                          arithmetic='exact finite-field tables',
                          complexity_scope='O(m^2) defect/oracle queries; no total-runtime claim',
                          normalized_scans=[scan_normalized(f) for f in fields],
                          semilinear_controls=controls,
                          selected_field81_transvections=selected_transvections(f81),
                          even_extension_repair=dict(extraction=repaired,
                              verification=verify_witness(f81, columns81, repaired))),
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
