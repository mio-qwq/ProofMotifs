#!/usr/bin/env python3
"""Exact free-algebra identity over Z[q,c], not a formal-proof kernel.

Words use A,B,Z with rightmost operator acting first. A certificate of P*S=0
only implies P=0 when S is right-cancellable (here an actual unit). This
arithmetic checker does not infer invertibility from a finite jet.
"""
import json


def clean(p):
    return {k: v for k, v in p.items() if v}


def add(*ps):
    result = {}
    for p in ps:
        for k, v in p.items():
            result[k] = result.get(k, 0)+v
    return clean(result)


def neg(p):
    return {k: -v for k, v in p.items()}


def mul(*ps):
    result = {(0, 0, ''): 1}
    for p in ps:
        new = {}
        for (i, j, w), a in result.items():
            for (k, ell, v), b in p.items():
                key = i+k, j+ell, w+v
                new[key] = new.get(key, 0)+a*b
        result = clean(new)
    return result


def scalar(n):
    if type(n) is not int:
        raise ValueError('Exact integer coefficient required')
    return clean({(0, 0, ''): n})


def variable(word):
    if any(c not in 'ABZ' for c in word):
        raise ValueError('Unknown word letter')
    return {(0, 0, word): 1}


def specialization(p, q=None, c=None, characteristic=0):
    if type(characteristic) is not int or characteristic < 0 or characteristic == 1:
        raise ValueError('Nonnegative coefficient modulus, not1')
    for x in [q, c]:
        if x is not None and type(x) is not int:
            raise ValueError('Integer specialization only')
    result = {}
    for (i, j, w), a in p.items():
        key = (i if q is None else 0, j if c is None else 0, w)
        value = a*(q**i if q is not None else 1)*(c**j if c is not None else 1)
        result[key] = result.get(key, 0)+value
    if characteristic:
        result = {k: v % characteristic for k, v in result.items()}
    return clean(result)


def encode(p):
    return [{'q_degree': i, 'c_degree': j, 'word': w, 'integer': a}
            for (i, j, w), a in sorted(p.items())]


def decode(rows):
    result = {}
    for row in rows:
        i, j, w, a = row['q_degree'], row['c_degree'], row['word'], row['integer']
        if any(type(x) is not int for x in [i, j, a]) or min(i, j) < 0:
            raise ValueError('Nonnegative integral degrees, integer coefficient required')
        variable(w)
        key = i, j, w
        result[key] = result.get(key, 0)+a
    return clean(result)


def build():
    A, B, Z = map(variable, ['A', 'B', 'Z'])
    one = scalar(1)
    q, c = {(1, 0, ''): 1}, {(0, 1, ''): 1}
    t = add(q, neg(one))
    S = add(one, neg(mul(c, Z)))
    R0 = add(mul(Z, A), neg(mul(q, A, Z)), neg(mul(t, A, A)))
    R1 = add(mul(B, S), neg(A))
    H = add(A, mul(t, B), mul(c, t, B, A))
    P = add(mul(A, B), neg(mul(q, B, A)), mul(t, B, B), mul(c, t, B, A, B))
    # P*S = H*R1 - R1*A - c*B*R0, in the FREE algebra, not only its quotient.
    return dict(P=P, S=S, H=H, R0=R0, R1=R1, A=A, B=B, c=c)


def verify_identity(data, characteristic=0):
    required = ['P', 'S', 'H', 'R0', 'R1', 'A', 'B', 'c']
    if not all(k in data for k in required):
        return False
    # This verifies an explicitly supplied identity, not semantic assumptions.
    d = data
    remainder = add(mul(d['P'], d['S']), neg(mul(d['H'], d['R1'])),
                    mul(d['R1'], d['A']), mul(d['c'], d['B'], d['R0']))
    return not specialization(remainder, characteristic=characteristic)


def demo():
    d = build()
    assert verify_identity(d)
    assert d['P']
    assert verify_identity({k: decode(encode(v)) for k, v in d.items()})
    bad = dict(d)
    # Omitting the cubic correction does NOT give the asserted identity.
    bad['P'] = {k: v for k, v in d['P'].items() if k[2] != 'BAB'}
    assert not verify_identity(bad)
    # q stays indeterminate in characteristic p; numeric finite fields do not
    # contain an infinite-order q. The equalities still reduce modulo any p.
    for p in [2, 3, 5]:
        assert verify_identity({k: specialization(v, characteristic=p) for k, v in d.items()}, characteristic=p)
    return {
        'status': 'PASS', 'coefficient_ring': 'Z[q,c], q,c central; A,B,Z free',
        'identity': 'P*S = H*R1 - R1*A - c*B*R0',
        'polynomials': {k: encode(v) for k, v in d.items()},
        'universal_remainder': [], 'JSON_roundtrip': True,
        'omitted_cubic_rejected': True, 'mod_prime_symbolic_q_controls': [2, 3, 5],
        'unit_hypothesis': 'S=1-cZ must be a genuine unit (or otherwise right-cancellable) to conclude P=0',
        'drop_unit_counterexample': {'q': 2, 'c': 1, 'A': 0, 'B': 1, 'Z': 1,
                                    'R0': 0, 'R1': 0, 'S': 0, 'P': 1},
        'not_claimed': ['Lean verification', 'inverting A or B', 'full defining ideal',
                        'new general method', 'unread transfer success']}


if __name__ == '__main__':
    print(json.dumps(demo(), indent=2, sort_keys=True))
