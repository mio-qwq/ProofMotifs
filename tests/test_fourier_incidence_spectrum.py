import unittest

from tools.cancellation import Field
from tools.fourier_incidence_spectrum import spectrum_report


class FourierIncidenceSpectrumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.f27 = Field(3, (1, 2, 0, 1))
        cls.f81 = Field(3, (2, 0, 1, 0, 1))
        cls.f243 = Field(3, (1, 2, 0, 0, 0, 1))

    def test_exact_spectra_are_affine_exponents(self):
        for f in (self.f27, self.f81, self.f243):
            report = spectrum_report(f)
            self.assertTrue(report['spectrum_matches'])
            self.assertEqual(report['admissible_exponents'],
                             [0] + [3**j for j in range(f.degree)])
            self.assertEqual(report['relation_size'],
                             report['expected_relation_size'])

    def test_even_degree_order_two_character_is_rejected(self):
        report = spectrum_report(self.f81)
        self.assertEqual(report['order_two_exponent'], 20)
        self.assertIsNotNone(report['order_two_failure'])
        self.assertEqual(report['nonsquare_s_with_square_s2_plus_1'], 24)

    def test_odd_degrees_have_no_order_two_character(self):
        for f in (self.f27, self.f243):
            report = spectrum_report(f)
            self.assertIsNone(report['order_two_exponent'])
            self.assertIsNone(report['order_two_failure'])

    def test_invalid_field_rejected(self):
        with self.assertRaises(ValueError):
            spectrum_report(Field(2, (1, 1, 1)))


if __name__ == '__main__':
    unittest.main()
