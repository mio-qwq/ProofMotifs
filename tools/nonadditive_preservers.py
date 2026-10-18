"""Exact quotient-hypergraph checks for arbitrary ternary-order preservers.

The proof in SC-008 reduces arbitrary permutations of F_(3^m) preserving
ternary cancellation order to automorphisms of a zero-sum hypergraph on the
nonzero squares.  This module checks the F_9 and F_27 instances exactly.  It
uses no randomness and does not claim a general automorphism classification.
"""

from itertools import combinations
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cancellation import Field
from ternary_differences import invariants, predicted_order


def square_hypergraph(f: Field) -> tuple[tuple[int, ...], tuple[tuple[int, int, int], ...]]:
    """Vertices are nonzero squares; edges are distinct zero-sum triples."""
    if f.p != 3:
        raise ValueError("characteristic three required")
    vertices = tuple(sorted({f.mul[x][x] for x in range(1, f.q)}))
    edges = tuple(e for e in combinations(vertices, 3)
                  if f.add[f.add[e[0]][e[1]]][e[2]] == 0)
    return vertices, edges


def hypergraph_automorphisms(
        vertices: tuple[int, ...], edges: tuple[tuple[int, int, int], ...]
) -> set[tuple[int, ...]]:
    """Enumerate every automorphism, with safe pair-incidence pruning.

    This routine is deliberately limited to the F_9/F_27/F_81 quotients used
    in the evidence file.  A pair in this hypergraph lies in at most one edge,
    so mapping an adjacent pair forces the third vertex.  Degree and
    pair-incidence tests are necessary constraints; completed maps are still
    checked against the entire edge set.
    """
    if len(vertices) > 40:
        raise ValueError("exact backtracking is restricted to at most 40 vertices")
    edge_set = {frozenset(e) for e in edges}
    degree = {v: sum(v in e for e in edges) for v in vertices}
    third: dict[frozenset[int], int] = {}
    for e in edges:
        for a, b in combinations(e, 2):
            key = frozenset((a, b))
            if key in third:
                raise ValueError("the exact enumerator requires a linear hypergraph")
            third[key] = next(x for x in e if x not in (a, b))
    adjacent = {x: {y for y in vertices if y != x and frozenset((x, y)) in third}
                for x in vertices}
    answer: set[tuple[int, ...]] = set()

    def propagate(image: dict[int, int], inverse: dict[int, int]) -> bool:
        while True:
            additions: list[tuple[int, int]] = []
            keys = list(image)
            for i, a in enumerate(keys):
                for b in keys[i + 1:]:
                    c = third.get(frozenset((a, b)))
                    d = third.get(frozenset((image[a], image[b])))
                    if (c is None) != (d is None):
                        return False
                    if c is None:
                        continue
                    if c in image:
                        if image[c] != d:
                            return False
                    elif d in inverse:
                        return False
                    else:
                        additions.append((c, d))
            if not additions:
                return True
            for c, d in additions:
                if c in image:
                    if image[c] != d:
                        return False
                elif d in inverse:
                    return False
                else:
                    image[c] = d
                    inverse[d] = c

    def visit(image: dict[int, int], inverse: dict[int, int]) -> None:
        if not propagate(image, inverse):
            return
        if len(image) == len(vertices):
            transported = {frozenset(image[x] for x in e) for e in edges}
            if transported == edge_set:
                answer.add(tuple(image[v] for v in vertices))
            return
        best_x = None
        best_candidates = None
        for x in vertices:
            if x in image:
                continue
            candidates = [y for y in vertices if y not in inverse and degree[y] == degree[x]
                          and all((z in adjacent[x]) == (image[z] in adjacent[y])
                                  for z in image)]
            if not candidates:
                return
            if best_candidates is None or len(candidates) < len(best_candidates):
                best_x, best_candidates = x, candidates
        assert best_x is not None and best_candidates is not None
        for y in best_candidates:
            extended = dict(image)
            extended_inverse = dict(inverse)
            extended[best_x] = y
            extended_inverse[y] = best_x
            visit(extended, extended_inverse)

    visit({}, {})
    return answer


def semilinear_quotient_actions(f: Field, vertices: tuple[int, ...]) -> set[tuple[int, ...]]:
    """Actions u -> s*u^(3^j), with s a nonzero square."""
    return {tuple(f.mul[s][f.pow(x, 3 ** j)] for x in vertices)
            for s in vertices for j in range(f.degree)}


def cancellation_label(f: Field, a: int, b: int, c: int) -> str:
    value = predicted_order(*invariants(f, a, b, c))
    return "infinity" if value is None else str(value)


def sign_flip_map(f: Field, representative: int = 1) -> tuple[int, ...]:
    """Swap one opposite pair and fix every other element."""
    if representative == 0:
        raise ValueError("the representative must be nonzero")
    other = f.neg[representative]
    values = list(range(f.q))
    values[representative], values[other] = other, representative
    return tuple(values)


def field_report(f: Field) -> dict:
    vertices, edges = square_hypergraph(f)
    automorphisms = hypergraph_automorphisms(vertices, edges)
    semilinear = semilinear_quotient_actions(f, vertices)
    degrees = {x: sum(x in e for e in edges) for x in vertices}
    return {
        "q": f.q,
        "modulus": list(f.modulus),
        "quotient_vertices": list(vertices),
        "zero_sum_edges": [list(e) for e in edges],
        "edge_count": len(edges),
        "vertex_degrees": sorted(degrees.values()),
        "quotient_automorphism_count": len(automorphisms),
        "semilinear_quotient_action_count": len(semilinear),
        "all_quotient_automorphisms_are_semilinear": automorphisms == semilinear,
        "full_arbitrary_preserver_count": (2 ** len(vertices)) * len(automorphisms),
    }


def main() -> None:
    f9 = Field(3, (1, 0, 1))
    f27 = Field(3, (1, 2, 0, 1))
    f81 = Field(3, (2, 0, 1, 0, 1))
    flip = sign_flip_map(f27)
    # Complete label comparison for the explicit nonadditive example.
    compared = 0
    for a in range(27):
        for b in range(27):
            for c in range(27):
                assert cancellation_label(f27, a, b, c) == \
                       cancellation_label(f27, flip[a], flip[b], flip[c])
                compared += 1
    alpha = 3
    one_plus_alpha = f27.add[1][alpha]
    assert flip[one_plus_alpha] != f27.add[flip[1]][flip[alpha]]
    report = {
        "schema": 1,
        "randomized": False,
        "arithmetic": "exact characteristic-three finite fields",
        "fields": [field_report(f9), field_report(f27), field_report(f81)],
        "explicit_nonadditive_preserver": {
            "field": 27,
            "map": "swap 1 and -1, fix every other element",
            "ordered_triples_compared": compared,
            "additivity_failure": {
                "x": 1,
                "y": alpha,
                "T(x+y)": flip[one_plus_alpha],
                "T(x)+T(y)": f27.add[flip[1]][flip[alpha]],
            },
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
