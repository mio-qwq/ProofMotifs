#!/usr/bin/env python3
"""Independent PM-IMPLICIT-C frontier algorithm and bounded regressions."""
from fractions import Fraction
from itertools import combinations, product


class Field:
    def __init__(self, p=0):
        self.p = p
    def x(self, a):
        return a % self.p if self.p else Fraction(a)
    def add(self, a, b):
        return self.x(a+b)
    def mul(self, a, b):
        return self.x(a*b)
    def inv(self, a):
        assert a
        return pow(a, -1, self.p) if self.p else 1/a


def reducer_add(rows, v, F):
    r = list(v)
    for pivot, row in rows:
        a = r[pivot]
        r = [F.add(x, -F.mul(a, y)) for x, y in zip(r, row)]
    pivot = next((i for i, a in enumerate(r) if a), None)
    if pivot is None:
        return False
    a = F.inv(r[pivot])
    rows.append((pivot, [F.mul(a, x) for x in r]))
    return True


def rank(vectors, F):
    rows = []
    for v in vectors:
        reducer_add(rows, v, F)
    return len(rows)


def eval_monomial(a, H, F):
    def at(h):
        value = F.x(1)
        for x, d in zip(h, a):
            for _ in range(d):
                value = F.mul(value, x)
        return value
    return [at(h) for h in H]


def discover(H, F):
    assert H and len(set(H)) == len(H)
    m, n = len(H), len(H[0])
    assert n and all(len(h) == n for h in H)
    one = ((0,)*n, [F.x(1)]*m)
    basis, frontier, rows, history = [one], [one], [], [(0, 1)]
    assert reducer_add(rows, one[1], F)
    candidates, degree = 0, 0
    while len(basis) < m:
        degree += 1
        new_frontier = []
        for a, v in frontier:
            for j in range(n):
                exponent = list(a)
                exponent[j] += 1
                w = [F.mul(h[j], x) for h, x in zip(H, v)]
                candidates += 1
                if reducer_add(rows, w, F):
                    item = tuple(exponent), w
                    basis.append(item)
                    new_frontier.append(item)
        assert new_frontier or len(basis) == m, "genuine deficient plateau"
        frontier = new_frontier
        history.append((degree, len(basis)))
    assert candidates <= n*m
    assert degree <= m-1
    return basis, history, candidates


def all_monomials(n, degree):
    # Exhaustive enumeration is used ONLY in the independent tiny-case oracle.
    return [a for a in product(range(degree+1), repeat=n) if sum(a) <= degree]


def check_case(H, p=0):
    F = Field(p)
    H = tuple(tuple(F.x(x) for x in h) for h in H)
    basis, history, _ = discover(H, F)
    n, m = len(H[0]), len(H)
    for degree, found in history:
        vectors = [eval_monomial(a, H, F) for a in all_monomials(n, degree)]
        assert rank(vectors, F) == found
    assert rank([v for _, v in basis], F) == m
    return history[-1][0]


def adversarial_controls():
    F = Field()
    H = ((0, 0), (0, 1))
    assert rank([[1, 1], [0, 0]], F) == 1  # x rejected, but not closure.
    assert check_case(H) == 1
    H = ((0,), (1,), (2,))
    bad = [eval_monomial((d,), H, F) for d in (0, 2, 3)]
    assert rank(bad, F) == 3
    assert check_case(H) == 2  # Arbitrary acceptance order loses degree optimality.
    cube = tuple(product(range(2), repeat=2))
    assert check_case(cube, 2) == 2
    for coefficients in product(range(2), repeat=2):
        image = {sum(x*a for x, a in zip(h, coefficients)) % 2 for h in cube}
        assert len(image) <= 2  # No injective linear form on F_2^2.
    H = ((0, 0), (1, 1), (2, 2), (3, 3), (0, 1))
    basis = [eval_monomial(a, H, F) for a in ((0,0), (1,0), (0,1), (1,1))]
    assert rank(basis, F) == 4
    assert eval_monomial((2,0), H, F) == basis[3]
    assert eval_monomial((0,2), H, F) == [u-x+y for u,x,y in zip(basis[3],basis[1],basis[2])]
    assert rank(basis + [eval_monomial((2,1), H, F)], F) == 5
    assert check_case(H) == 3
    # Rejecting both squares after accepting xy, then pruning all their
    # multiples, leaves only {1,x,y,xy}; that unsupported pruning is invalid.
    print("PASS premature-rejection, degree-order, finite-field-separator, and non-ideal-pruning controls")


if __name__ == '__main__':
    adversarial_controls()
    cases = 0
    points = tuple(product(range(2), repeat=3))
    for m in range(1, len(points)+1):
        for H in combinations(points, m):
            check_case(H, 2)
            cases += 1
    assert cases == 255
    assert check_case(tuple(product(range(3), repeat=2)), 3) == 4
    assert check_case(tuple((j,) for j in range(7))) == 6
    assert check_case(((0, 0), (1, 0), (2, 0), (0, 1))) == 2
    print("PASS all 255 nonempty subsets of F_2^3 against exhaustive small-degree oracle")
    print("PASS F_3^2, seven rational collinear points, and mixed hole geometry")
    print("The production algorithm generated only coordinate-products of retained frontier vectors.")
