#!/usr/bin/env python3
"""Classical Berlekamp readout from supplied small-label observables.

p is PROMISED prime; no sqrt(p) trial validation is hidden in the bit cost.
This verifies/splits supplied observables, not discovers factors or tests.
Dense coefficient lists are ascending; the input must be monic squarefree.
"""
import json
from collections import deque


def trim(a, p):
    a = [x % p for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))], p)


def neg(a, p):
    return trim([-x for x in a], p)


def mul(a, b, p):
    c = [0] * max(0, len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % p
    return trim(c, p)


def divmod_poly(a, b, p):
    a, b = trim(a, p), trim(b, p)
    if not b:
        raise ValueError('division by zero polynomial')
    q = [0] * max(0, len(a)-len(b)+1)
    inv = pow(b[-1], -1, p)
    while a and len(a) >= len(b):
        k, c = len(a)-len(b), a[-1]*inv % p
        q[k] = c
        for j, x in enumerate(b):
            a[k+j] = (a[k+j]-c*x) % p
        a = trim(a, p)
    return trim(q, p), a


def mod(a, f, p):
    return divmod_poly(a, f, p)[1]


def gcd(a, b, p):
    while b:
        a, b = b, mod(a, b, p)
    return trim([x*pow(a[-1], -1, p) for x in a], p) if a else []


def power(a, k, f, p):
    if type(k) is not int or k < 0:
        raise ValueError('nonnegative integer exponent required')
    out = [1]
    a = mod(a, f, p)
    while k:
        if k & 1:
            out = mod(mul(out, a, p), f, p)
        a = mod(mul(a, a, p), f, p)
        k >>= 1
    return out


def rref(rows, p):
    rows = [list(row) for row in rows]
    n = len(rows[0]) if rows else 0
    pivots = []
    for c in range(n):
        k = next((k for k in range(len(pivots), len(rows)) if rows[k][c] % p), None)
        if k is None:
            continue
        j = len(pivots)
        rows[j], rows[k] = rows[k], rows[j]
        u = pow(rows[j][c] % p, -1, p)
        rows[j] = [x*u % p for x in rows[j]]
        for k in range(len(rows)):
            if k != j:
                u = rows[k][c] % p
                rows[k] = [(x-u*y) % p for x, y in zip(rows[k], rows[j])]
        pivots.append(c)
        if len(pivots) == len(rows):
            break
    return rows, pivots


def kernel(rows, p):
    reduced, pivots = rref(rows, p)
    n = len(rows[0])
    out = []
    for c in range(n):
        if c not in pivots:
            v = [int(i == c) for i in range(n)]
            for j, k in enumerate(pivots):
                v[k] = -reduced[j][c] % p
            out.append(v)
    return out


def checked_input(p, f):
    if type(p) is not int or p < 2:
        raise ValueError('p >= 2, promised prime')
    if not isinstance(f, list) or any(type(x) is not int for x in f):
        raise ValueError('integer coefficient list required')
    f = trim(f, p)
    if len(f) < 2 or f[-1] != 1:
        raise ValueError('positive-degree monic polynomial required')
    derivative = trim([i*f[i] for i in range(1, len(f))], p)
    if gcd(f, derivative, p) != [1]:
        raise ValueError('squarefree modulus required; multiplicities are not certified')
    return f


def fixed_basis(p, f):
    """Kernel basis with p promised prime, f already checked if public input."""
    n = len(f)-1
    xp = power([0, 1], p, f, p)
    columns, a = [], [1]
    for j in range(n):
        v = a + [0]*(n-len(a))
        v[j] = (v[j]-1) % p
        columns.append(v)
        a = mod(mul(a, xp, p), f, p)
    return kernel([[columns[j][i] for j in range(n)] for i in range(n)], p)


def generated_basis(p, f, generators):
    """Finite unital algebra closure, no scalar/root search."""
    n, basis, pending, offered, reducers = len(f)-1, [], deque([[1]]), 0, {}
    while pending:
        a = pending.popleft()
        padded = a + [0]*(n-len(a))
        reduced = padded[:]
        for pivot in sorted(reducers):
            c = reduced[pivot]
            reduced = [(x-c*y) % p for x, y in zip(reduced, reducers[pivot])]
        pivot = next((i for i, x in enumerate(reduced) if x), None)
        if pivot is None:
            continue
        inv = pow(reduced[pivot], -1, p)
        reducers[pivot] = [x*inv % p for x in reduced]
        basis.append(padded)
        for e in generators:
            pending.append(mod(mul(a, e, p), f, p))
            offered += 1
    return basis, offered


def readout(p, f, tests):
    """Verify small codomains, return exact factors of the induced partition.

    COMPLETE means irreducible factors; PARTIAL means certified coprime blocks.
    Reject malformed tests rather than silently infer scalar labels/primehood.
    """
    f = checked_input(p, f)
    n = len(f)-1
    if not isinstance(tests, list):
        raise ValueError('test list required')
    parsed = []
    for test in tests:
        if not isinstance(test, dict) or 'poly' not in test or 'labels' not in test:
            raise ValueError('each test requires poly and labels')
        b, labels = test['poly'], test['labels']
        if not isinstance(b, list) or len(b) > n or any(type(x) is not int for x in b):
            raise ValueError('integer observable of degree less than n required')
        if (not isinstance(labels, list) or not labels or
                any(type(x) is not int or not 0 <= x < p for x in labels) or
                len(set(labels)) != len(labels)):
            raise ValueError('distinct canonical prime-field labels required')
        b = mod(b, f, p)
        annihilator = [1]
        for c in labels:
            annihilator = mod(mul(annihilator, add(b, [-c], p), p), f, p)
        if annihilator:
            raise ValueError('supplied labels do not cover this observable')
        parsed.append((b, labels))
    rank = len(fixed_basis(p, f))
    blocks = [f]
    for b, labels in parsed:
        next_blocks = []
        for h in blocks:
            for c in labels:
                g = gcd(h, add(b, [-c], p), p)
                if len(g) > 1:
                    next_blocks.append(g)
        blocks = next_blocks
    product = [1]
    for h in blocks:
        product = mul(product, h, p)
    if product != f or len(blocks) > rank:
        raise ArithmeticError('partition invariant violated')
    basis, offered = generated_basis(p, f, [b for b, _ in parsed])
    if len(basis) != len(blocks):
        raise ArithmeticError('algebra dimension and partition count disagree')
    return {'p': p, 'modulus': f, 'tests': tests, 'fixed_dimension': rank,
            'observable_algebra_dimension': len(basis),
            'closure_product_offers': offered,
            'blocks': sorted(blocks, key=lambda h: (len(h), h)),
            'status': 'COMPLETE' if len(blocks) == rank else 'PARTIAL',
            'primehood': 'input promise; not independently tested'}


def demo():
    p = 1000000007
    f = [4, -5, 5, -5, 1]  # (X-1)(X-4)(X^2+1); -1 nonsquare.
    b = [0, 0, 1]
    z1 = power(b, (p-1)//2, f, p)
    z2 = power(add(b, [-1], p), (p-1)//2, f, p)
    one = {'poly': z1, 'labels': [p-1, 1]}
    two = {'poly': z2, 'labels': [p-1, 0, 1]}
    partial = readout(p, f, [one])
    complete = readout(p, f, [one, two])
    assert partial['status'] == 'PARTIAL' and complete['status'] == 'COMPLETE'
    # These tests are supplied/source-informed, NOT discovered by a solver.
    return {'contract': 'supplied finite-label tests; no field scan or discovery',
            'partial': partial, 'complete': complete,
            'nonreduced_control': 'X^2 rejected by squarefree validation'}


if __name__ == '__main__':
    print(json.dumps(demo(), indent=2, sort_keys=True))
