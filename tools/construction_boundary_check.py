"""Independent exact boundary checks for PM-SYNTH-C; standard library only."""
from itertools import product
import json


def dot(x, y, p=2):
    return sum(a * b for a, b in zip(x, y)) % p


def matvec(a, x, p=2):
    return tuple(dot(row, x, p) for row in a)


def triangle_without_symmetry():
    # Columns are the edge basis e12,e23,e31 assigned to each vertex's
    # outgoing and incoming witnesses. All maps have independent columns.
    U = [((1, 0), (0, 0), (0, 1)),
         ((0, 1), (1, 0), (0, 0)),
         ((0, 0), (0, 1), (1, 0))]
    u = [(1, 1, 0), (0, 1, 1), (1, 0, 1)]
    a = (0, 1)
    T = ((0, 0), (1, 0))
    outgoing, incoming = (1, 0), (0, 1)
    checked = 0
    for i, j in [(0, 1), (1, 2), (2, 0)]:
        xi, xj = outgoing, incoming
        assert matvec(U[i], xi) == matvec(U[j], xj)
        assert (dot(a, xi) + dot(a, xj)) % 2 == 1
        for z in product(range(2), repeat=2):
            assert dot(u[j], matvec(U[i], z)) == (
                dot(a, z) + dot(xi, matvec(T, z))) % 2
            assert dot(u[i], matvec(U[j], z)) == (
                dot(a, z) + dot(xj, matvec(T, z))) % 2
            checked += 2
    return checked


def unary_trade():
    off = [(1, 2, 3, 1), (2, 1, 1, 3)]
    target = [(1, 1, 3, 3), (2, 2, 1, 1)]
    for s in off + target:
        g, h, u, v = s
        assert u - v + 2 * (g - h) == 0
    for coordinate in range(4):
        assert sorted(s[coordinate] for s in off) == sorted(
            s[coordinate] for s in target)


def cross_pair_classification():
    off = [(1, 2, 3, 1), (2, 1, 1, 3)]
    matchings = [([(0, 2), (1, 3)], [(1, 1, 3, 3), (2, 2, 1, 1)]),
                 ([(0, 3), (1, 2)], [(1, 1, 1, 1), (2, 2, 3, 3)])]
    for pairs, target in matchings:
        for pair in pairs:
            assert sorted(tuple(s[i] for i in pair) for s in off) == sorted(
                tuple(s[i] for i in pair) for s in target)
    checked = 0
    for M in range(3, 7):
        for g, h, u, v in product(range(1, M + 1), repeat=4):
            if u - v + 2 * (g - h):
                continue
            weights = [g*g-h*h+h*u-h*v,
                       h*h-g*g-g*u+g*v,
                       v*v-u*u-4*u*g+4*u*h,
                       u*u-v*v+4*v*g-4*v*h]
            assert weights[:2] == [(g-h)**2, (g-h)**2]
            assert weights[2:] == [(u-v)**2, (u-v)**2]
            for weight in weights:
                assert weight >= 0
                assert (weight == 0) == (g == h and u == v)
            checked += 1
    return checked


def finite_characteristic_failures():
    # In characteristic three, identical copies form a hole triangle even
    # with symmetric T=0: a=u_i=id, U_i=id, all edge witnesses equal 2.
    assert (2 + 2) % 3 == 1
    # Full Fourier selector fails without a primitive root: zeta=1 makes
    # every average 1. This branch is non-target but has weight zero.
    g, h, u, v = 2, 1, 1, 4
    assert g * g - h * h + h * (u - v) == 0
    assert u - v + 2 * (g - h) == -1
    # Primitive period 5 alone does not replace the label bound M=1.
    g, h, u, v = 10, 5, 1, 16
    assert g * g - h * h + h * (u - v) == 0
    assert u - v + 2 * (g - h) == -5


if __name__ == "__main__":
    unary_trade()
    star_count = cross_pair_classification()
    count = triangle_without_symmetry()
    finite_characteristic_failures()
    print(json.dumps({"unary_balanced_trade": "verified", "nonsymmetric_triangle_functional_checks": count,
           "cross_pair_star_support_checks": star_count,
           "characteristic_three_triangle": "verified", "damaged_fourier_branches": "verified"},
          indent=2, sort_keys=True))
