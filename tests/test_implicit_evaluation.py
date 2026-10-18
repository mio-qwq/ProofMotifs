import unittest
from copy import deepcopy
from tools import implicit_evaluation as e


class ImplicitEvaluationTests(unittest.TestCase):
    def test_construct_and_independent_verifier(self):
        points = [[0, 0], [1, 0], [0, 1], [1, 1]]
        c = e.construct(points)
        self.assertEqual(c['minimum_common_degree'], 2)
        self.assertEqual(c['hilbert_profile'], [1, 3, 4])
        self.assertTrue(e.verify(points, c)[0])

    def test_rejected_prefix_is_not_plateau(self):
        c = e.construct([[0, 0], [0, 1]])
        self.assertEqual(c['minimum_common_degree'], 1)
        self.assertEqual(c['observed_coordinate_offers'], 2)

    def test_finite_field_no_separating_linear_form(self):
        from itertools import product
        points = list(product(range(2), repeat=3))
        c = e.construct(points, 2)
        self.assertEqual(c['minimum_common_degree'], 3)
        self.assertEqual(c['hilbert_profile'], [1, 4, 7, 8])
        self.assertTrue(e.verify(points, c, 2)[0])

    def test_inverse_and_border_corruptions(self):
        points = [[0, 0], [1, 0], [0, 1], [1, 1]]
        c = e.construct(points)
        for kind in ['inverse', 'border', 'omit', 'degrees', 'witness', 'profile_type', 'bound', 'telemetry']:
            bad = deepcopy(c)
            if kind == 'inverse':
                bad['inverse_evaluation'][0][0] += 1
            elif kind == 'border':
                bad['multiplication_coordinates'][0][0][0] += 1
            elif kind == 'omit':
                bad['multiplication_coordinates'].pop()
            elif kind == 'degrees':
                bad['minimum_common_degree'] += 1
            elif kind == 'witness':
                bad['dual_minimality_witnesses'][0]['target_pairing'] += 1
            elif kind == 'profile_type':
                bad['hilbert_profile'][0] = True
            elif kind == 'bound':
                bad['proved_offer_bound'] = -1
            else:
                bad['observed_coordinate_offers'] = -100
            self.assertFalse(e.verify(points, bad)[0], kind)

    def test_rejected_divisors_need_not_form_monomial_ideal(self):
        points = [[0, 0], [1, 1], [2, 2], [3, 3], [0, 1]]
        self.assertTrue(all(x*x == x*y and y*y == x*y-x+y for x, y in points))
        # If xy is retained before both squares, rejecting all their multiples
        # leaves only 1,x,y,xy. Safe frontier closure must still reach degree3.
        c = e.construct(points)
        self.assertEqual(c['hilbert_profile'], [1, 3, 4, 5])
        self.assertEqual(c['minimum_common_degree'], 3)
        self.assertTrue(e.verify(points, c)[0])

    def test_input_boundaries(self):
        for points, p in [([], 0), ([[0], [0]], 0), ([[0], [2]], 2),
                          ([[0], [1, 2]], 0), ([[0], [1]], 4), ([[0.5]], 0)]:
            with self.assertRaises(ValueError):
                e.construct(points, p)

    def test_singleton(self):
        c = e.construct([[3, 7]], 11)
        self.assertEqual(c['minimum_common_degree'], 0)
        self.assertEqual(c['cardinal_minimum_degrees'], [0])
        self.assertTrue(e.verify([[3, 7]], c, 11)[0])
        self.assertFalse(e.verify([[3, 7]], c, 0)[0])


if __name__ == '__main__':
    unittest.main()
