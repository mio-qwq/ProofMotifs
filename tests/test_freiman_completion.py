import unittest
from itertools import product

from tools.cancellation import Field
from tools.freiman_completion import (
    CompletionGeometry, bit_elements, bound_holds, character_expansion,
)


class FreimanCompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fields = {
            9: CompletionGeometry(Field(3, (1, 0, 1))),
            27: CompletionGeometry(Field(3, (1, 2, 0, 1))),
            81: CompletionGeometry(Field(3, (2, 0, 1, 0, 1))),
            243: CompletionGeometry(Field(3, (1, 2, 0, 0, 0, 1))),
        }

    def test_four_triple_equations_imply_pair_relation(self):
        # Derive the implication in the free F_3-vector space on the labels,
        # independently of any finite-field membership computation.
        labels = "uvwzabcd"
        triples = ("uab", "wac", "bzd", "cvd")
        coefficients = (1, -1, -1, 1)
        combined = {label: 0 for label in labels}
        for coefficient, triple in zip(coefficients, triples):
            for label in triple:
                combined[label] = (combined[label] + coefficient) % 3
        self.assertEqual(combined, dict(zip(labels, (1, 1, 2, 2, 0, 0, 0, 0))))

    def test_complete_f27_and_f81_relations(self):
        for q, relation_count, minimum in ((27, 780, 1), (81, 28880, 2)):
            report = self.fields[q].relation_report()
            self.assertEqual(report["relations_examined"], relation_count)
            self.assertEqual(report["minimum_completions"], minimum)
            self.assertEqual(report["failed_relations"], 0)

    def test_f243_all_normalized_relations(self):
        report = self.fields[243].relation_report(normalized=True)
        self.assertEqual(report["relations_examined"], 7080)
        self.assertEqual(report["ordered_relations_represented"], 856680)
        self.assertEqual(report["minimum_completions"], 10)
        self.assertEqual(report["failed_relations"], 0)

    def test_square_scaling_transports_completion_sets(self):
        geometry = self.fields[27]
        f = geometry.f
        for relation in geometry.relations(normalized=True):
            completions = tuple(bit_elements(geometry.completion_mask(*relation)))
            for scalar in geometry.squares:
                scaled = tuple(f.mul[scalar][x] for x in relation)
                expected = {f.mul[scalar][a] for a in completions}
                self.assertEqual(set(bit_elements(geometry.completion_mask(*scaled))), expected)

    def test_f9_failure_is_a_real_failure_of_affine_forcing(self):
        geometry = self.fields[9]
        f = geometry.f
        report = geometry.relation_report()
        self.assertEqual(report["relations_examined"], 8)
        self.assertEqual(report["failed_relations"], 8)
        relation = (1, 2, 3, 6)
        self.assertEqual(geometry.completion_mask(*relation), 0)
        # Every distinct zero-sum triple is absent.  Even allowing repetitions,
        # the delta function at 1 solves every zero-sum-triple equation but
        # violates the displayed pair-sum relation.
        values = {s: int(s == 1) for s in geometry.squares}
        for a, b, c in product(geometry.squares, repeat=3):
            if f.add[f.add[a][b]][c] == 0:
                self.assertEqual((values[a] + values[b] + values[c]) % 3, 0)
        u, v, w, z = relation
        self.assertNotEqual((values[u] + values[v]) % 3,
                            (values[w] + values[z]) % 3)

    def test_all_nondegenerate_triple_intersections(self):
        for q, expected_minimum in ((27, 2), (81, 6), (243, 26)):
            report = self.fields[q].triple_report()
            self.assertEqual(report["nondegenerate_ordered_increment_pairs"], (q - 1) * (q - 2))
            self.assertEqual(report["minimum_intersection"], expected_minimum)
            self.assertEqual(report["empty_intersections"], 0)
        small = self.fields[9].triple_report()
        self.assertEqual(small["empty_intersections"], 32)
        self.assertEqual(small["first_failure"], [1, 1])

    def test_character_indicator_root_correction(self):
        for geometry in self.fields.values():
            # The F_9 failure is deliberately included: zero characters at the
            # roots must not be counted as nonzero square memberships.
            relation = next(geometry.relations(normalized=True))
            report = character_expansion(geometry, relation)
            self.assertGreaterEqual(report["root_correction"], 0)
            self.assertLessEqual(report["root_correction"], 32)
            self.assertEqual(report["raw_indicator_sum"] - report["root_correction"],
                             16 * report["completion_count"])

    def test_invalid_input_and_exact_radical_bound_controls(self):
        geometry = self.fields[27]
        with self.assertRaises(ValueError):
            geometry.completion_mask(0, 1, 1, 1)
        with self.assertRaises(ValueError):
            geometry.completion_mask(1, 1, 1, 9)
        with self.assertRaises(ValueError):
            CompletionGeometry(Field(2, (1, 1, 1)))
        self.assertFalse(bound_holds(0, 243, 38, 11, 16))
        self.assertTrue(bound_holds(3, 243, 38, 11, 16))
        self.assertFalse(bound_holds(0, 27, 15, 2, 8))
        self.assertTrue(bound_holds(1, 27, 15, 2, 8))


if __name__ == "__main__":
    unittest.main()
