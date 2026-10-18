import unittest

from tools.cancellation import Field
from tools.cyclotomic_incidence import cyclotomic_incidence


class CyclotomicIncidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.f81 = Field(3, (2, 0, 1, 0, 1))
        cls.f243 = Field(3, (1, 2, 0, 0, 0, 1))

    def test_f81_index_five_has_a_real_extra_kernel_dimension(self):
        report = cyclotomic_incidence(self.f81, 5)
        self.assertEqual((report['subgroup_size'], report['edge_count']), (16, 16))
        self.assertEqual((report['incidence_nullity'],
                          report['affine_restriction_dimension']), (6, 5))
        self.assertFalse(report['affine_kernel_holds'])

    def test_sparse_subgroups_can_have_no_lines(self):
        for f, index, size in ((self.f81, 4, 20), (self.f81, 8, 10),
                               (self.f243, 11, 22), (self.f243, 22, 11)):
            report = cyclotomic_incidence(f, index)
            self.assertEqual(report['subgroup_size'], size)
            self.assertEqual(report['edge_count'], 0)
            self.assertEqual(report['incidence_nullity'], size)
            self.assertFalse(report['affine_kernel_holds'])

    def test_subfield_case_records_restricted_affine_dimension(self):
        report = cyclotomic_incidence(self.f81, 10)
        self.assertEqual((report['subgroup_size'], report['edge_count']), (8, 8))
        self.assertEqual((report['incidence_nullity'],
                          report['affine_restriction_dimension']), (3, 3))
        self.assertTrue(report['affine_kernel_holds'])

    def test_affine_basis_subgroup_has_empty_hypergraph(self):
        report = cyclotomic_incidence(self.f81, 16)
        self.assertEqual((report['subgroup_size'], report['edge_count']), (5, 0))
        self.assertEqual((report['incidence_nullity'],
                          report['affine_restriction_dimension']), (5, 5))
        self.assertTrue(report['affine_kernel_holds'])

    def test_rejects_invalid_parameters(self):
        with self.assertRaises(ValueError):
            cyclotomic_incidence(self.f81, 3)
        with self.assertRaises(ValueError):
            cyclotomic_incidence(self.f81, 1)
        with self.assertRaises(ValueError):
            cyclotomic_incidence(Field(2, (1, 1, 1)), 3)


if __name__ == '__main__':
    unittest.main()
