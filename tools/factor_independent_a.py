#!/usr/bin/env python3
"""Exact, standalone checks for PM-FACTOR-A. No third-party dependencies.

This is finite arithmetic testing, not a complexity benchmark or a proof of
the quantified theorems. The intentionally slow independent divisor search
is used ONLY as a finite validation oracle, never by the proposed constructor.
"""
from itertools import product


def norm(a, p):
    a = [x % p for x in a]
    while a and not a[-1]:
        a.pop()
    return tuple(a)


def add(a, b, p):
    return norm([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))], p)


def scale(a, c, p):
    return norm([c*x for x in a], p)


def sub(a, b, p):
    return add(a, scale(b, -1, p), p)


def mul(a, b, p):
    if not a or not b:
        return ()
    c = [0] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return norm(c, p)


def divmodp(a, b, p):
    assert b
    a = list(norm(a, p))
    q = [0] * max(0, len(a)-len(b)+1)
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b):
        k = len(a)-len(b)
        c = a[-1]*inv % p
        q[k] = c
        for j, x in enumerate(b):
            a[j+k] = (a[j+k]-c*x) % p
        while a and not a[-1]:
            a.pop()
    return norm(q, p), tuple(a)


def rem(a, f, p):
    return divmodp(a, f, p)[1]


def gcd(a, b, p):
    while b:
        a, b = b, rem(a, b, p)
    return scale(a, pow(a[-1], -1, p), p) if a else ()


def xgcd(a, b, p):
    aa, bb, u, v, w, z = a, b, (1,), (), (), (1,)
    while bb:
        q, rr = divmodp(aa, bb, p)
        aa, bb = bb, rr
        u, w = w, sub(u, mul(q, w, p), p)
        v, z = z, sub(v, mul(q, z, p), p)
    c = pow(aa[-1], -1, p)
    return scale(aa, c, p), scale(u, c, p), scale(v, c, p)


def powmod(a, e, f, p):
    out = rem((1,), f, p)
    a = rem(a, f, p)
    while e:
        if e & 1:
            out = rem(mul(out, a, p), f, p)
        a = rem(mul(a, a, p), f, p)
        e >>= 1
    return out


def evaluate(h, b, f, p):
    out = ()
    for c in reversed(h):
        out = rem(add(mul(out, b, p), (c,), p), f, p)
    return out


def vec(a, n):
    return list(a) + [0]*(n-len(a))


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matmul(a, b, p):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


def columns(cs, n):
    return [[c[i] if i < len(c) else 0 for c in cs] for i in range(n)]


def rref(a, p):
    a = [row[:] for row in a]
    n = len(a)
    t = identity(n)
    pivots = []
    rr = 0
    for j in range(len(a[0])):
        ii = next((i for i in range(rr, n) if a[i][j] % p), None)
        if ii is None:
            continue
        a[ii], a[rr] = a[rr], a[ii]
        t[ii], t[rr] = t[rr], t[ii]
        c = pow(a[rr][j], -1, p)
        a[rr] = [c*x % p for x in a[rr]]
        t[rr] = [c*x % p for x in t[rr]]
        for i in range(n):
            if i != rr and a[i][j]:
                c = a[i][j]
                a[i] = [(x-c*y) % p for x, y in zip(a[i], a[rr])]
                t[i] = [(x-c*y) % p for x, y in zip(t[i], t[rr])]
        pivots.append(j)
        rr += 1
        if rr == n:
            break
    return a, pivots, t


def fixed_algebra(f, p):
    n = len(f)-1
    xp = powmod((0, 1), p, f, p)
    cs = [(1,)]
    for _ in range(1, n):
        cs.append(rem(mul(cs[-1], xp, p), f, p))
    ff = columns(cs, n)
    mm = [[(ff[i][j]-int(i == j)) % p for j in range(n)]
          for i in range(n)]
    rr, pivots, tt = rref(mm, p)
    free = [j for j in range(n) if j not in pivots]
    basis = []
    for j in free:
        u = [0]*n
        u[j] = 1
        for i, k in enumerate(pivots):
            u[k] = -rr[i][j] % p
        basis.append(norm(u, p))
    # Finite rank/complete-kernel certificate. Verify independently of queue.
    assert matmul(tt, mm, p) == rr
    assert len(rref(tt, p)[1]) == n
    assert len(rref(columns(basis, n), p)[1]) == len(basis)
    assert matmul(mm, columns(basis, n), p) == [[0]*len(basis) for _ in range(n)]
    assert len(basis)+len(pivots) == n
    assert all(powmod((0, 1), p*j, f, p) == cs[j] for j in range(n))
    assert all(powmod(b, p, f, p) == b for b in basis)
    return basis, ff


def minpoly(b, f, p):
    n = len(f)-1
    powers = [(1,)]
    for k in range(1, n+1):
        powers.append(rem(mul(powers[-1], b, p), f, p))
        rr, pivots, _ = rref(columns(powers, n), p)
        if len(pivots) == k:
            assert pivots == list(range(k))
            m = tuple([-rr[i][k] % p for i in range(k)] + [1])
            # Minimality and all-degree relation certificate.
            assert len(rref(columns(powers[:-1], n), p)[1]) == k
            assert evaluate(m, b, f, p) == ()
            return m
    raise AssertionError("finite-dimensional algebra failed a dependence")


def factor_scan(f, basis, p):
    parts = [f]
    for b in basis:
        for a in range(p):
            refined = []
            for h in parts:
                g = gcd(h, sub(b, (a,), p), p)
                if 1 < len(g) < len(h):
                    q, rr = divmodp(h, g, p)
                    assert not rr
                    refined.extend((g, q))
                else:
                    refined.append(h)
            parts = refined
    return sorted(parts)


def brute_factor(f, p):
    # Independent finite validation only; deliberately not efficient.
    n = len(f)-1
    for d in range(1, n//2+1):
        for coeff in product(range(p), repeat=d):
            h = tuple(coeff)+(1,)
            q, rr = divmodp(f, h, p)
            if not rr:
                return sorted(brute_factor(h, p)+brute_factor(q, p))
    return [f]


def separator_large_field(f, basis, p):
    r = len(basis)
    dd = r*(r-1)//2
    assert p > dd
    b = ()
    history = []
    for c in basis:
        best = None
        for lam in range(dd+1):
            trial = add(b, scale(c, lam, p), p)
            m = minpoly(trial, f, p)
            if best is None or len(m) > len(best[1]):
                best = trial, m, lam
        b, m, lam = best
        history.append((lam, len(m)-1))
    assert len(minpoly(b, f, p))-1 == r
    return b, history


def check_one(f, p):
    n = len(f)-1
    deriv = norm([i*f[i] for i in range(1, len(f))], p)
    if gcd(f, deriv, p) != (1,):
        return False
    basis, ff = fixed_algebra(f, p)
    ground_truth = brute_factor(f, p)
    assert len(basis) == len(ground_truth)
    assert factor_scan(f, basis, p) == ground_truth
    for b in basis:
        m = minpoly(b, f, p)
        assert len(m)-1 <= len(basis)
        assert powmod((0, 1), p, m, p) == rem((0, 1), m, p)
        roots = [a for a in range(p) if evaluate(m, (a,), (0, 1), p) == ()]
        assert len(roots) == len(m)-1
        es = []
        for a in roots:
            vv, rr = divmodp(m, ((-a) % p, 1), p)
            assert not rr
            va = evaluate(vv, (a,), (0, 1), p)
            assert len(va) == 1 and va[0]
            e = scale(evaluate(vv, b, f, p), pow(va[0], -1, p), p)
            # Two independently computed selector constructions agree.
            fermat = sub((1,), powmod(sub(b, (a,), p), p-1, f, p), p)
            assert e == fermat
            assert rem(sub(mul(e, e, p), e, p), f, p) == ()
            assert rem(mul(sub(b, (a,), p), e, p), f, p) == ()
            assert gcd(f, sub(b, (a,), p), p) == gcd(f, sub((1,), e, p), p)
            es.append(e)
        ee = ()
        for e in es:
            ee = add(ee, e, p)
        assert ee == (1,)
        for i, e in enumerate(es):
            for j in range(i):
                assert rem(mul(e, es[j], p), f, p) == ()
        if len(roots) > 1:
            # Root-free transport from a coprime partition m=u*v.
            u = ((-roots[0]) % p, 1)
            v, rr = divmodp(m, u, p)
            assert not rr
            one, alpha, beta = xgcd(u, v, p)
            assert one == (1,)
            assert add(mul(alpha, u, p), mul(beta, v, p), p) == (1,)
            e = evaluate(mul(beta, v, p), b, f, p)
            assert e not in ((), (1,))
            assert rem(sub(mul(e, e, p), e, p), f, p) == ()
            g = gcd(f, e, p)
            assert 1 < len(g) < len(f)
    if p > len(basis)*(len(basis)-1)//2:
        separator_large_field(f, basis, p)
    return True


def main():
    total = 0
    for p, max_degree in ((2, 5), (3, 4), (5, 3), (7, 2)):
        subtotal = 0
        for n in range(1, max_degree+1):
            for coeff in product(range(p), repeat=n):
                if check_one(tuple(coeff)+(1,), p):
                    subtotal += 1
        total += subtotal
        print(f"p={p}: {subtotal} squarefree monic inputs checked")
    # r>p: scalar separation impossible, joint basis still factors correctly.
    p = 2
    f = mul(mul((0, 1), (1, 1), p), (1, 1, 1), p)
    basis, _ = fixed_algebra(f, p)
    assert len(basis) == 3 > p
    fixed_elements = []
    for coeff in product(range(p), repeat=len(basis)):
        b = ()
        for c, u in zip(coeff, basis):
            b = add(b, scale(u, c, p), p)
        fixed_elements.append(b)
    assert max(len(minpoly(b, f, p))-1 for b in fixed_elements) == p
    assert factor_scan(f, basis, p) == brute_factor(f, p)
    print("r>p boundary: r=3,p=2; maximum scalar minimal degree=2; joint readout succeeds")
    # Infinite-family structural boundary illustrated, not inferred from test.
    p = 101
    f = (1,)
    for a in (2, 7, 19, 37, 61, 89):
        f = mul(f, ((-a) % p, 1), p)
    basis, ff = fixed_algebra(f, p)
    assert ff == identity(6)
    b, history = separator_large_field(f, basis, p)
    assert len(minpoly(b, f, p))-1 == 6
    print(f"split-input control: p=101,n=6,F=I; separator minimal degree=6; history={history}")
    print(f"PASS: {total} exhaustive squarefree inputs plus two boundary controls; all exact identities verified")


if __name__ == "__main__":
    main()
