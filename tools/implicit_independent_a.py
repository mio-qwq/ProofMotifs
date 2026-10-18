"""Exact, dictionary-free frontier evaluation-basis constructor.

Task PM-IMPLICIT-A. No third-party dependencies; fixed controls only.
"""
from fractions import Fraction


class Field:
    def __init__(self, p=None):
        self.p = p

    def coerce(self, x):
        return Fraction(x) if self.p is None else x % self.p

    def add(self, x, y):
        return x + y if self.p is None else (x + y) % self.p

    def sub(self, x, y):
        return x - y if self.p is None else (x - y) % self.p

    def mul(self, x, y):
        return x * y if self.p is None else (x * y) % self.p

    def inv(self, x):
        assert x != 0
        return 1 / x if self.p is None else pow(x, -1, self.p)


def matvec(F, a, v):
    return [sum_field(F, [F.mul(x, y) for x, y in zip(row, v)]) for row in a]


def sum_field(F, xs):
    a = F.coerce(0)
    for x in xs:
        a = F.add(a, x)
    return a


def inverse(F, a):
    m = len(a)
    w = [row[:] + [F.coerce(i == j) for j in range(m)] for i, row in enumerate(a)]
    for j in range(m):
        k = next(i for i in range(j, m) if w[i][j] != 0)
        w[j], w[k] = w[k], w[j]
        c = F.inv(w[j][j])
        w[j] = [F.mul(c, x) for x in w[j]]
        for i in range(m):
            if i != j:
                c = w[i][j]
                w[i] = [F.sub(x, F.mul(c, y)) for x, y in zip(w[i], w[j])]
    return [row[m:] for row in w]


def construct(F, points):
    m, n = len(points), len(points[0])
    H = [[F.coerce(x) for x in h] for h in points]
    pivots, reduced = [], []

    def independent(v):
        w = v[:]
        for p, r in zip(pivots, reduced):
            c = w[p]
            w = [F.sub(x, F.mul(c, y)) for x, y in zip(w, r)]
        p = next((i for i, x in enumerate(w) if x != 0), None)
        if p is None:
            return False
        c = F.inv(w[p])
        pivots.append(p)
        reduced.append([F.mul(c, x) for x in w])
        return True

    basis = [(0,) * n]
    values = [[F.coerce(1)] * m]
    assert independent(values[0])
    frontier, ranks, count = [0], [1], 0
    while len(basis) < m:
        nxt = []
        for j in frontier:
            for i in range(n):
                count += 1
                v = [F.mul(H[a][i], values[j][a]) for a in range(m)]
                if independent(v):
                    exponent = list(basis[j])
                    exponent[i] += 1
                    nxt.append(len(basis))
                    basis.append(tuple(exponent))
                    values.append(v)
                    if len(basis) == m:
                        break
            if len(basis) == m:
                break
        assert nxt, "Nonseparating input or implementation error"
        frontier = nxt
        ranks.append(len(basis))
    E = [[values[j][a] for j in range(m)] for a in range(m)]
    return H, basis, E, inverse(F, E), ranks, count


def verify(F, H, basis, E, C):
    """Check cardinality, all needed border inclusions, and a dual witness."""
    m, n = len(H), len(H[0])
    deg = [sum(b) for b in basis]
    D = max(deg)
    assert basis[0] == (0,) * n
    for a in range(m):
        for j, b in enumerate(basis):
            v = F.coerce(1)
            for x, e in zip(H[a], b):
                for _ in range(e):
                    v = F.mul(v, x)
            assert v == E[a][j]
    for j in range(m):
        e = [F.coerce(i == j) for i in range(m)]
        col = [C[k][j] for k in range(m)]
        assert matvec(F, E, col) == e
    for j in range(m):
        if deg[j] < D:
            for i in range(n):
                v = [F.mul(H[a][i], E[a][j]) for a in range(m)]
                coords = matvec(F, C, v)
                assert all(coords[k] == 0 for k in range(m) if deg[k] > deg[j] + 1)
    k = deg.index(D)
    lam = C[k]
    assert any(x != 0 for x in lam)
    for j in range(m):
        if deg[j] < D:
            assert sum_field(F, [F.mul(lam[a], E[a][j]) for a in range(m)]) == 0
    return D


def control(name, F, points, expected):
    H, B, E, C, ranks, count = construct(F, points)
    D = verify(F, H, B, E, C)
    assert ranks == expected, (name, ranks, expected)
    assert D <= len(H) - 1
    assert count <= len(H) * len(H[0])
    print(f"{name}: PASS; ranks={ranks}, minimum_degree={D}, candidates={count}")


if __name__ == "__main__":
    control("singleton over Q", Field(), [(7, -2)], [1])
    control("duplicate coordinate functions over Q", Field(), [(t, t) for t in range(4)], [1, 2, 3, 4])
    control("five explicit non-Cartesian F2 points", Field(2),
            [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)], [1, 4, 5])
    control("fifteen irrelevant coordinates over Q", Field(),
            [(0,) * 15 + (t,) for t in range(4)], [1, 2, 3, 4])
    control("non-Cartesian Q points", Field(),
            [(0, 0), (1, 0), (0, 1), (2, 2), (3, 4)], [1, 3, 5])
