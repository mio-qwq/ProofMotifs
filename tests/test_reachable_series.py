from copy import deepcopy
from fractions import Fraction
import unittest
from tools import reachable_series as rs


class ReachableSeriesTests(unittest.TestCase):
    def test_sharp_word_bound(self):
        for d in range(10):
            m = rs.shift_family(d, 2)
            c, stats = rs.synthesize(m)
            self.assertTrue(rs.verify(m, c)[0])
            self.assertEqual(stats['rank'], d+1)
            self.assertEqual(c['witness']['word'], 'x'*d)

    def test_zero_and_constant(self):
        for value in (0, 2):
            m = rs.Model([1], {}, [value])
            c, _ = rs.synthesize(m)
            self.assertTrue(rs.verify(m, c)[0])
            self.assertEqual(c['decision'], 'nonzero' if value else 'zero')

    def test_closed_span_is_essential(self):
        m = rs.shift_family(2)
        c = {'version': 'PM-SUCCINCT-B-1', 'field': 'Q', 'rows': [[1, 0, 0]],
             'words': [''], 'initial': [1], 'closure': {'x': [[0]], 'y': [[0]]},
             'outputs': [0], 'decision': 'zero'}
        self.assertEqual(rs.verify(m, c), (False, 'closure identity'))

    def test_field_specialization(self):
        for p, rank in ((None, 2), (2, 1), (3, 2)):
            m = rs.Model([1, 0], {'x': [[0, 2], [0, 0]]}, [0, 1], p)
            c, stats = rs.synthesize(m)
            self.assertTrue(rs.verify(m, c)[0])
            self.assertEqual(stats['rank'], rank)
            self.assertEqual(c['decision'], 'zero' if p == 2 else 'nonzero')

    def test_denominator_and_modulus_contract(self):
        with self.assertRaises(ValueError):
            rs.Model([Fraction(1, 2)], {}, [1], 2)
        with self.assertRaises(ValueError):
            rs.Model([1], {}, [1], 4)

    def test_witness_and_provenance_checked(self):
        m = rs.shift_family(3, 3)
        c, _ = rs.synthesize(m)
        bad = deepcopy(c)
        bad['witness']['word'] = 'x'
        self.assertEqual(rs.verify(m, bad), (False, 'witness coefficient'))
        bad = deepcopy(c)
        bad['rows'][1][0] = 1
        self.assertEqual(rs.verify(m, bad), (False, 'basis word provenance'))


if __name__ == '__main__':
    unittest.main()
