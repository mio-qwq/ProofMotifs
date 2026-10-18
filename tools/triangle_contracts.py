"""Exact local tests for PM-SYNTH-B. No repository writes or dependencies."""
from itertools import permutations, product
import json


def rank_mod(matrix, p):
    a = [[v % p for v in row] for row in matrix]
    r = 0
    for c in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(v * inv) % p for v in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [(x - q * y) % p for x, y in zip(a[i], a[r])]
        r += 1
    return r


def system(p, symmetric=True, shared=True, constants=(1, 1, 1)):
    rows = []
    variables = []

    def var(name):
        if name not in variables:
            variables.append(name)
        return name

    equations = []
    for i, j, k in permutations(range(3)):
        l = ("L", j, tuple(sorted((i, k)))) if shared else ("L", j, i, k)
        b = ("B", i, tuple(sorted((j, k)))) if symmetric else ("B", i, j, k)
        equations.append(({var(l): 1, var(b): -1, var(("A", i, k)): -1}, 0))
    for (i, k), c in zip(((0, 1), (0, 2), (1, 2)), constants):
        equations.append(({var(("A", i, k)): 1, var(("A", k, i)): 1}, c))
    for eq, c in equations:
        rows.append([eq.get(v, 0) for v in variables])
    augmented = [row + [c] for row, (_, c) in zip(rows, equations)]
    return rank_mod(rows, p), rank_mod(augmented, p)


def dot(x, y, p=2):
    return sum(a*b for a, b in zip(x, y)) % p


def mv(a, x, p=2):
    return tuple(dot(row, x, p) for row in a)


def transpose(a):
    return tuple(zip(*a))


def nonsymmetric_triangle():
    # Columns of U_i specify images of the two X-basis vectors in V=F_2^3.
    U = (
        ((1, 0), (0, 1), (0, 0)),
        ((0, 1), (0, 0), (1, 0)),
        ((0, 0), (1, 0), (0, 1)),
    )
    u = ((0, 0, 1), (0, 1, 0), (1, 0, 0))
    T = ((0, 0), (1, 1))
    a = (0, 1)
    x = {(0, 1): (1, 0), (0, 2): (0, 1),
         (1, 0): (0, 1), (1, 2): (1, 0),
         (2, 0): (1, 0), (2, 1): (0, 1)}
    for i in range(3):
        assert rank_mod(U[i], 2) == 2
        assert all(dot(u[i], c) == 0 for c in transpose(U[i]))
    for i, j in permutations(range(3), 2):
        assert mv(U[i], x[i, j]) == mv(U[j], x[j, i])
        lhs = tuple(dot(u[j], c) for c in transpose(U[i]))
        rhs = tuple((a[k] + sum(x[i,j][r]*T[r][k] for r in range(2))) % 2
                    for k in range(2))
        assert lhs == rhs
        assert (dot(a, x[i, j]) + dot(a, x[j, i])) % 2 == 1
    return True


def odd_characteristic_triangle(p):
    # X=V=F_p, U_i=id, a=id, T=0, u_i=a, all witnesses=1/2.
    half = pow(2, -1, p)
    assert (half + half) % p == 1
    assert 1 == (1 + 0 * half) % p
    return True


def no_holes_with_distinct_maps():
    # X=F2^2, V=F2^4; U_i(e1)=e1 and U_i(e2)=e_(i+2).
    U = [tuple((int(r == 0), int(r == i+1)) for r in range(4)) for i in range(3)]
    a, T = (1, 1), ((1, 0), (0, 1))
    vectors = list(product(range(2), repeat=2))
    assert len(set(U)) == 3
    assert all(rank_mod(u, 2) == 2 for u in U)
    assert all(dot(x, mv(T, x)) == dot(a, x) for x in vectors)
    holes = 0
    functional_witnesses = 0
    for i, j in ((0, 1), (0, 2), (1, 2)):
        for x, y in product(vectors, repeat=2):
            fx = all((dot(a, z) + dot(x, mv(T, z))) % 2 == 0 for z in vectors)
            fy = all((dot(a, z) + dot(y, mv(T, z))) % 2 == 0 for z in vectors)
            if fx and fy:
                functional_witnesses += 1
                assert x == y == (1, 1)
            if fx and fy and mv(U[i], x) == mv(U[j], y) and (dot(a, x)+dot(a, y)) % 2 == 1:
                holes += 1
    assert functional_witnesses == 3 and holes == 0
    return {'distinct_injective_maps': 3, 'witness_pairs_tested': 48, 'holes': holes,
            'symmetric_nondegenerate_T': True, 'diagonal_identity': True}


def report():
    assert system(2) == (8, 9)
    assert system(2, symmetric=False) == (9, 9)
    assert system(2, shared=False) == (9, 9)
    assert system(2, constants=(1, 1, 0)) == (8, 8)
    for p in (3, 5, 7):
        assert system(p) == (9, 9)
        assert odd_characteristic_triangle(p)
    assert nonsymmetric_triangle()
    return {'full_scalar_ranks': {str(p): system(p) for p in (2, 3, 5, 7)},
            'without_symmetry_ranks_char2': system(2, symmetric=False),
            'without_sharing_ranks_char2': system(2, shared=False),
            'even_parity_ranks_char2': system(2, constants=(1, 1, 0)),
            'realized_nonsymmetric_triangle': True,
            'realized_odd_characteristic_triangles': [3, 5, 7],
            'no_hole_law': no_holes_with_distinct_maps(),
            'scope': 'local triangle interface and six-row grammar only'}


if __name__ == '__main__':
    print(json.dumps(report(), indent=2, sort_keys=True))
