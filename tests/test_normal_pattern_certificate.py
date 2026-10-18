"""Rejection tests for exact normal-character basecase certificates."""
import copy
import unittest

from tools.normal_pattern_certificate import build_report, verify_report


class NormalPatternCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = build_report()

    def damaged(self):
        return copy.deepcopy(self.certificate)

    def test_accepts_exact_exclusion_and_two_selected_witnesses(self):
        receipt = verify_report(self.certificate)
        self.assertTrue(receipt["verified"])
        self.assertEqual(receipt["degree_four_pattern_count"], 18)
        self.assertEqual(receipt["degree_four_normal_pattern_count"], 0)
        self.assertEqual([r["conjugate_rank"] for r in receipt["witnesses"]], [5, 8])
        self.assertFalse(receipt["scope"]["field_enumeration_used"])
        self.assertFalse(receipt["scope"]["all_normal_seeds_connected_claimed"])
        self.assertFalse(receipt["scope"]["single_orbit_full_rank_claimed"])

    def test_rejects_false_gcd_divisibility(self):
        report = self.damaged()
        report["degree_four"]["gcd"][0] = 1
        with self.assertRaisesRegex(ValueError, "gcd divisibility"):
            verify_report(report)

    def test_rejects_false_bezout_identity(self):
        report = self.damaged()
        report["degree_four"]["bezout"] = [[], [], []]
        with self.assertRaisesRegex(ValueError, "Bezout"):
            verify_report(report)

    def test_rejects_false_annihilator(self):
        for key in ("subfield_quotient", "linearized_quotient"):
            with self.subTest(key=key):
                report = self.damaged()
                report["degree_four"][key][0] = (
                    report["degree_four"][key][0] + 1) % 3
                with self.assertRaisesRegex(ValueError, "annihilator"):
                    verify_report(report)

    def test_rejects_reducible_field(self):
        report = self.damaged()
        report["witnesses"][0]["modulus"][0] = 0
        with self.assertRaisesRegex(ValueError, "Rabin"):
            verify_report(report)

    def test_rejects_forged_rank_and_conjugate_basis(self):
        for key, value in (("conjugate_rank", 4), ("conjugates", [[1]] * 5)):
            with self.subTest(key=key):
                report = self.damaged()
                report["witnesses"][0][key] = value
                with self.assertRaisesRegex(ValueError, "conjugate"):
                    verify_report(report)

    def test_rejects_changed_character_witness_and_seed(self):
        for key, value in (("characters", [1, 1, 1]), ("a", [1]),
                           ("gamma_seed_exponents", [0, 89, 86]),
                           ("connectivity_index", 11)):
            with self.subTest(key=key):
                report = self.damaged()
                report["witnesses"][0][key] = value
                with self.assertRaises(ValueError):
                    verify_report(report)

    def test_rejects_expanded_scope_and_duplicate_degree(self):
        report = self.damaged()
        report["scope"]["all_normal_seeds_connected_claimed"] = True
        with self.assertRaisesRegex(ValueError, "scope"):
            verify_report(report)
        report = self.damaged()
        report["witnesses"][1] = copy.deepcopy(report["witnesses"][0])
        with self.assertRaisesRegex(ValueError, "scope"):
            verify_report(report)

    def test_rejects_false_degree_four_count(self):
        report = self.damaged()
        report["degree_four"]["normal_pattern_count"] = 1
        with self.assertRaisesRegex(ValueError, "count"):
            verify_report(report)


if __name__ == "__main__":
    unittest.main()
