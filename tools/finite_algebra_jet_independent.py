#!/usr/bin/env python3
"""Independent finite controls for the C8 finite-algebra/faithful-jet boundary.

Run: python3 tools/finite_algebra_jet_independent.py
Only standard-library integer polynomial arithmetic is used. These are
finite controls for explicit examples, not a test of a finiteness decision
procedure and not a proof of the general proposition.
"""

import json


def poly(a, p):
    a = [x % p if p else x for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p):
    return poly([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))], p)


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return poly(out, p)


def mm(a, b, p):
    out = [[[0] for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                out[i][j] = add(out[i][j], mul(a[i][k], b[k][j], p), p)
    return out


def jet(a, length, p):
    return [[poly(entry[:length], p) for entry in row] for row in a]


def nonzero(a):
    return any(any(entry) for row in a for entry in row)


def monomial(degree):
    return [0] * degree + [1]


def main():
    checks = 0
    for p in (0, 2, 3, 5, 7):
        zero = [[[0], [0]], [[0], [0]]]
        identity = [[[1], [0]], [[0], [1]]]
        # A support cycle is not itself an obstruction to finite algebra.
        projection = [[[1], [0, 1]], [[0], [0]]]
        assert mm(projection, projection, p) == projection
        checks += 1
        # I and P remain independent even after the one-coefficient jet:
        # their (1,1) and (2,2) entries distinguish the two coefficients.
        assert jet(projection, 1, p) == [[[1], [0]], [[0], [0]]]
        assert jet(identity, 1, p) == identity
        checks += 2
        for degree in (1, 2, 5, 9):
            v = [[[0], monomial(degree)], [[0], [0]]]
            assert mm(v, v, p) == zero
            assert not nonzero(jet(v, degree, p))
            assert nonzero(jet(v, degree + 1, p))
            checks += 3
        # Each generator is square-zero, but the joint algebra is infinite.
        a = [[[0], [0, 1]], [[0], [0]]]
        b = [[[0], [0]], [[1], [0]]]
        assert mm(a, a, p) == zero
        assert mm(b, b, p) == zero
        checks += 2
        ab = mm(a, b, p)
        power = identity
        for length in range(1, 10):
            power = mm(power, ab, p)
            assert power == [[monomial(length), [0]], [[0], [0]]]
            assert nonzero(power)
            assert not nonzero(jet(power, length, p))
            checks += 3
    assert checks == 220
    print(json.dumps({'fields': [0, 2, 3, 5, 7], 'checks': checks,
                      'examples': ['cyclic-support idempotent',
                                   'dimension-two arbitrary jet delay',
                                   'individually nilpotent infinite joint algebra'],
                      'result': 'PASS'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
