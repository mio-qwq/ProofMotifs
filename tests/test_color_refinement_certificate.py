"""Independent certificate replay, adversarial controls and equivariance."""

from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from cancellation import Field
from nonadditive_preservers import square_hypergraph
from color_refinement_certificate import build_certificate, refinement_trace, verify_certificate


class ColorCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = build_certificate()

    def test_independent_arithmetic_and_sharp_group_certificate(self):
        result = verify_certificate(self.certificate)
        self.assertEqual(result["exact_automorphism_count"], 605)
        self.assertEqual(result["known_semilinear_actions_checked"], 605)
        self.assertEqual(result["root_refinement_cell_counts"], [2, 3, 15, 25, 25])
        self.assertEqual(result["pair_refinement_cell_counts"], [3, 6, 121, 121])
        self.assertEqual(result["root_second_vertex_cell"], [9, 15, 69, 148, 239])

    def test_omitted_field_edge_is_rejected(self):
        bad = deepcopy(self.certificate)
        bad["edges"].pop()
        with self.assertRaisesRegex(ValueError, "edge set mismatch"):
            verify_certificate(bad)

    def test_unsafe_refinement_split_is_rejected(self):
        bad = deepcopy(self.certificate)
        colors = bad["root_refinement"]["trace"][1]
        repeated = next(c for c in colors if colors.count(c) > 1)
        colors[colors.index(repeated)] = max(colors) + 1
        with self.assertRaisesRegex(ValueError, "splits equal signatures"):
            verify_certificate(bad)

    def test_changed_frobenius_action_is_rejected(self):
        bad = deepcopy(self.certificate)
        permutation = bad["known_generators"]["frobenius_permutation"]
        permutation[0], permutation[1] = permutation[1], permutation[0]
        with self.assertRaisesRegex(ValueError, "Frobenius permutation mismatch"):
            verify_certificate(bad)

    def test_refinement_is_equivariant_under_relabeling(self):
        f = Field(3, (1, 2, 0, 1))
        vertices, edges = square_hypergraph(f)
        relabel = {v: vertices[(5 * i + 1) % len(vertices)] for i, v in enumerate(vertices)}
        fixed = (1, 9)
        original = refinement_trace(vertices, edges, fixed)
        renamed_edges = [tuple(relabel[x] for x in e) for e in edges]
        renamed = refinement_trace(vertices, renamed_edges, tuple(relabel[x] for x in fixed))
        index = {v: i for i, v in enumerate(vertices)}
        self.assertEqual(len(original["trace"]), len(renamed["trace"]))
        for old, new in zip(original["trace"], renamed["trace"]):
            for i, v in enumerate(vertices):
                self.assertEqual(old[i], new[index[relabel[v]]])

    def test_empty_f9_graph_does_not_give_false_discreteness(self):
        f = Field(3, (1, 0, 1))
        vertices, edges = square_hypergraph(f)
        self.assertEqual(edges, ())
        root = refinement_trace(vertices, edges, (1,))
        pair = refinement_trace(vertices, edges, (1, vertices[1]))
        self.assertEqual(root["cell_sizes"], [1, 3])
        self.assertEqual(pair["cell_sizes"], [1, 1, 2])
        self.assertLess(pair["cell_counts"][-1], len(vertices))


if __name__ == "__main__":
    unittest.main()
