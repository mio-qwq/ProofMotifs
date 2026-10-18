"""Exact color-refinement/orbit certificate for the F_243 square hypergraph.

The builder uses project finite-field arithmetic.  The verifier reconstructs
the same field by a separate alpha recurrence and cyclic-log arithmetic; its
verification path imports no other project module.  No backtracking is used.
"""

from collections import Counter
from itertools import combinations
from pathlib import Path
import argparse
import hashlib
import json
import sys


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _incidence(vertices, edges):
    vertices = tuple(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    _require(len(index) == len(vertices), "vertices must be distinct")
    incident = [[] for _ in vertices]
    seen = set()
    for edge in edges:
        key = frozenset(edge)
        _require(len(edge) == 3 and len(key) == 3, "edges must have three distinct vertices")
        _require(key not in seen, "duplicate edge")
        _require(key.issubset(index), "edge outside vertex set")
        seen.add(key)
        for x in edge:
            incident[index[x]].append(tuple(index[y] for y in edge if y != x))
    return index, incident


def refinement_trace(vertices, edges, fixed_vertices):
    """Canonical, equivariant refinement of a finite 3-uniform hypergraph.

    Signatures retain the old color and the multiset of unordered color pairs
    on the other endpoints of incident edges.  Pair uniqueness is not assumed.
    Each listed fixed vertex receives its own initial color, in listed order.
    """
    vertices, fixed_vertices = tuple(vertices), tuple(fixed_vertices)
    index, incident = _incidence(vertices, edges)
    _require(len(set(fixed_vertices)) == len(fixed_vertices), "duplicate fixed vertex")
    _require(set(fixed_vertices).issubset(index), "fixed vertex outside vertex set")
    colors = [0] * len(vertices)
    for color, x in enumerate(fixed_vertices, 1):
        colors[index[x]] = color
    trace = [colors]
    for _ in range(len(vertices) + 1):
        signatures = [
            (colors[x], tuple(sorted(tuple(sorted((colors[a], colors[b])))
                                     for a, b in incident[x])))
            for x in range(len(vertices))
        ]
        lookup = {signature: i for i, signature in enumerate(sorted(set(signatures)))}
        new = [lookup[signature] for signature in signatures]
        trace.append(new)
        if len(set(new)) == len(set(colors)):
            return {
                "fixed_vertices": list(fixed_vertices),
                "trace": trace,
                "cell_sizes": sorted(Counter(new).values()),
                "cell_counts": [len(set(c)) for c in trace],
            }
        colors = new
    raise RuntimeError("refinement did not stabilize")


def build_certificate():
    """Build deterministic full edge/color traces using project arithmetic."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from cancellation import Field
    from nonadditive_preservers import square_hypergraph

    f = Field(3, (1, 2, 0, 0, 0, 1))
    vertices, edges = square_hypergraph(f)
    root = refinement_trace(vertices, edges, (1,))
    pair = refinement_trace(vertices, edges, (1, 9))
    index = {v: i for i, v in enumerate(vertices)}
    color = root["trace"][-1][index[9]]
    cell = [v for i, v in enumerate(vertices) if root["trace"][-1][i] == color]
    generator = next(s for s in vertices if f.pow(s, 11) != 1)
    return {
        "schema": 1,
        "field_order": 243,
        "field_modulus": list(f.modulus),
        "vertices": list(vertices),
        "edges": [list(edge) for edge in edges],
        "root_refinement": root,
        "pair_refinement": pair,
        "second_vertex": 9,
        "root_second_vertex_cell": cell,
        "known_generators": {
            "square_scaling_element": generator,
            "scaling_permutation": [f.mul[generator][v] for v in vertices],
            "frobenius_permutation": [f.pow(v, 3) for v in vertices],
        },
        "upper_bound_factors": [121, 5, 1],
        "automorphism_count": 605,
    }


def _independent_arithmetic():
    """Field arithmetic from alpha^5=alpha+2, without polynomial division.

    Multiplication by alpha cycles through all 242 nonzero coordinate vectors.
    Consequently every nonzero vector is a power with an inverse; the quotient
    is a field.  General multiplication uses logarithms, not project tables.
    """
    def times_alpha(x):
        c = [(x // (3 ** i)) % 3 for i in range(5)]
        d = [2 * c[4] % 3, (c[0] + c[4]) % 3, c[1], c[2], c[3]]
        return sum(v * (3 ** i) for i, v in enumerate(d))

    exp, log, x = [], {}, 1
    for k in range(242):
        _require(x not in log, "alpha recurrence closed too early")
        exp.append(x)
        log[x] = k
        x = times_alpha(x)
    _require(x == 1 and set(exp) == set(range(1, 243)), "invalid alpha cycle")

    def mul(x, y):
        return exp[(log[x] + log[y]) % 242] if x and y else 0

    def add(x, y):
        return sum((((x // (3 ** i)) + (y // (3 ** i))) % 3) * (3 ** i)
                   for i in range(5))

    def neg(x):
        return sum((-(x // (3 ** i)) % 3) * (3 ** i) for i in range(5))

    def power(x, k):
        return exp[(log[x] * k) % 242] if x else int(k == 0)

    return exp, mul, add, neg, power


def _verify_trace(record, expected_fixed, vertices, index, incident):
    """Check every color-transition by independent signature equivalence."""
    _require(record["fixed_vertices"] == list(expected_fixed), "incorrect fixed vertices")
    trace = record["trace"]
    _require(2 <= len(trace) <= len(vertices) + 2, "invalid trace length")
    _require(all(len(c) == len(vertices) for c in trace), "invalid color-vector length")
    initial = [0] * len(vertices)
    for color, x in enumerate(expected_fixed, 1):
        initial[index[x]] = color
    _require(trace[0] == initial, "incorrect initial coloring")
    for old, new in zip(trace, trace[1:]):
        by_signature, by_color = {}, {}
        for i in range(len(vertices)):
            pairs = Counter(tuple(sorted((old[a], old[b]))) for a, b in incident[i])
            signature = (old[i], tuple(sorted(pairs.items())))
            _require(signature not in by_signature or by_signature[signature] == new[i],
                     "refinement splits equal signatures")
            _require(new[i] not in by_color or by_color[new[i]] == signature,
                     "refinement merges different signatures")
            by_signature[signature] = new[i]
            by_color[new[i]] = signature
    counts = [len(set(c)) for c in trace]
    _require(counts[-1] == counts[-2], "trace does not reach stability")
    _require(record["cell_sizes"] == sorted(Counter(trace[-1]).values()), "cell-size mismatch")
    _require(record["cell_counts"] == counts, "cell-count trace mismatch")
    return counts


def verify_certificate(certificate):
    """Verify field, all edges, both traces and all 605 known actions.

    This path uses only standard-library code defined in this module.  It does
    not call the builder, the project Field class or refinement_trace.
    """
    _require(certificate["schema"] == 1, "unknown certificate schema")
    _require(certificate["field_order"] == 243, "wrong field order")
    _require(certificate["field_modulus"] == [1, 2, 0, 0, 0, 1], "wrong field modulus")
    exp, mul, add, neg, power = _independent_arithmetic()
    vertices = tuple(sorted(exp[::2]))
    squares = set(vertices)
    edges = []
    for a, b in combinations(vertices, 2):
        c = neg(add(a, b))
        if c in squares and b < c:
            edges.append((a, b, c))
    _require(certificate["vertices"] == list(vertices), "square vertex set mismatch")
    claimed_edges = [tuple(e) for e in certificate["edges"]]
    _require(sorted(claimed_edges) == sorted(edges), "square zero-sum edge set mismatch")
    _require(len(vertices) == 121 and len(edges) == 1210, "wrong hypergraph parameters")
    index, incident = _incidence(vertices, edges)
    _require(set(map(len, incident)) == {30}, "wrong vertex degrees")
    root_counts = _verify_trace(certificate["root_refinement"], (1,), vertices, index, incident)
    pair_counts = _verify_trace(certificate["pair_refinement"], (1, 9), vertices, index, incident)
    _require(certificate["second_vertex"] == 9, "wrong second pivot")
    colors = certificate["root_refinement"]["trace"][-1]
    cell = [v for i, v in enumerate(vertices) if colors[i] == colors[index[9]]]
    _require(cell == certificate["root_second_vertex_cell"] and len(cell) == 5,
             "incorrect root-stabilizer cell")
    _require(len(set(certificate["pair_refinement"]["trace"][-1])) == 121,
             "two-point refinement is not discrete")
    generators = certificate["known_generators"]
    g = generators["square_scaling_element"]
    _require(g in squares and len({power(g, k) for k in range(121)}) == 121,
             "scaling generator does not have order 121")
    _require(generators["scaling_permutation"] == [mul(g, v) for v in vertices],
             "scaling permutation mismatch")
    _require(generators["frobenius_permutation"] == [power(v, 3) for v in vertices],
             "Frobenius permutation mismatch")
    edge_set = {frozenset(e) for e in edges}
    known = set()
    for s in vertices:
        for j in range(5):
            permutation = tuple(mul(s, power(v, 3 ** j)) for v in vertices)
            _require(len(set(permutation)) == 121, "non-bijective known action")
            action = dict(zip(vertices, permutation))
            transported = {frozenset(action[x] for x in e) for e in edges}
            _require(transported == edge_set, "known action fails edge preservation")
            known.add(permutation)
    _require(len(known) == 605, "wrong number of distinct known actions")
    _require(certificate["upper_bound_factors"] == [121, 5, 1], "incorrect upper-bound factors")
    _require(certificate["automorphism_count"] == 605, "incorrect stated group order")
    canonical = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
    return {
        "arithmetic": "independent alpha recurrence and cyclic-log multiplication",
        "alpha_multiplicative_order": 242,
        "quotient_vertices": 121,
        "zero_sum_edges": 1210,
        "vertex_degree": 30,
        "pivot_vertices": [1, 9],
        "root_refinement_cell_counts": root_counts,
        "pair_refinement_cell_counts": pair_counts,
        "root_second_vertex_cell": cell,
        "two_point_stabilizer_upper_bound": 1,
        "point_stabilizer_upper_bound": 5,
        "automorphism_upper_bound": 605,
        "known_semilinear_actions_checked": len(known),
        "exact_automorphism_count": 605,
        "all_automorphisms_are_semilinear": True,
        "canonical_certificate_sha256": hashlib.sha256(canonical).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="verify a saved certificate or complete report")
    args = parser.parse_args()
    if args.check is not None:
        value = json.loads(args.check.read_text())
        certificate = value.get("certificate", value)
        verification = verify_certificate(certificate)
        if "verification" in value:
            _require(value["verification"] == verification, "saved verification receipt mismatch")
        print(json.dumps(verification, indent=2, sort_keys=True))
        return
    certificate = build_certificate()
    report = {"schema": 1, "method": "equivariant color refinement and orbit-stabilizer",
              "certificate": certificate, "verification": verify_certificate(certificate)}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
