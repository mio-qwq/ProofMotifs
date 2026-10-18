"""Positive and negative tests for the PM-CYCLE12-D minimal certificates."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location("connected_normal_certificate",
                                            Path(__file__).with_name("pm_cycle12_d_minimal.py"))
CERT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CERT)


class MinimalConnectedNormalCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = CERT.build_report()

    def reject_change(self, operation):
        changed = copy.deepcopy(self.report)
        operation(changed)
        with self.assertRaises((ValueError, KeyError)):
            CERT.verify_report(changed)

    def test_deterministic_build_and_scope(self):
        self.assertEqual(self.report, CERT.build_report())
        checked = CERT.verify_report(self.report)
        self.assertTrue(checked["verified"])
        self.assertEqual([r["m"] for r in checked["witnesses"]], [5, 6, 7, 8, 10, 16])

    def test_exact_factorization_control(self):
        self.assertEqual(CERT.prime_factorization((3**16-1)//2),
                         [2, 2, 2, 2, 2, 5, 17, 41, 193])

    def test_changed_normal_determinant_rejected(self):
        self.reject_change(lambda r: r["witnesses"][-1]["normality"].update(determinant=0))

    def test_changed_character_rejected(self):
        self.reject_change(lambda r: r["witnesses"][0]["character_powers_y_minus_1_y_y_plus_1"].__setitem__(0, 0))

    def test_missing_prime_factor_rejected(self):
        self.reject_change(lambda r: r["witnesses"][-1]["subgroup_certificate"]["N_factorization_with_multiplicity"].pop())

    def test_missing_maximal_subgroup_check_rejected(self):
        self.reject_change(lambda r: r["witnesses"][-1]["subgroup_certificate"]["maximal_subgroup_exclusions"].pop())

    def test_changed_ratio_rejected(self):
        self.reject_change(lambda r: r["witnesses"][0].update(a=1))

    def test_changed_modulus_rejected(self):
        self.reject_change(lambda r: r["witnesses"][0]["modulus"].__setitem__(0, 2))

    def test_changed_degree_scope_rejected(self):
        self.reject_change(lambda r: r["scope"]["degrees"].append(12))

    def test_disconnected_normal_boundary_rejected(self):
        f = CERT.Field([2, 0, 0, 1, 0, 0, 0, 0, 1])
        with self.assertRaisesRegex(ValueError, "maximal proper subgroup"):
            f.witness(4863)

    def test_joint_generation_does_not_require_primitive_a(self):
        # Targeted predicate control, not an additional existence-degree table.
        f = CERT.Field([2, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1])
        row = f.witness(2190)
        self.assertTrue(row["subgroup_certificate"]["joint_generation"])
        self.assertFalse(row["subgroup_certificate"]["a_generates_S"])

    def test_non_normal_parameter_rejected(self):
        with self.assertRaisesRegex(ValueError, "excluded parameter"):
            CERT.Field(self.report["witnesses"][0]["modulus"]).witness(0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
