"""PM-IMPLICIT-B exact independent closure/cardinal controls."""
from fractions import Fraction
from itertools import product
from math import comb


class Field:
    def __init__(self, p=None):
        self.p = p

    def k(self, a):
        return Fraction(a) if self.p is None else a % self.p

    def add(self, a, b):
        return self.k(a + b)

    def sub(self, a, b):
        return self.k(a - b)

    def mul(self, a, b):
        return self.k(a * b)

    def div(self, a, b):
        assert b
        return a / b if self.p is None else a * pow(b, -1, self.p) % self.p

    def dot(self, a, b):
        result = self.k(0)
        for x, y in zip(a, b):
            result = self.add(result, self.mul(x, y))
        return result


def inverse(matrix, f):
    m = len(matrix)
    a = [row[:] + [f.k(i == j) for j in range(m)]
         for i, row in enumerate(matrix)]
    for j in range(m):
        pivot = next(i for i in range(j, m) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        scalar = a[j][j]
        a[j] = [f.div(x, scalar) for x in a[j]]
        for i in range(m):
            if i != j:
                scalar = a[i][j]
                a[i] = [f.sub(x, f.mul(scalar, y))
                        for x, y in zip(a[i], a[j])]
    return [row[m:] for row in a]


def retain(v, echelon, f):
    v = v[:]
    for pivot, row in echelon:
        scalar = v[pivot]
        v = [f.sub(x, f.mul(scalar, y)) for x, y in zip(v, row)]
    pivot = next((i for i, x in enumerate(v) if x), None)
    if pivot is None:
        return False
    scalar = v[pivot]
    echelon.append((pivot, [f.div(x, scalar) for x in v]))
    return True


def closure(points, f):
    m, n = len(points), len(points[0])
    assert m >= 1 and n >= 1
    assert len(set(tuple(p) for p in points)) == m
    values = [[f.k(1)] * m]
    exponents = [(0,) * n]
    degrees = [0]
    echelon = []
    assert retain(values[0], echelon, f)
    ranks, offers, frontier = [1], 0, [0]
    while len(values) < m:
        following = []
        degree = len(ranks)
        for parent in frontier:
            for coordinate in range(n):
                offers += 1
                v = [f.mul(values[parent][h], points[h][coordinate])
                     for h in range(m)]
                if retain(v, echelon, f):
                    e = list(exponents[parent])
                    e[coordinate] += 1
                    following.append(len(values))
                    values.append(v)
                    exponents.append(tuple(e))
                    degrees.append(degree)
                    if len(values) == m:
                        break
            if len(values) == m:
                break
        ranks.append(len(values))
        assert following, "proper plateau contradicts distinct-point input"
        frontier = following
    evaluation = [list(row) for row in zip(*values)]
    c = inverse(evaluation, f)
    cardinal_degrees = [max(degrees[k] for k in range(m) if c[k][j])
                        for j in range(m)]
    assert offers <= n * m
    for i in range(m):
        for j in range(m):
            assert f.dot(evaluation[i], [c[k][j] for k in range(m)]) == f.k(i == j)
    # Every coordinate product has coordinates supported in the correct
    # filtered level: this is the finite degree-safe transition certificate.
    for k in range(m):
        for coordinate in range(n):
            v = [f.mul(values[k][h], points[h][coordinate]) for h in range(m)]
            for j in range(m):
                if degrees[j] > degrees[k] + 1:
                    assert f.dot(c[j], v) == 0
    return {"values": values, "exponents": exponents, "degrees": degrees,
            "ranks": ranks, "offers": offers, "inverse": c,
            "cardinal_degrees": cardinal_degrees}


def exponents_exact(n, total):
    if n == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in exponents_exact(n - 1, total - first):
                yield (first,) + rest


def monomial_values(points, e, f):
    result = []
    for point in points:
        value = f.k(1)
        for a, power in zip(point, e):
            value = f.mul(value, a ** power)
        result.append(value)
    return result


def brute_control(points, f, result):
    echelon = []
    for degree, expected in enumerate(result["ranks"]):
        for e in exponents_exact(len(points[0]), degree):
            retain(monomial_values(points, e, f), echelon, f)
        assert len(echelon) == expected
    c, degrees = result["inverse"], result["degrees"]
    # Individual-degree lower certificates: a selected inverse row separates
    # e_j while annihilating every lower-degree monomial, checked here by
    # independent ambient enumeration only on these small control panels.
    for j, delta in enumerate(result["cardinal_degrees"]):
        k = next(k for k, d in enumerate(degrees) if d == delta and c[k][j])
        assert c[k][j]
        for degree in range(delta):
            for e in exponents_exact(len(points[0]), degree):
                assert f.dot(c[k], monomial_values(points, e, f)) == 0


q = Field()
panels = [
    ([(Fraction(3), Fraction(-2))], [1], [0]),
    ([(Fraction(i), Fraction(0)) for i in range(5)], [1, 2, 3, 4, 5], [4] * 5),
    ([(Fraction(x), Fraction(y)) for x, y in product(range(2), repeat=2)],
     [1, 3, 4], [2] * 4),
    ([(Fraction(0), Fraction(0)), (Fraction(1), Fraction(0)),
      (Fraction(2), Fraction(0)), (Fraction(0), Fraction(1))],
     [1, 3, 4], [2, 2, 2, 1]),
]
for points, ranks, degrees in panels:
    result = closure(points, q)
    assert result["ranks"] == ranks
    assert result["cardinal_degrees"] == degrees
    brute_control(points, q, result)

f2 = Field(2)
cube = [tuple(p) for p in product(range(2), repeat=3)]
cube_result = closure(cube, f2)
assert cube_result["ranks"] == [1, 4, 7, 8]
assert cube_result["cardinal_degrees"] == [3] * 8
brute_control(cube, f2, cube_result)

# Source197 square-Gram positive/negative same-budget controls in F7.
f7 = Field(7)
hplus = [(0, 0), (1, 0), (2, 0), (0, 1)]
hminus = [(0, 0), (1, 0), (2, 0), (3, 0)]
good, bad = closure(hplus, f7), closure(hminus, f7)
assert good["ranks"] == [1, 3, 4]
assert bad["ranks"] == [1, 2, 3, 4]
brute_control(hplus, f7, good)
brute_control(hminus, f7, bad)
lam = bad["inverse"][-1]
assert lam == [1, 4, 3, 6]
assert [f7.dot(lam, monomial_values(hminus, (k, 0), f7))
        for k in range(4)] == [0, 0, 0, 1]


def cardinal_values(point):
    row = [monomial_values([point], e, f7)[0] for e in good["exponents"]]
    return [f7.dot(row, [good["inverse"][k][j] for k in range(4)])
            for j in range(4)]


plane = list(product(range(7), repeat=2))
gram = [[0] * 4 for _ in range(4)]
for point in plane:
    if point not in hplus:
        v = cardinal_values(point)
        for i in range(4):
            for j in range(4):
                gram[i][j] = (gram[i][j] + v[i] * v[j]) % 7
assert gram == [[(-int(i == j)) % 7 for j in range(4)] for i in range(4)]
lines = set()
for direction in [(1, a) for a in range(7)] + [(0, 1)]:
    for point in plane:
        lines.add(frozenset(((point[0] + t * direction[0]) % 7,
                             (point[1] + t * direction[1]) % 7)
                            for t in range(7)))
assert len(lines) == 56
for line in lines:
    gram = [[0] * 4 for _ in range(4)]
    for point in line:
        v = cardinal_values(point)
        for i in range(4):
            for j in range(4):
                gram[i][j] = (gram[i][j] + v[i] * v[j]) % 7
    assert not any(x for row in gram for x in row)

# Large ambient dictionary is not enumerated for this input.
wide = [tuple(Fraction(t) for _ in range(40)) for t in range(9)]
wide_result = closure(wide, q)
assert wide_result["ranks"] == list(range(1, 10))
assert wide_result["offers"] == 281
ambient = comb(48, 8)

# Input-contract control: duplicates are rejected before closure.
try:
    closure([(0,), (0,)], f7)
    raise RuntimeError("duplicate input was accepted")
except AssertionError:
    pass

print("PASS: seven small rational/prime-field filtered-rank and dual-certificate panels")
print("PASS: individual cardinal degrees [2,2,2,1] on off-line 4-point panel")
print("PASS: F7 generated degree-2 cardinal map, punctured Gram -I4, all 56 line Grams zero")
print("PASS: F7 collinear same-budget obstruction lambda=[1,4,3,6], moments=[0,0,0,1]")
print(f"PASS: n=40,m=9,d*=8; offers=281; ambient monomials={ambient}; not enumerated")
print("PASS: duplicate-input rejection")
