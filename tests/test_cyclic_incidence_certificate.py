"""Polynomial-only cyclic incidence certificate and false-certificate controls."""

from copy import deepcopy
import unittest

from tools.cyclic_incidence_certificate import (
    build_certificate, proper_orbit_control, verify_certificate,
)


class CyclicIncidenceCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = build_certificate()

    def test_polynomial_only_rank_and_field_certificate(self):
        result = verify_certificate(self.certificate)
        self.assertEqual(result["gcd"], [1, 0, 2, 0, 0, 2, 1])
        self.assertEqual(result["seed_orbit_incidence_rank"], 115)
        self.assertEqual(result["full_hypergraph_incidence_rank"], 115)
        self.assertEqual(result["seed_cyclic_orbit_size"], 121)
        self.assertEqual(result["seed_orbit_kernel_dimension"], 6)
        self.assertTrue(result["full_kernel_is_affine"])
        self.assertEqual(result["seed_field_coordinates"], [[1], [0, 0, 0, 0, 1], [2, 0, 0, 0, 2]])

    def test_seed_orbit_is_not_frobenius_invariant(self):
        result = verify_certificate(self.certificate)
        self.assertEqual(result["frobenius_orbit_patterns"],
                         [[0, 4, 68], [0, 12, 83], [0, 7, 36], [0, 13, 34], [0, 19, 58]])
        self.assertEqual(result["seed_orbit_stabilizing_frobenius_exponents"], [0])
        self.assertEqual(result["seed_orbit_semilinear_stabilizer_order"], 121)

    def test_forged_frobenius_invariance_is_rejected(self):
        bad = deepcopy(self.certificate)
        bad["frobenius_orbit_patterns"][1] = [0, 4, 68]
        with self.assertRaisesRegex(ValueError, "orbit-pattern mismatch"):
            verify_certificate(bad)

    def test_corrupted_incidence_bezout_is_rejected(self):
        bad = deepcopy(self.certificate)
        bad["bezout_cyclic_modulus"][0] = (bad["bezout_cyclic_modulus"][0] + 1) % 3
        with self.assertRaisesRegex(ValueError, "incidence Bezout identity failed"):
            verify_certificate(bad)

    def test_corrupted_divisibility_quotient_is_rejected(self):
        bad = deepcopy(self.certificate)
        bad["quotient_seed"][0] = (bad["quotient_seed"][0] + 1) % 3
        with self.assertRaisesRegex(ValueError, "divisibility of seed failed"):
            verify_certificate(bad)

    def test_smaller_common_divisor_cannot_replace_gcd(self):
        bad = deepcopy(self.certificate)
        bad["gcd"] = [2, 1]
        with self.assertRaisesRegex(ValueError, "degree six"):
            verify_certificate(bad)

    def test_corrupted_irreducibility_witness_is_rejected(self):
        bad = deepcopy(self.certificate)
        old = bad["irreducibility_bezout_modulus"][0]
        bad["irreducibility_bezout_modulus"][0] = 1 if old != 1 else 2
        with self.assertRaisesRegex(ValueError, "irreducibility Bezout identity failed"):
            verify_certificate(bad)

    def test_genuine_f81_orbit_can_have_insufficient_rank(self):
        control = proper_orbit_control()
        self.assertEqual(control["generator_order"], 40)
        self.assertEqual([r["gcd_degree"] for r in control["orbit_controls"]], [15, 5])
        self.assertEqual([r["cyclic_orbit_incidence_rank"] for r in control["orbit_controls"]], [25, 35])


if __name__ == "__main__":
    unittest.main()
