"""Exact tests of characteristic-three first-difference classification.

The general proof is in SC-003. This script provides finite checks and an exact
polynomial coefficient check. It is not a Lean kernel or independent reviewer.
"""
from itertools import product
from math import factorial
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cancellation import Field, order


def subset_weight(f: Field, directions: tuple[int, int, int]) -> tuple[int, ...]:
    """Inclusion-exclusion, not a convolution call."""
    out = [0] * f.q
    for mask in range(8):
        x = 0
        for j, a in enumerate(directions):
            if mask & (1 << j):
                x = f.add[x][a]
        sign = f.neg[1] if (3 - mask.bit_count()) % 2 else 1
        out[x] = f.add[out[x]][sign]
    return tuple(out)


def invariants(f: Field, a: int, b: int, c: int) -> tuple[int, int, int]:
    if f.p != 3:
        raise ValueError('the classification is specific to characteristic three')
    if any(not 0 <= x < f.q for x in (a,b,c)):
        raise ValueError('invalid direction')
    aa, bb, cc = (f.mul[x][x] for x in (a,b,c))
    e1 = f.add[f.add[aa][bb]][cc]
    e2 = f.add[f.add[f.mul[aa][bb]][f.mul[aa][cc]]][f.mul[bb][cc]]
    abc = f.mul[f.mul[a][b]][c]
    return abc, e1, e2


def predicted_order(abc: int, e1: int, e2: int) -> int | None:
    return None if not abc else (5 if e1 else (7 if e2 else None))


def symbolic_moments() -> dict[int, dict[tuple[int, int, int], int]]:
    """Surviving inclusion-exclusion coefficients, calculated over integers mod 3."""
    answer = {}
    for n in range(8):
        terms = {}
        for i in range(1,n):
            for j in range(1,n-i):
                k = n-i-j
                coefficient = factorial(n)//(factorial(i)*factorial(j)*factorial(k)) % 3
                if coefficient:
                    terms[i,j,k] = coefficient
        answer[n] = terms
    assert all(not answer[n] for n in (0,1,2,3,4,6))
    assert answer[5] == {(3,1,1):2,(1,3,1):2,(1,1,3):2}
    assert answer[7] == {(3,3,1):2,(3,1,3):2,(1,3,3):2}
    return answer


def scan(f: Field) -> dict:
    differences = [f.difference(a) for a in range(f.q)]
    pairs = {(a,b): f.convolution(differences[a], differences[b])
             for a,b in product(range(f.q),repeat=2)}
    counts = {'5':0,'7':0,'infinity':0}
    normalized_independent = {'5':0,'7':0}
    zero_directions = one_line = 0
    for a,b,c in product(range(f.q),repeat=3):
        mu = subset_weight(f,(a,b,c))
        assert mu == f.convolution(pairs[a,b],differences[c])
        m = f.moments(mu)
        t = order(m)
        abc,e1,e2 = invariants(f,a,b,c)
        assert t == predicted_order(abc,e1,e2)
        # Compute through degree 7 even when q<8; do not index an incomplete vector.
        low = []
        for n in range(8):
            v=0
            for x,w in enumerate(mu):
                v=f.add[v][f.mul[w][f.pow(x,n)]]
            low.append(v)
        assert all(low[n] == 0 for n in (0,1,2,3,4,6))
        assert low[5] == f.neg[f.mul[abc][e1]]
        assert low[7] == f.neg[f.mul[abc][e2]]
        counts['infinity' if t is None else str(t)] += 1
        if not abc:
            zero_directions += 1
        elif not e1 and not e2:
            assert all(x in (a,f.neg[a]) for x in (b,c))
            assert not any(mu)
            one_line += 1
        if a == 1 and len(f.span((a,b,c))) == 27:
            normalized_independent[str(t)] += 1
    return dict(q=f.q,modulus=list(f.modulus),ordered_triples=f.q**3,
                orders=counts,zero_direction_cases=zero_directions,
                nonzero_single_line_cases=one_line,
                normalized_rank_three=normalized_independent)


def main() -> None:
    symbolic_moments()
    fields=[Field(3,(0,1)),Field(3,(1,0,1)),Field(3,(1,2,0,1))]
    report={'schema':1,'randomized':False,'arithmetic':'exact characteristic three',
            'symbolic_degrees_checked':list(range(8)),
            'fields':[scan(f) for f in fields]}
    f=fields[-1]
    report['F27_witnesses']=[]
    for directions in ((1,3,9),(1,3,15)):
        mu=subset_weight(f,directions)
        report['F27_witnesses'].append(dict(directions=list(directions),
            span_size=len(f.span(directions)),invariants=list(invariants(f,*directions)),
            support=[[x,w] for x,w in enumerate(mu) if w],
            moments_0_through_8=list(f.moments(mu)[:9]),order=order(f.moments(mu))))
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
