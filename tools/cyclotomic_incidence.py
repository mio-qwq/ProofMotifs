"""Exact small-field controls for cyclotomic zero-sum line kernels.

This is a finite negative-control tool for SC-010.  It does not verify the
all-field character-sum argument.  Field arithmetic and F3 elimination reuse
the already tested project implementations.
"""
from itertools import combinations
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cancellation import Field
from incidence_rank_certificate import rank_profile


def cyclotomic_incidence(f: Field, index: int) -> dict:
    """Return exact incidence and affine-restriction dimensions for H=(K*)^index."""
    if f.p != 3 or f.degree < 2:
        raise ValueError('a characteristic-three field with q>3 is required')
    if not isinstance(index, int) or index < 2 or (f.q-1) % index:
        raise ValueError('index must be a divisor of q-1 and at least two')

    vertices = tuple(sorted({f.pow(x, index) for x in range(1, f.q)}))
    if len(vertices) != (f.q-1)//index:
        raise AssertionError('power image has the wrong subgroup size')
    vertex_set = set(vertices)
    position = {x: i for i, x in enumerate(vertices)}
    edges = []
    rows = []
    for u, v in combinations(vertices, 2):
        w = f.neg[f.add[u][v]]
        if w > v and w in vertex_set:
            edges.append((u, v, w))
            row = [0]*len(vertices)
            for x in (u, v, w):
                row[position[x]] = 1
            rows.append(row)

    incidence_rank = rank_profile(rows, len(vertices))['rank']
    affine = [[1]*len(vertices)] + [
        [(u//3**j) % 3 for u in vertices] for j in range(f.degree)
    ]
    affine_dimension = rank_profile(affine, len(vertices))['rank']
    for row in rows:
        for vector in affine:
            if sum(x*y for x, y in zip(row, vector)) % 3:
                raise AssertionError('affine restriction violates a line equation')

    nullity = len(vertices)-incidence_rank
    return dict(q=f.q, degree=f.degree, modulus=list(f.modulus), index=index,
                subgroup_size=len(vertices), edge_count=len(edges),
                incidence_rank=incidence_rank, incidence_nullity=nullity,
                affine_restriction_dimension=affine_dimension,
                affine_kernel_holds=nullity == affine_dimension,
                limitations=('finite exact control only; the SC-010 theorem uses '
                             'a multiplicative-character proof'))


def main() -> None:
    f81 = Field(3, (2, 0, 1, 0, 1))
    f243 = Field(3, (1, 2, 0, 0, 0, 1))
    cases = [(f81, 4), (f81, 5), (f81, 8), (f81, 10), (f81, 16),
             (f243, 11), (f243, 22)]
    print(json.dumps(dict(
        schema=1,
        randomized=False,
        purpose='negative controls showing the large-field hypothesis is essential',
        reports=[cyclotomic_incidence(f, d) for f, d in cases],
    ), sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
