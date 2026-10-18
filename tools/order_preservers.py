"""Exact finite checks for additive preservers of ternary cancellation order.

Enumerate normalized additive bijections T(1)=1 in F_3, F_9, F_27. Truth
labels come from actual subset weights and complete moment vectors, not the
candidate classification of the preserver group. No randomness is used.
"""
from itertools import product
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cancellation import Field, order
from ternary_differences import subset_weight


def additive_map(f: Field, columns: tuple[int, ...]) -> tuple[int, ...]:
    if len(columns) != f.degree or any(not 0 <= x < f.q for x in columns):
        raise ValueError('one valid image per prime-field basis vector is required')
    values = []
    for x in range(f.q):
        y = 0
        for j, image in enumerate(columns):
            digit = (x // f.p**j) % f.p
            y = f.add[y][f.mul[digit][image]]
        values.append(y)
    return tuple(values)


def scan_preservers(f: Field) -> dict:
    if f.p != 3:
        raise ValueError('this experiment concerns characteristic three')
    triples = list(product(range(f.q), repeat=3))
    # Nonzero exceptional cases first, only to accelerate rejection of maps.
    labels = {v: order(f.moments(subset_weight(f, v))) for v in triples}
    triples.sort(key=lambda v: (labels[v] != 7, labels[v] is None, v))
    preservers = []
    candidates = labels_compared = 0
    rejection = None
    for tail in product(range(f.q), repeat=f.degree-1):
        columns = (1, *tail)
        if len(f.span(columns)) != f.q:
            continue
        candidates += 1
        t = additive_map(f, columns)
        assert len(set(t)) == f.q and t[1] == 1
        for a, b, c in triples:
            labels_compared += 1
            before = labels[a, b, c]
            after = labels[t[a], t[b], t[c]]
            if before != after:
                if rejection is None:
                    rejection = dict(columns=list(columns), directions=[a,b,c],
                                     images=[t[a],t[b],t[c]], before=before, after=after)
                break
        else:
            preservers.append(columns)
    frobenius_columns = sorted({tuple(f.pow(f.p**j, f.p**k) for j in range(f.degree))
                                for k in range(f.degree)})
    if f.q == 9:
        assert len(preservers) == candidates == 6
    else:
        assert sorted(preservers) == frobenius_columns
    return dict(q=f.q, modulus=list(f.modulus), all_triples_labeled=len(labels),
                normalization='T(1)=1; unnormalized count follows by nonzero scalar multiplication',
                normalized_bijections=candidates, normalized_preservers=len(preservers),
                preserver_columns=[list(c) for c in preservers],
                normalized_frobenius_columns=[list(c) for c in frobenius_columns],
                full_preserver_count=(f.q-1)*len(preservers),
                labels_compared=labels_compared, first_rejection=rejection)


def parameter_identity_check(f: Field) -> dict:
    """Check the conic parameterization and transformed identity for every
    additive map in F_9 (including non-bijections), and normalized maps in F_27.
    This validates an identity, not the universal mathematical proof.
    """
    if f.p != 3:
        raise ValueError('characteristic three required')
    total = good = 0
    columns_iter = (product(range(f.q), repeat=f.degree) if f.q <= 9 else
                    ((1,*tail) for tail in product(range(f.q), repeat=f.degree-1)))
    for columns in columns_iter:
        t = additive_map(f, tuple(columns))
        for x in range(f.q):
            xx = f.mul[x][x]
            a = f.add[f.add[1][f.neg[xx]]][x]
            b = f.add[f.add[1][f.neg[xx]]][f.neg[x]]
            c = f.neg[f.add[1][xx]]
            assert f.add[f.add[f.mul[a][a]][f.mul[b][b]]][f.mul[c][c]] == 0
            actual = f.add[f.add[f.mul[t[a]][t[a]]][f.mul[t[b]][t[b]]]][f.mul[t[c]][t[c]]]
            expected = f.add[f.mul[t[1]][t[xx]]][f.neg[f.mul[t[x]][t[x]]]]
            assert actual == expected
            total += 1
            good += bool(a and b and c)
    return dict(q=f.q, identity_instances=total, nonzero_coordinate_instances=good)


def main() -> None:
    fields=[Field(3,(0,1)), Field(3,(1,0,1)), Field(3,(1,2,0,1))]
    print(json.dumps(dict(schema=1, arithmetic='exact finite fields', randomized=False,
                         preserver_scans=[scan_preservers(f) for f in fields],
                         parameter_identity=[parameter_identity_check(f) for f in fields]),
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
