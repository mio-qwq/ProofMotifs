"""Power-generator ternary witnesses with at most 2m-3 defect evaluations.

The bound concerns Q(t)=T(1)T(t^2)-T(t)^2 evaluations, not an optimal count
of T-oracle calls or the executable's total runtime.  In particular m basis
images already determine an additive map.  Field table construction, input
validation, evaluation from columns and complete-moment verification have
their own costs.  Only the finite fields supported by Field are implemented.
"""
from itertools import product
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cancellation import Field
from order_preservers import additive_map
from constructive_witness import (
    _ColumnOracle, _validate, _rank, _semilinear_exponent,
    conic_directions, verify_witness)


def generator_test_pairs(f: Field) -> list[dict]:
    """Choose admissible pairs using the validated polynomial power basis.

    For m>=3 the generator alpha has degree m, hence is outside F9.  For
    u=alpha^k, use two points which are outside F9.  If Q(alpha)=0 and their
    defects both vanish, polarization forces H(alpha,u)=0.  This is an
    adaptive choice from field membership, not from unqueried defect values.
    """
    if f.p != 3 or f.degree < 3:
        raise ValueError('generator pair construction requires characteristic three and m>=3')
    alpha = f.p
    pairs = []
    for k in range(2, f.degree):
        u = f.p**k
        plus, minus = f.add[alpha][u], f.add[alpha][f.neg[u]]
        if f.pow(u,9) == u:
            branch, parameters = 'u_in_F9', (plus,minus)
        elif f.pow(plus,9) == plus:
            branch, parameters = 'alpha_plus_u_in_F9', (u,minus)
        else:
            branch, parameters = 'ordinary', (u,plus)
        if any(f.pow(t,9) == t for t in parameters):
            raise AssertionError('adaptive generator pair contains a parameter in F9')
        pairs.append(dict(power=k, u=u, branch=branch, parameters=list(parameters)))
    return pairs


def construct_generator_witness(f: Field, columns: tuple[int, ...]) -> dict:
    """Extract a directly checked 7->5 certificate, or label the preserver.

    The input is an additive bijection specified on the standard polynomial
    power basis (1,alpha,...,alpha^(m-1)).  For m>=3 at most 2m-3 Q-values
    are evaluated: Q(alpha), then at most two admissible values for each
    remaining power.  No bad-parameter repair is needed.  F3 and F9 receive
    separate exact classifications; F9 admits exceptional preservers.
    """
    columns = tuple(columns)
    _validate(f, columns)
    oracle = _ColumnOracle(f, columns)
    scale = oracle(1)
    defects: dict[int,int] = {}
    query_log: list[dict] = []
    visited_pairs: list[dict] = []
    exponent = _semilinear_exponent(f, columns)

    def defect(t: int, phase: str, power: int) -> int:
        if t not in defects:
            value = f.add[f.mul[scale][oracle(f.mul[t][t])]][
                f.neg[f.mul[oracle(t)][oracle(t)]]]
            defects[t] = value
            query_log.append(dict(parameter=t,defect=value,phase=phase,power=power))
        return defects[t]

    result = dict(q=f.q,modulus=list(f.modulus),columns=list(columns),
                  generator=f.p if f.degree>1 else None,
                  defect_query_bound=max(0,2*f.degree-3),
                  semilinear_exponent=exponent,
                  admissibility_guaranteed=f.degree>=3)
    parameter = None
    if f.degree == 1:
        result['status'] = 'semilinear'
    elif f.degree == 2:
        defect(f.p,'exceptional_field',1)
        result['status'] = 'semilinear' if exponent is not None else 'exceptional_preserver'
    else:
        alpha = f.p
        if f.pow(alpha,9) == alpha:
            raise AssertionError('a degree-m power generator cannot lie in F9 for m>=3')
        if defect(alpha,'generator',1):
            parameter = alpha
        else:
            for pair in generator_test_pairs(f):
                record = dict(pair,queried=[])
                visited_pairs.append(record)
                for i,t in enumerate(pair['parameters']):
                    record['queried'].append(t)
                    if defect(t,'pair_first' if i==0 else 'pair_second',pair['power']):
                        parameter = t
                        break
                if parameter is not None:
                    break
        if parameter is None:
            if exponent is None:
                raise AssertionError('vanishing generator defects contradict field-automorphism theorem')
            result['status'] = 'semilinear'
        else:
            if exponent is not None:
                raise AssertionError('a scalar Frobenius map has nonzero square defect')
            directions = conic_directions(f,parameter)
            if not all(directions):
                raise AssertionError('admissible generator parameter has a zero conic coordinate')
            extraction_calls = len(oracle.cache)
            images = tuple(oracle(x) for x in directions)
            result.update(status='witness',parameter=parameter,
                          directions=list(directions),images=list(images),
                          map_oracle_calls_extraction=extraction_calls)
    result.update(query_log=query_log,visited_pairs=visited_pairs,
                  defect_query_count=len(defects),
                  map_oracle_calls_including_images=len(oracle.cache),
                  uncached_oracle_call_bound_extraction=1+2*len(defects))
    result.setdefault('map_oracle_calls_extraction',len(oracle.cache))
    assert result['defect_query_count'] <= result['defect_query_bound']
    assert result['map_oracle_calls_extraction'] <= 1+2*len(defects)
    return result


def scan_normalized_generators(f: Field) -> dict:
    """Exhaust normalized maps only in fields of at most 27 elements."""
    if f.q>27:
        raise ValueError('full normalized-map scan intentionally restricted to q<=27')
    counts = {'semilinear':0,'exceptional_preserver':0,'witness':0}
    histogram: dict[int,int] = {}
    max_calls = 0
    first_witness = None
    for tail in product(range(f.q),repeat=f.degree-1):
        columns = (1,*tail)
        if _rank(f,columns)!=f.degree:
            continue
        result = construct_generator_witness(f,columns)
        counts[result['status']] += 1
        n = result['defect_query_count']
        histogram[n] = histogram.get(n,0)+1
        max_calls = max(max_calls,result['map_oracle_calls_extraction'])
        if result['status']=='witness':
            verified = verify_witness(f,columns,result)
            if first_witness is None:
                first_witness = dict(extraction=result,verification=verified)
    return dict(q=f.q,modulus=list(f.modulus),normalized_bijections=sum(counts.values()),
                statuses=counts,defect_query_histogram=histogram,
                maximum_defect_queries=max(histogram),
                maximum_map_oracle_calls_extraction=max_calls,
                first_witness=first_witness)


def selected_generator_maps(f: Field) -> list[dict]:
    """Exact checks of specified elementary shears, not exhaustive GL_m data."""
    records = []
    for changed in range(1,f.degree):
        for added in range(f.degree):
            if changed==added:
                continue
            for coefficient in (1,2):
                columns = [f.p**i for i in range(f.degree)]
                columns[changed] = f.add[columns[changed]][f.mul[coefficient][columns[added]]]
                result = construct_generator_witness(f,tuple(columns))
                if result['status']!='witness':
                    raise AssertionError('a nontrivial elementary shear should not be scalar Frobenius')
                verified = verify_witness(f,tuple(columns),result)
                records.append(dict(extraction=result,
                                    verified_orders=[verified['before_order'],verified['after_order']],
                                    complete_moments_per_side=f.q))
    return records


def annihilator_transvection(f: Field, parameters: tuple[int,...]) -> dict | None:
    """Build a non-Frobenius map invisible on the supplied Q-only queries.

    If U=span_F3(1,t_i,t_i^2) is proper, choose a nonzero prime-valued linear
    functional phi annihilating U and return S(x)=x+phi(x).  Since phi(1)=0,
    its nilpotent perturbation squares to zero, so S is unital and bijective.
    Its fixed space has dimension m-1, proving it is not Frobenius for m>=3.
    Every supplied defect is zero.  This is a small-field verification of a
    Q-oracle lower-bound adversary, NOT a lower bound for T-oracle queries.

    The implementation enumerates small prime-field functionals.  No claim
    of polynomial runtime for this helper or the surrounding Field is made.
    Return None if U is the entire field, where this construction is silent.
    """
    if f.p!=3 or f.degree<3:
        raise ValueError('the transvection adversary requires characteristic three and m>=3')
    parameters = tuple(parameters)
    if any(not isinstance(t,int) or not 0<=t<f.q for t in parameters):
        raise ValueError('all queried parameters must be valid field elements')
    span_columns = (1,*(x for t in parameters for x in (t,f.mul[t][t])))
    dimension = _rank(f,span_columns)
    if dimension==f.degree:
        return None

    def functional(coefficients: tuple[int,...], x: int) -> int:
        return sum(c*((x//f.p**j)%f.p) for j,c in enumerate(coefficients)) % f.p

    coefficients = next((c for tail in product(range(f.p),repeat=f.degree-1)
                         if any(tail)
                         for c in ((0,*tail),)
                         if all(functional(c,x)==0 for x in span_columns)),None)
    if coefficients is None:
        raise AssertionError('a proper subspace has no enumerated nonzero annihilator')
    columns = tuple(f.add[f.p**j][c] for j,c in enumerate(coefficients))
    _validate(f,columns)
    if _semilinear_exponent(f,columns) is not None:
        raise AssertionError('a nonzero rank-one unital transvection is Frobenius')
    oracle = _ColumnOracle(f,columns)
    queried_defects = [f.add[oracle(f.mul[t][t])][f.neg[f.mul[oracle(t)][oracle(t)]]]
                       for t in parameters]
    if any(queried_defects):
        raise AssertionError('annihilator transvection exposed by its input Q transcript')
    return dict(columns=list(columns),functional_coefficients=list(coefficients),
                parameters=list(parameters),queried_defects=queried_defects,
                transcript_span_dimension=dimension,
                fixed_space_dimension=f.degree-1,
                scope='Q-oracle decision adversary; no T-oracle lower-bound claim')


def scan_one_query_adversaries(f: Field) -> dict:
    """Verify every single-query zero transcript in a selected small field."""
    if f.degree<4:
        raise ValueError('every one-query span is guaranteed proper only for m>=4')
    dimensions: dict[int,int] = {}
    distinct_maps: set[tuple[int,...]] = set()
    maximum_queries = count = 0
    first_example = None
    for t in range(f.q):
        adversary = annihilator_transvection(f,(t,))
        if adversary is None:
            raise AssertionError('a one-query span has dimension above three')
        result = construct_generator_witness(f,tuple(adversary['columns']))
        distinct_maps.add(tuple(adversary['columns']))
        if result['status']!='witness':
            raise AssertionError('non-Frobenius adversary did not yield a witness')
        verified = verify_witness(f,tuple(adversary['columns']),result)
        n = adversary['transcript_span_dimension']
        dimensions[n] = dimensions.get(n,0)+1
        maximum_queries = max(maximum_queries,result['defect_query_count'])
        count += 1
        if first_example is None:
            first_example = dict(adversary=adversary,extraction=result,verification=verified)
    return dict(q=f.q,modulus=list(f.modulus),single_query_transcripts=count,
                verified_nonsemilinear_adversaries=count,
                distinct_map_count=len(distinct_maps),
                transcript_span_dimension_histogram=dimensions,
                maximum_extractor_defect_queries=maximum_queries,
                first_example=first_example,
                scope='Q-oracle decision only; not a T-oracle lower bound')


def nongenerator_counterexample(f: Field) -> dict:
    """One multiplication intertwiner at a nongenerator need not suffice.

    In this particular F81 representation, i=alpha^2-1 lies in F9 and the
    map with columns (1,4,9,36) commutes with multiplication by i, although
    it has a nonzero square defect at the full-degree generator alpha.
    """
    if f.p!=3 or f.modulus!=(2,0,1,0,1):
        raise ValueError('this explicit counterexample uses modulus x^4+x^2+2 over F3')
    columns = (1,4,9,36)
    _validate(f,columns)
    values = additive_map(f,columns)
    i,alpha = 11,3
    intertwiner_defects = [f.add[values[f.mul[i][x]]][f.neg[f.mul[values[i]][values[x]]]]
                          for x in range(f.q)]
    square_defect = f.add[values[f.mul[alpha][alpha]]][f.neg[f.mul[values[alpha]][values[alpha]]]]
    if (values[1]!=1 or len(set(values))!=81 or f.pow(i,9)!=i or
            any(intertwiner_defects) or square_defect!=5):
        raise AssertionError('the specified nongenerator counterexample failed')
    result = construct_generator_witness(f,columns)
    verified = verify_witness(f,columns,result)
    return dict(q=f.q,modulus=list(f.modulus),columns=list(columns),
                nongenerator=i,nongenerator_subfield_size=len(f.span((1,i))),
                multiplication_intertwiner_defects=intertwiner_defects,
                generator=alpha,generator_square_defect=square_defect,
                extraction=result,verification=verified)


def main() -> None:
    fields = [Field(3,(0,1)),Field(3,(1,0,1)),Field(3,(1,2,0,1))]
    f81u = Field(3,(2,0,1,0,1))
    f81plus = Field(3,(2,1,2,2,1))
    f243 = Field(3,(1,2,0,0,0,1))
    controls = []
    for f in (*fields,f81u,f81plus,f243):
        for scale in (1,2):
            for exponent in range(f.degree):
                columns = tuple(f.mul[scale][f.pow(f.p**i,f.p**exponent)]
                                for i in range(f.degree))
                result = construct_generator_witness(f,columns)
                assert result['status']=='semilinear'
                controls.append(result)
    endpoint_columns = (1,9,15)
    endpoint = construct_generator_witness(fields[2],endpoint_columns)
    assert endpoint['query_log'][0]['defect']==0 and endpoint['status']=='witness'
    print(json.dumps(dict(schema=1,randomized=False,arithmetic='exact finite-field tables',
                          complexity_scope='at most 2m-3 defect evaluations for m>=3; no total-runtime or optimal T-call claim',
                          normalized_scans=[scan_normalized_generators(f) for f in fields],
                          semilinear_controls=controls,
                          selected_maps=[dict(q=f.q,modulus=list(f.modulus),
                                              records=selected_generator_maps(f))
                                         for f in (f81u,f81plus,f243)],
                          field81_one_query_adversaries=scan_one_query_adversaries(f81u),
                          nongenerator_negative=nongenerator_counterexample(f81u),
                          endpoint_negative=dict(extraction=endpoint,
                              verification=verify_witness(fields[2],endpoint_columns,endpoint))),
                     indent=2,sort_keys=True))


if __name__=='__main__':
    main()
