#!/usr/bin/env python3
"""Independent exact PM-FACTOR-B checks; no external algebra packages."""
from collections import deque

COUNTERS = {"pow_calls": 0, "pow_mults": 0, "scalar_tests": 0}


def trim(a, p):
    a = [x % p for x in a]
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b, p):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))], p)


def neg(a, p):
    return trim([-x for x in a], p)


def sub(a, b, p):
    return add(a, neg(b, p), p)


def scale(a, c, p):
    return trim([c*x for x in a], p)


def mul(a, b, p):
    if not a or not b:
        return ()
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % p
    return trim(c, p)


def divrem(a, b, p):
    assert b
    a = list(trim(a, p))
    q = [0] * max(0, len(a)-len(b)+1)
    leadinv = pow(b[-1], -1, p)
    while len(a) >= len(b):
        k = len(a)-len(b)
        c = a[-1] * leadinv % p
        q[k] = c
        for j in range(len(b)):
            a[k+j] = (a[k+j] - c*b[j]) % p
        while a and a[-1] == 0:
            a.pop()
    return trim(q, p), tuple(a)


def mod(a, f, p):
    return divrem(a, f, p)[1]


def mmul(a, b, f, p):
    return mod(mul(a, b, p), f, p)


def mpow(a, e, f, p):
    COUNTERS["pow_calls"] += 1
    a = mod(a, f, p)
    out = (1,)
    while e:
        if e & 1:
            out = mmul(out, a, f, p)
            COUNTERS["pow_mults"] += 1
        e //= 2
        if e:
            a = mmul(a, a, f, p)
            COUNTERS["pow_mults"] += 1
    return out


def gcd(a, b, p):
    while b:
        a, b = b, divrem(a, b, p)[1]
    return scale(a, pow(a[-1], -1, p), p) if a else ()


def invmod(a, f, p):
    r0, r1, s0, s1 = f, a, (), (1,)
    while r1:
        q, r = divrem(r0, r1, p)
        r0, r1 = r1, r
        s0, s1 = s1, sub(s0, mul(q, s1, p), p)
    assert len(r0) == 1
    return mod(scale(s0, pow(r0[0], -1, p), p), f, p)


def product(xs, p):
    out = (1,)
    for a in xs:
        out = mul(out, a, p)
    return out


def derivative(f, p):
    return trim([i*f[i] for i in range(1, len(f))], p)


def rref(mat, p):
    a = [list(row) for row in mat]
    nr, nc = len(a), len(a[0]) if a else 0
    pivots = []
    row = 0
    for col in range(nc):
        pivot = next((i for i in range(row, nr) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        a[row] = [x*pow(a[row][col], -1, p) % p for x in a[row]]
        for i in range(nr):
            if i != row and a[i][col]:
                c = a[i][col]
                a[i] = [(x-c*y) % p for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == nr:
            break
    return a, pivots


def fixed_basis(f, p):
    n = len(f)-1
    z = mpow((0, 1), p, f, p)
    cols = []
    w = (1,)
    for _ in range(n):
        cols.append(list(w) + [0]*(n-len(w)))
        w = mmul(w, z, f, p)
    mat = [[(cols[j][i] - (i == j)) % p for j in range(n)]
           for i in range(n)]
    a, pivots = rref(mat, p)
    basis = []
    for free in (j for j in range(n) if j not in pivots):
        v = [0]*n
        v[free] = 1
        for i, col in enumerate(pivots):
            v[col] = -a[i][free] % p
        basis.append(trim(v, p))
    assert all(mpow(v, p, f, p) == v for v in basis)
    return basis


def rank(polys, n, p):
    if not polys:
        return 0
    return len(rref([list(v) + [0]*(n-len(v)) for v in polys], p)[1])


def generated_dimension(gens, f, p):
    n = len(f)-1
    basis = [(1,)]
    queue = deque([(1,)])
    while queue:
        v = queue.popleft()
        for g in gens:
            w = mmul(v, g, f, p)
            if rank(basis+[w], n, p) > len(basis):
                basis.append(w)
                queue.append(w)
    return len(basis)


def partition(f, p, tests):
    assert gcd(f, derivative(f, p), p) == (1,), "squarefree required"
    pieces = [f]
    for c, labels in tests:
        assert len(set(labels)) == len(labels)
        assert mpow(c, p, f, p) == mod(c, f, p), "not Frobenius-fixed"
        ann = (1,)
        for a in labels:
            ann = mmul(ann, sub(c, (a,), p), f, p)
        assert not ann, "incorrect supplied codomain"
        newpieces = []
        for h in pieces:
            branch = []
            for a in labels:
                COUNTERS["scalar_tests"] += 1
                d = gcd(h, sub(c, (a,), p), p)
                if len(d) > 1:
                    branch.append(d)
            assert product(branch, p) == h
            newpieces.extend(branch)
        pieces = newpieces
    assert product(pieces, p) == f
    assert all(gcd(a, b, p) == (1,)
               for i, a in enumerate(pieces) for b in pieces[i+1:])
    return pieces


def crt_indicators(factors, p):
    f = product(factors, p)
    out = []
    for h in factors:
        q, rem = divrem(f, h, p)
        assert not rem
        out.append(mmul(q, invmod(mod(q, h, p), h, p), f, p))
    assert all(mmul(e, e, f, p) == e for e in out)
    assert sum(len(e) for e in out) >= 0
    total = ()
    for e in out:
        total = add(total, e, p)
    assert total == (1,)
    return f, out


def binary_family(factors, p):
    f, primitive = crt_indicators(factors, p)
    bits = (len(factors)-1).bit_length()
    out = []
    for bit in range(bits):
        e = ()
        for i, primitive_e in enumerate(primitive):
            if (i >> bit) & 1:
                e = add(e, primitive_e, p)
        assert mmul(e, e, f, p) == e
        out.append(e)
    return f, out


def main():
    p = 1_000_000_007
    factors = [(p-1, 1), (p-4, 1), (1, 0, 1)]
    f = product(factors, p)
    basis = fixed_basis(f, p)
    assert len(basis) == 3
    b = (0, 0, 1)
    assert mpow(b, p, f, p) == b
    assert generated_dimension([b], f, p) == 3
    c0 = mpow(b, (p-1)//2, f, p)
    c1 = mpow(sub(b, (1,), p), (p-1)//2, f, p)
    one = partition(f, p, [(c0, [0, 1, p-1])])
    two = partition(f, p, [(c0, [0, 1, p-1]), (c1, [0, 1, p-1])])
    assert len(one) == generated_dimension([c0], f, p) == 2
    assert len(two) == generated_dimension([c0, c1], f, p) == 3
    assert set(two) == set(factors)
    print("large-prime mixed-degree case: p=1000000007, n=4, fixed_dimension=3")
    print("observable X^2 generates B; Euler alone: 2 leaves; shifted Euler: 3 exact irreducible leaves")

    roots = list(range(2, 11))
    linear_factors = [(p-a, 1) for a in roots]
    f9, bits = binary_family(linear_factors, p)
    r9 = len(fixed_basis(f9, p))
    assert r9 == 9 and len(bits) == 4
    full = partition(f9, p, [(e, [0, 1]) for e in bits])
    incomplete = partition(f9, p, [(e, [0, 1]) for e in bits[:3]])
    assert set(full) == set(linear_factors)
    assert len(full) == generated_dimension(bits, f9, p) == 9
    assert len(incomplete) == generated_dimension(bits[:3], f9, p) == 8
    print("binary-certificate case: r=9, minimum_bits=4; four supplied bits give9 leaves; first3 give8")

    f2, e2 = binary_family([(0, 1), (1, 1), (1, 1, 1)], 2)
    assert len(fixed_basis(f2, 2)) == 3
    leaves2 = partition(f2, 2, [(e, [0, 1]) for e in e2])
    assert len(leaves2) == generated_dimension(e2, f2, 2) == 3
    print("characteristic2 mixed-degree case: n=4, r=3, two binary idempotents give3 leaves")

    rejected = False
    try:
        partition(f, p, [(b, [0, 1])])
    except AssertionError as exc:
        rejected = str(exc) == "incorrect supplied codomain"
    assert rejected
    repeated = (0, 0, 1)
    assert len(fixed_basis(repeated, p)) == 1
    rejected = False
    try:
        partition(repeated, p, [])
    except AssertionError as exc:
        rejected = str(exc) == "squarefree required"
    assert rejected
    print("negative controls: false small-codomain certificate rejected; nonreduced input rejected")
    print("exact counters:", COUNTERS)
    print("ALL ASSERTIONS PASSED; no loop over F_p, no random choices, no factorization package")


if __name__ == "__main__":
    main()
