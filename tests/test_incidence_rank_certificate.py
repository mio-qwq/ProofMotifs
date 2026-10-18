import unittest

from tools.cancellation import Field
from tools.incidence_rank_certificate import (
    determinant3, rank_profile, rank_certificate, square_incidence)


class IncidenceRankCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.f9 = Field(3, (1, 0, 1))
        cls.f27 = Field(3, (1, 2, 0, 1))
        cls.f81 = Field(3, (2, 0, 1, 0, 1))
        cls.f243 = Field(3, (1, 2, 0, 0, 0, 1))

    def test_f243_rank_lower_minor_matches_affine_upper_bound(self):
        report = rank_certificate(self.f243)
        self.assertEqual((report['vertex_count'], report['edge_count']), (121, 1210))
        self.assertEqual((report['incidence_rank'], report['incidence_nullity']), (115, 6))
        self.assertTrue(report['rank_condition_holds'])
        self.assertIn(report['rank_minor_determinant_mod3'], (1, 2))
        self.assertIn(report['affine_basis_minor_determinant_mod3'], (1, 2))
        self.assertEqual(report['exact_kernel_annihilation_checks'], 1210*6)

    def test_previous_nontrivial_fields_have_minimal_kernel(self):
        for f, rank, nullity in ((self.f27, 9, 4), (self.f81, 35, 5)):
            report = rank_certificate(f)
            self.assertEqual((report['incidence_rank'], report['incidence_nullity']),
                             (rank, nullity))
            self.assertTrue(report['rank_condition_holds'])

    def test_f9_is_a_negative_control_for_the_criterion(self):
        report = rank_certificate(self.f9)
        self.assertEqual((report['vertex_count'], report['edge_count']), (4, 0))
        self.assertEqual((report['incidence_rank'], report['incidence_nullity']), (0, 4))
        self.assertEqual(report['affine_basis_dimension'], 3)
        self.assertFalse(report['rank_condition_holds'])

    def test_pair_completion_produces_only_distinct_zero_sum_edges(self):
        f = self.f81
        vertices, edges, rows = square_incidence(f)
        self.assertEqual(len(set(edges)), len(edges))
        self.assertEqual(len(edges), 120)
        for edge, row in zip(edges, rows):
            self.assertEqual(tuple(sorted(set(edge))), edge)
            self.assertEqual(f.add[f.add[edge[0]][edge[1]]][edge[2]], 0)
            self.assertEqual(sum(row), 3)
            self.assertEqual(tuple(vertices[i] for i, x in enumerate(row) if x), edge)

    def test_exact_matrix_utilities_and_rejections(self):
        matrix = [[0, 1], [2, 0]]
        self.assertEqual(determinant3(matrix), 1)
        self.assertEqual(rank_profile(matrix, 2)['rank'], 2)
        self.assertEqual(determinant3([[1, 2], [2, 1]]), 0)
        self.assertEqual(rank_profile([[1, 2], [2, 1]], 2)['rank'], 1)
        self.assertEqual(determinant3([]), 1)
        with self.assertRaises(ValueError):
            rank_profile([[3]], 1)
        with self.assertRaises(ValueError):
            determinant3([[1, 0]])
        with self.assertRaises(ValueError):
            square_incidence(Field(3, (0, 1)))


if __name__ == '__main__':
    unittest.main()
