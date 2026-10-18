"""Exact small-field cancellation experiments. Standard library only.

Elements are base-p integers encoding polynomials in a, reduced by a supplied
monic irreducible polynomial (coefficients in ascending order). This is research
software for small fields, not a cryptographic implementation.
"""
from itertools import product, permutations
from math import comb, isqrt
from typing import Sequence


def _prime(p: int) -> bool:
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def _remainder(a: Sequence[int], b: Sequence[int], p: int) -> tuple[int, ...]:
    a = [x % p for x in a]
    while a and not a[-1]:
        a.pop()
    while len(a) >= len(b):
        c = a[-1] * pow(b[-1], -1, p) % p
        k = len(a) - len(b)
        for j, v in enumerate(b):
            a[k + j] = (a[k + j] - c * v) % p
        while a and not a[-1]:
            a.pop()
    return tuple(a)


class Field:
    """Validated finite field of at most 256 elements, using exact tables."""

    def __init__(self, p: int, modulus: Sequence[int]):
        if not isinstance(p, int) or not _prime(p):
            raise ValueError('characteristic must be prime')
        self.p = p
        self.modulus = tuple(c % p for c in modulus)
        if len(self.modulus) < 2 or self.modulus[-1] != 1:
            raise ValueError('modulus must be monic with positive degree')
        self.degree = len(self.modulus) - 1
        self.q = p ** self.degree
        if self.q > 256:
            raise ValueError('small-field implementation: q must be <= 256')
        # A reducible polynomial has a monic factor of degree <= degree/2.
        for d in range(1, self.degree // 2 + 1):
            for low in product(range(p), repeat=d):
                if not _remainder(self.modulus, (*low, 1), p):
                    raise ValueError('modulus is reducible')
        digits = [tuple((x // p ** i) % p for i in range(self.degree))
                  for x in range(self.q)]
        self.add = [[sum(((a[i] + b[i]) % p) * p ** i
                         for i in range(self.degree)) for b in digits] for a in digits]
        self.neg = [sum((-v % p) * p ** i for i, v in enumerate(a)) for a in digits]
        self.mul = []
        for a in digits:
            row = []
            for b in digits:
                c = [0] * (2 * self.degree - 1)
                for i, u in enumerate(a):
                    for j, v in enumerate(b):
                        c[i + j] = (c[i + j] + u * v) % p
                rem = _remainder(c, self.modulus, p)
                row.append(sum(v * p ** i for i, v in enumerate(rem)))
            self.mul.append(row)
        self.power_table = [[self.pow(x, n) for n in range(self.q)] for x in range(self.q)]

    def pow(self, x: int, n: int) -> int:
        if not 0 <= x < self.q or n < 0:
            raise ValueError('invalid field element or negative exponent')
        out = 1
        while n:
            if n & 1:
                out = self.mul[out][x]
            x = self.mul[x][x]
            n >>= 1
        return out

    def weights(self, mu: Sequence[int]) -> tuple[int, ...]:
        if len(mu) != self.q or any(not isinstance(x, int) or not 0 <= x < self.q for x in mu):
            raise ValueError('weights must be q valid field elements')
        return tuple(mu)

    def delta(self, x: int) -> tuple[int, ...]:
        if not 0 <= x < self.q:
            raise ValueError('invalid support point')
        return tuple(int(i == x) for i in range(self.q))

    def difference(self, a: int) -> tuple[int, ...]:
        out = list(self.delta(a))
        out[0] = self.add[out[0]][self.neg[1]]
        return tuple(out)

    def convolution(self, mu: Sequence[int], nu: Sequence[int]) -> tuple[int, ...]:
        mu, nu = self.weights(mu), self.weights(nu)
        out = [0] * self.q
        for x, u in enumerate(mu):
            for y, v in enumerate(nu):
                z = self.add[x][y]
                out[z] = self.add[out[z]][self.mul[u][v]]
        return tuple(out)

    def moments(self, mu: Sequence[int]) -> tuple[int, ...]:
        mu = self.weights(mu)
        out = []
        for n in range(self.q):
            v = 0
            for x, w in enumerate(mu):
                v = self.add[v][self.mul[w][self.power_table[x][n]]]
            out.append(v)
        return tuple(out)

    def moment_product(self, a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
        """Second route: binomial contraction, without forming a convolution."""
        a, b = self.weights(a), self.weights(b)
        out = []
        for n in range(self.q):
            v = 0
            for i in range(n + 1):
                t = self.mul[comb(n, i) % self.p][self.mul[a[i]][b[n - i]]]
                v = self.add[v][t]
            out.append(v)
        return tuple(out)

    def saturated(self, directions: Sequence[int]) -> tuple[int, ...]:
        mu = self.delta(0)
        for a in directions:
            for _ in range(self.p - 1):
                mu = self.convolution(mu, self.difference(a))
        return mu

    def span(self, directions: Sequence[int]) -> set[int]:
        points = {0}
        for a in directions:
            if not 0 <= a < self.q:
                raise ValueError('invalid direction')
            points = {self.add[x][self.mul[c][a]] for x in points for c in range(self.p)}
        return points

    def derivative_constant(self, points: set[int]) -> int:
        """Coefficient of X in product(X-w), when 0 is one of the roots."""
        if 0 not in points:
            raise ValueError('the subspace must contain zero')
        result = 1
        for w in sorted(points - {0}):
            result = self.mul[result][self.neg[w]]
        return result

    def moore_det(self, directions: Sequence[int]) -> int:
        """Small determinant by permutations, independent of the root product."""
        d = len(directions)
        total = 0
        for perm in permutations(range(d)):
            inversions = sum(perm[i] > perm[j] for i in range(d) for j in range(i + 1, d))
            term = self.neg[1] if inversions % 2 else 1
            for i, j in enumerate(perm):
                term = self.mul[term][self.pow(directions[j], self.p ** i)]
            total = self.add[total][term]
        return total


def order(moments: Sequence[int]) -> int | None:
    """None means all supplied moments vanish; infinity only if range is complete."""
    return next((n for n, x in enumerate(moments) if x), None)


def carry_free(r: int, s: int, p: int) -> bool:
    if r < 0 or s < 0 or not _prime(p):
        raise ValueError('require nonnegative indices and a prime')
    while r or s:
        if r % p + s % p >= p:
            return False
        r //= p
        s //= p
    return True


def standard_fields() -> list[Field]:
    return [Field(2, (0, 1)), Field(3, (0, 1)), Field(2, (1, 1, 1)),
            Field(2, (1, 1, 0, 1)), Field(3, (1, 0, 1))]
