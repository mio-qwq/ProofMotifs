"""Exact F3 incidence-rank certificates for the square zero-sum hypergraph.

No automorphisms are enumerated. A nonzero minor supplies a lower rank bound;
independent affine kernel vectors supply the matching upper bound. Field
arithmetic shares the existing validated small-field implementation. All
matrix calculations below are exact prime-field operations, without floats.
"""
from itertools import combinations
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cancellation import Field


def rank_profile(rows: list[list[int]], width: int) -> dict:
    """Eliminate over F3 and retain original row labels and pivot columns."""
    if any(len(row) != width or any(x not in (0, 1, 2) for x in row)
           for row in rows):
        raise ValueError('a rectangular F3 matrix is required')
    matrix = [list(row) for row in rows]
    labels = list(range(len(matrix)))
    pivot_rows, pivot_columns = [], []
    rank = 0
    for column in range(width):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        labels[rank], labels[pivot] = labels[pivot], labels[rank]
        pivot_rows.append(labels[rank])
        pivot_columns.append(column)
        if matrix[rank][column] == 2:
            matrix[rank] = [(2*x) % 3 for x in matrix[rank]]
        for i in range(rank+1, len(matrix)):
            factor = matrix[i][column]
            if factor:
                matrix[i] = [(x-factor*y) % 3
                             for x, y in zip(matrix[i], matrix[rank])]
        rank += 1
        if rank == len(matrix):
            break
    if any(any(row) for row in matrix[rank:]):
        raise AssertionError('nonzero row remains after the reported rank')
    return dict(rank=rank, pivot_rows=pivot_rows, pivot_columns=pivot_columns,
                zero_tail_rows=len(matrix)-rank)


def determinant3(square: list[list[int]]) -> int:
    """Exact determinant by column elimination, separate from rank_profile."""
    n = len(square)
    if any(len(row) != n for row in square):
        raise ValueError('a square matrix is required')
    matrix = [[x % 3 for x in row] for row in square]
    determinant = 1
    for k in range(n):
        pivot = next((j for j in range(k, n) if matrix[k][j]), None)
        if pivot is None:
            return 0
        if pivot != k:
            for row in matrix:
                row[k], row[pivot] = row[pivot], row[k]
            determinant = (-determinant) % 3
        value = matrix[k][k]
        determinant = determinant * value % 3
        inverse = value  # Both nonzero F3 elements are their own inverses.
        for j in range(k+1, n):
            factor = matrix[k][j] * inverse % 3
            if factor:
                for i in range(k, n):
                    matrix[i][j] = (matrix[i][j]-factor*matrix[i][k]) % 3
    return determinant


def square_incidence(f: Field) -> tuple[tuple[int, ...], tuple[tuple[int, int, int], ...], list[list[int]]]:
    """Build each edge by pair completion rather than enumerating triples."""
    if f.p != 3 or f.degree < 2:
        raise ValueError('a characteristic-three field with q>3 is required')
    vertices = tuple(sorted({f.mul[x][x] for x in range(1, f.q)}))
    vertex_set = set(vertices)
    edges = []
    for u, v in combinations(vertices, 2):
        w = f.neg[f.add[u][v]]
        if w > v and w in vertex_set:
            edges.append((u, v, w))
    index = {u: i for i, u in enumerate(vertices)}
    rows = []
    for edge in edges:
        row = [0]*len(vertices)
        for u in edge:
            row[index[u]] = 1
        rows.append(row)
    return vertices, tuple(edges), rows


def rank_certificate(f: Field) -> dict:
    vertices, edges, rows = square_incidence(f)
    n = len(vertices)
    profile = rank_profile(rows, n)
    lower_minor = [[rows[i][j] for j in profile['pivot_columns']]
                   for i in profile['pivot_rows']]
    lower_determinant = determinant3(lower_minor)
    if not lower_determinant:
        raise AssertionError('selected rank minor is singular')
    affine = [[1]*n] + [[(u//3**j) % 3 for u in vertices]
                       for j in range(f.degree)]
    affine_profile = rank_profile(affine, n)
    affine_minor = [[row[j] for j in affine_profile['pivot_columns']]
                    for row in affine]
    affine_determinant = determinant3(affine_minor)
    annihilation_checks = 0
    for row in rows:
        for vector in affine:
            if sum(x*y for x, y in zip(row, vector)) % 3:
                raise AssertionError('an affine restriction is not in the incidence kernel')
            annihilation_checks += 1
    if affine_profile['rank'] != f.degree+1 or not affine_determinant:
        raise AssertionError('affine restrictions are not independent')
    nullity = n-profile['rank']
    if nullity < f.degree+1:
        raise AssertionError('rank contradicts the explicit affine kernel')
    return dict(q=f.q, degree=f.degree, modulus=list(f.modulus),
                vertex_count=n, edge_count=len(edges), vertices=list(vertices),
                incidence_rank=profile['rank'], incidence_nullity=nullity,
                pivot_edge_indices=profile['pivot_rows'],
                pivot_vertex_indices=profile['pivot_columns'],
                rank_minor_determinant_mod3=lower_determinant,
                zero_tail_rows=profile['zero_tail_rows'],
                affine_kernel_basis=affine,
                affine_basis_dimension=affine_profile['rank'],
                affine_basis_pivot_vertex_indices=affine_profile['pivot_columns'],
                affine_basis_minor_determinant_mod3=affine_determinant,
                exact_kernel_annihilation_checks=annihilation_checks,
                rank_condition_holds=nullity == f.degree+1,
                classification_scope=('conditional affine-extension criterion applies'
                                      if nullity == f.degree+1 else
                                      'criterion fails; no classification follows'),
                arithmetic='exact F3 elimination and column-elimination determinants',
                limitations='shared finite-field arithmetic; no Lean or novelty certification')


def main() -> None:
    fields = [Field(3, (1, 0, 1)), Field(3, (1, 2, 0, 1)),
              Field(3, (2, 0, 1, 0, 1)), Field(3, (1, 2, 0, 0, 0, 1))]
    print(json.dumps(dict(schema=1, randomized=False,
                          method='incidence-rank lower minor plus explicit affine kernel',
                          reports=[rank_certificate(f) for f in fields]),
                     sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
