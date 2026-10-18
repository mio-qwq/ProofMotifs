"""Mathematical boundary and certificate-corruption controls."""
from copy import deepcopy
from fractions import Fraction
import unittest

from tools.feature_repair import oracle, optimize, verify


def instance(rows, target, blocks=()):
    return {'omega': list(range(len(rows[0]))), 'target_indices': target,
            'base_rows': rows, 'blocks': list(blocks)}


class FeatureRepairBoundaries(unittest.TestCase):
    def test_homogeneous_face_cannot_silently_add_constant(self):
        homogeneous = instance([[1, 2]], [0])
        affine = instance([[1, 2], [1, 1]], [0])
        self.assertEqual(oracle(homogeneous, 0)['kind'], 'trade')
        self.assertEqual(oracle(affine, 0)['kind'], 'selector')

    def test_evaluated_rational_weights_are_integralized(self):
        data = instance([[0, Fraction(2, 3), 1]], [0])
        cert = oracle(data, 0)
        self.assertEqual(cert['kind'], 'selector')
        self.assertEqual(list(map(Fraction, cert['weights'])), [0, 2, 3])

    def test_all_targets_is_vacuously_feasible(self):
        data = instance([[2, 7]], [0, 1])
        self.assertEqual(optimize(data)['cost'], '0')

    def test_matching_feature_columns_forbid_separation(self):
        data = instance([[1, 1], [-3, -3]], [0])
        cert = oracle(data, 0)
        self.assertEqual(cert['kind'], 'trade')
        self.assertEqual(list(map(Fraction, cert['trade'])), [-1, 1])

    def test_breaking_both_original_rays_does_not_repair(self):
        data = instance([[1, 1, 1]], [0],
                        [{'name': 'signed', 'cost': 1, 'rows': [[0, 1, -1]]}])
        self.assertEqual(optimize(data)['status'], 'dictionary_impossible')

    def test_target_trade_coefficients_must_be_free_signed(self):
        data = instance([[1, 1, 1], [0, 1, Fraction(1, 2)]], [0, 1])
        cert = oracle(data, 0)
        self.assertEqual(cert['kind'], 'trade')
        self.assertEqual(list(map(Fraction, cert['trade'])),
                         [Fraction(-1, 2), Fraction(-1, 2), 1])
        # A different target configuration genuinely needs a positive D coefficient.
        data = instance([[1, 1, 1], [0, 1, 2]], [0, 1])
        cert = oracle(data, 0)
        self.assertGreater(Fraction(cert['trade'][0]), 0)

    def test_corrupted_primal_and_dual_are_rejected(self):
        positive = instance([[0, 1]], [0])
        cert = deepcopy(oracle(positive, 0))
        cert['weights'][1] = '0'
        with self.assertRaises(AssertionError):
            verify(positive, 0, cert)
        negative = instance([[1, 1]], [0])
        cert = deepcopy(oracle(negative, 0))
        cert['trade'][1] = '0'
        with self.assertRaises(AssertionError):
            verify(negative, 0, cert)


if __name__ == '__main__':
    unittest.main()
