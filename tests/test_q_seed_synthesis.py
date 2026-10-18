from copy import deepcopy
from fractions import Fraction as Q
import unittest
from tools import q_seed_synthesis as qs


class QSeedSynthesisTests(unittest.TestCase):
    def seed(self, terms, cost=1, pp=(0,)):
        return qs.seed_from_parts('test', cost, pp, terms)

    def test_raw_partial_fractions_and_polynomial(self):
        seed = self.seed([(3, 2, 5), (6, 1, -2), (-5, 3, Q(2, 3))], pp=(0, 2, -1))
        dec = qs.decompose(seed)
        self.assertEqual(dec['poly'], [0, 2, -1])
        got = {(x['alpha'], x['order']): x['coefficient'] for x in dec['terms']}
        self.assertEqual(got, {(Q(3), 2): 5, (Q(6), 1): -2, (Q(-5), 3): Q(2, 3)})

    def test_same_orbit_not_distinct_pole_count(self):
        seeds = [self.seed([(3, 1, 1)], 9), self.seed([(6, 1, 1)], 2)]
        out = qs.synthesize(seeds, 2)
        self.assertEqual(out['status'], 'strong_rank_insufficient')
        self.assertEqual(out['quotient_rank'], 1)
        self.assertTrue(qs.verify(seeds, 2, out)[0])
        self.assertEqual(qs.synthesize(seeds, 1)['selected'], [1])

    def test_exact_finite_chain_and_negative_orbit(self):
        dec = qs.decompose(self.seed([(-3, 2, 2), (-24, 2, -2)]))
        anti = qs.telescoper(dec)
        self.assertEqual(qs.shift_difference(anti), dec)
        self.assertEqual(len(anti['terms']), 3)
        self.assertEqual(qs.orbit(Q(-3, 8)), (Q(-3), -3))

    def test_higher_order_is_distinct_quotient_coordinate(self):
        seeds = [self.seed([(3, 1, 1)]), self.seed([(6, 2, 1)])]
        out = qs.synthesize(seeds, 2)
        self.assertEqual(out['quotient_rank'], 2)
        self.assertTrue(qs.verify(seeds, 2, out)[0])

    def test_strong_contract_not_basic_faithfulness(self):
        seed = self.seed([], pp=(0, 1))
        out = qs.synthesize([seed], 1)
        self.assertEqual(out['status'], 'strong_rank_insufficient')
        self.assertEqual(out['repairs'][0]['telescoper']['poly'], [0, 1])
        # J_z^n(1) is nonzero at degree n, so strong failure is not basic failure.
        coefficient = Q(1)
        for n in range(1, 15):
            coefficient /= 2**n-1
            self.assertNotEqual(coefficient, 0)

    def test_reject_incomplete_factor_pole_constant_and_cost(self):
        bad = self.seed([(3, 1, 1)])
        bad['poles'] = []
        with self.assertRaises(ValueError):
            qs.synthesize([bad], 1)
        bad = self.seed([(3, 1, 1)])
        bad['num'][0] = 1
        with self.assertRaises(ValueError):
            qs.decompose(bad)
        bad = self.seed([(3, 1, 1)], -1)
        with self.assertRaises(ValueError):
            qs.synthesize([bad], 1)
        with self.assertRaises(ValueError):
            qs.scalar(0.5)
        with self.assertRaises(ValueError):
            qs.telescoper({'poly': [Q(1)], 'terms': []})
        bad = self.seed([(3, 1, 1)])
        bad['poles'][0]['order'] = 10**30
        with self.assertRaises(ValueError):
            qs.decompose(bad)

    def test_certificate_corruption_and_json_round_trip(self):
        seeds = [self.seed([(3, 1, 1)]), self.seed([(6, 1, 1)], 2)]
        out = qs.synthesize(seeds, 1)
        self.assertTrue(qs.verify(seeds, 1, qs.jsonable(out))[0])
        for name in ('cost', 'quotient_rank'):
            bad = deepcopy(out)
            bad[name] += 1
            self.assertFalse(qs.verify(seeds, 1, bad)[0])
        bad = deepcopy(out)
        bad['repairs'][1]['telescoper']['terms'][0]['coefficient'] += 1
        self.assertFalse(qs.verify(seeds, 1, bad)[0])
        bad = deepcopy(out)
        bad['contract'] = 'ordinary faithfulness iff quotient rank'
        self.assertFalse(qs.verify(seeds, 1, bad)[0])
        bad = deepcopy(out)
        bad['repairs'][1]['telescoper']['poly'][0] = 1
        self.assertFalse(qs.verify(seeds, 1, bad)[0])

    def test_zero_rank_and_empty_dictionary(self):
        self.assertEqual(qs.synthesize([], 0)['status'], 'selected')
        self.assertEqual(qs.synthesize([], 1)['status'], 'strong_rank_insufficient')
        self.assertTrue(qs.verify([], 0, qs.synthesize([], 0))[0])


if __name__ == '__main__':
    unittest.main()
