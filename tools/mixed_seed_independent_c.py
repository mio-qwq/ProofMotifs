#!/usr/bin/env python3
"""PM-MIX-C: universal certificate plus finite exact regression checks.

No third-party dependencies. The free-polynomial identity is universal;
truncations are regressions, not a proof by finite ranks. Rightmost acts first.
"""

from fractions import Fraction


class CP:
    """Commutative polynomials over Z in q,c."""
    def __init__(self, terms=0):
        self.terms = ({(0, 0): terms} if isinstance(terms, int) and terms else
                      {} if isinstance(terms, int) else {m: a for m, a in terms.items() if a})
    def __add__(self, other):
        other = other if isinstance(other, CP) else CP(other)
        out = dict(self.terms)
        for m, a in other.terms.items():
            out[m] = out.get(m, 0) + a
        return CP(out)
    __radd__ = __add__
    def __neg__(self):
        return CP({m: -a for m, a in self.terms.items()})
    def __sub__(self, other):
        return self + -other if isinstance(other, CP) else self + CP(-other)
    def __rsub__(self, other):
        return -self + other
    def __mul__(self, other):
        other = other if isinstance(other, CP) else CP(other)
        out = {}
        for (i, j), a in self.terms.items():
            for (k, l), b in other.terms.items():
                m = (i + k, j + l)
                out[m] = out.get(m, 0) + a * b
        return CP(out)
    __rmul__ = __mul__
    def __eq__(self, other):
        other = other if isinstance(other, CP) else CP(other)
        return self.terms == other.terms
    def __bool__(self):
        return bool(self.terms)


q, c = CP({(1, 0): 1}), CP({(0, 1): 1})


def nc_add(*items):
    out = {}
    for item in items:
        for word, coefficient in item.items():
            value = out.get(word, CP()) + coefficient
            if value:
                out[word] = value
            else:
                out.pop(word, None)
    return out


def nc_scale(a, p):
    return {w: a * v for w, v in p.items() if a * v}


def nc_mul(p, r):
    out = {}
    for w, a in p.items():
        for v, b in r.items():
            out = nc_add(out, {w + v: a * b})
    return out


def universal_certificate():
    one = {(): CP(1)}
    A, B, Z = ({(x,): CP(1)} for x in ("A", "B", "Z"))
    S = nc_add(one, nc_scale(-c, Z))
    R0 = nc_add(nc_mul(Z, A), nc_scale(-q, nc_mul(A, Z)),
                nc_scale(1 - q, nc_mul(A, A)))
    R1 = nc_add(nc_mul(B, S), nc_scale(-1, A))
    P = nc_add(nc_mul(A, B), nc_scale(-q, nc_mul(B, A)),
               nc_scale(q - 1, nc_mul(B, B)),
               nc_scale(c * (q - 1), nc_mul(nc_mul(B, A), B)))
    assert P and P[("A", "B")] == 1
    H = nc_add(A, nc_scale(q - 1, B), nc_scale(c * (q - 1), nc_mul(B, A)))
    certificate = nc_add(nc_mul(P, S), nc_mul(R1, A),
                         nc_scale(c, nc_mul(B, R0)),
                         nc_scale(-1, nc_mul(H, R1)))
    assert certificate == {}, certificate
    print("PASS universal free-polynomial certificate over Z[q,c]")
    print("P*S + R1*A + c*B*R0 - (A+(q-1)B+c(q-1)BA)*R1 = 0")
    # Cleared local telescoping identity with c standing for s:
    # (q-1)/((s-1)(qs-1)) = 1/(s-1)-q/(qs-1).
    assert (q - 1) - (q * c - 1) + q * (c - 1) == 0
    print("PASS universally cleared rational telescoping kernel")


def trim(f, p):
    f = [x % p for x in f]
    while f and f[-1] == 0:
        f.pop()
    return tuple(f)


def pa(f, g, p):
    return trim([(f[i] if i < len(f) else 0) + (g[i] if i < len(g) else 0)
                 for i in range(max(len(f), len(g)))], p)


def pn(f, p):
    return trim([-x for x in f], p)


def pm(f, g, p):
    out = [0] * max(0, len(f) + len(g) - 1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            out[i + j] += x * y
    return trim(out, p)


def pd(f, g, p):
    assert g
    f, out = list(f), [0] * max(0, len(f) - len(g) + 1)
    while f and len(f) >= len(g):
        n = len(f) - len(g)
        a = f[-1] * pow(g[-1], -1, p) % p
        out[n] = a
        f = list(pa(f, (0,) * n + tuple(-a * x for x in g), p))
    return trim(out, p), trim(f, p)


def pg(f, g, p):
    while g:
        _, r = pd(f, g, p)
        f, g = g, r
    return trim([x * pow(f[-1], -1, p) for x in f], p) if f else ()


class FpT:
    """Exact rational functions over F_p(t), with Euclidean cancellation."""
    def __init__(self, a=0, p=3, b=(1,)):
        a = (a,) if isinstance(a, int) else a
        a, b = trim(a, p), trim(b, p)
        assert b
        g = pg(a, b, p)
        a, ra = pd(a, g, p)
        b, rb = pd(b, g, p)
        assert not ra and not rb
        u = pow(b[-1], -1, p)
        self.a, self.b, self.p = trim([x * u for x in a], p), trim([x * u for x in b], p), p
    def coerce(self, other):
        other = other if isinstance(other, FpT) else FpT(other, self.p)
        assert self.p == other.p
        return other
    def __add__(self, other):
        other = self.coerce(other)
        return FpT(pa(pm(self.a, other.b, self.p), pm(other.a, self.b, self.p), self.p),
                   self.p, pm(self.b, other.b, self.p))
    __radd__ = __add__
    def __neg__(self):
        return FpT(pn(self.a, self.p), self.p, self.b)
    def __sub__(self, other):
        return self + -self.coerce(other)
    def __rsub__(self, other):
        return self.coerce(other) + -self
    def __mul__(self, other):
        other = self.coerce(other)
        return FpT(pm(self.a, other.a, self.p), self.p, pm(self.b, other.b, self.p))
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = self.coerce(other)
        assert other.a
        return FpT(pm(self.a, other.b, self.p), self.p, pm(self.b, other.a, self.p))
    def __pow__(self, n):
        assert n >= 0
        out, base = FpT(1, self.p), self
        while n:
            if n & 1:
                out = out * base
            base, n = base * base, n // 2
        return out
    def __eq__(self, other):
        other = self.coerce(other)
        return self.a == other.a and self.b == other.b
    def __bool__(self):
        return bool(self.a)


def truncated_regression(q, c, size, label):
    zero, one = q - q, q**0
    denominators = [zero] + [q**n - one for n in range(1, size)]
    assert all(denominators[1:])
    def A(f):
        return [zero] + [f[n - 1] / denominators[n] for n in range(1, size)]
    def B(f):
        return [zero] + [sum((c**(n - j - 1) * f[j] for j in range(n)), zero)
                          / denominators[n] for n in range(1, size)]
    for m in range(size):
        f = [zero] * size
        f[m] = one
        AB, BA, BB, BAB = A(B(f)), B(A(f)), B(B(f)), B(A(B(f)))
        result = [AB[n] - q * BA[n] + (q - one) * BB[n]
                  + c * (q - one) * BAB[n] for n in range(size)]
        assert all(x == zero for x in result), (label, m)
    print(f"PASS all {size} input monomials modulo z^{size}: {label}")


if __name__ == "__main__":
    universal_certificate()
    truncated_regression(Fraction(2), Fraction(1), 18, "Q,q=2,c=1")
    truncated_regression(Fraction(3), Fraction(0), 12, "Q,q=3,c=0")
    for p in (2, 3, 5):
        truncated_regression(FpT((0, 1), p), FpT(1, p), 9, f"F_{p}(t),q=t,c=1")
    print("No finite-order q specialization, no word-rank scan, no floating point.")
