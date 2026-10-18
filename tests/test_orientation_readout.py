import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools'))
import factor_readout as F
import orientation_readout as O


class OrientationTests(unittest.TestCase):
    def test_conditional_root_free_split(self):
        out = O.demo()
        self.assertEqual(out['digit_levels'], 5)
        self.assertEqual(out['factor'], [96, 1])
        self.assertLessEqual(out['maximum_nonempty_masks'], 12)

    def test_tensor_multiplication_matches_grid(self):
        p, f = 97, [24, -50, 35, -10, 1]
        r = O.Tensor(p, F.trim(f, p))
        a, b = list(range(16)), list(reversed(range(16)))
        c = r.multiply(a, b)
        def value(v, x, y):
            return sum(v[i*4+j]*pow(x, i, p)*pow(y, j, p)
                       for i in range(4) for j in range(4)) % p
        for x in range(1, 5):
            for y in range(1, 5):
                self.assertEqual(value(c, x, y), value(a, x, y)*value(b, x, y) % p)

    def test_wrong_primary_generator_rejected(self):
        with self.assertRaises(ValueError):
            O.construct(97, [24, -50, 35, -10, 1], 96)

    def test_negative_tensor_power_rejected(self):
        r = O.setup(97, [24, -50, 35, -10, 1])
        with self.assertRaises(ValueError):
            r.power(r.one, -1)

    def test_corrupted_mask_rejected(self):
        out = O.demo()
        bad = copy.deepcopy(out['orientation'])
        bad[0] = (bad[0]+1) % 97
        with self.assertRaises(ValueError):
            O.verify_orientation(97, out['modulus'], bad)

    def test_half_offdiagonal_not_boolean(self):
        p, f = 97, [24, -50, 35, -10, 1]
        r = O.setup(p, f)
        delta = [0]*16
        delta[4], delta[1] = 1, p-1
        off = r.power(delta, p-1)
        e = r.scale(off, pow(2, -1, p))
        self.assertEqual(r.add(e, r.swap(e)), off)
        self.assertNotEqual(r.multiply(e, e), e)
        self.assertEqual(len(r.partial_trace(e)), 1)
        with self.assertRaises(ValueError):
            O.verify_orientation(p, f, e)

    def test_odd_cyclic_orientation_has_constant_trace(self):
        # Outside even-input contract: a genuine three-cycle is regular.
        p, f = 5, [0, 2, 2, 1]  # X(X-1)(X-2)
        f = F.trim(f, p)
        r = O.Tensor(p, f)
        cards = []
        for x in range(3):
            a, den = [1], 1
            for y in range(3):
                if x != y:
                    a, den = F.mul(a, [-y, 1], p), den*(x-y) % p
            cards.append([z*pow(den, -1, p) % p for z in a])
        e = [0]*9
        for i, j in [(0, 1), (1, 2), (2, 0)]:
            e = r.add(e, [x*y % p for x in cards[i] for y in cards[j]])
        self.assertEqual(r.multiply(e, e), e)
        delta = [0]*9
        delta[3], delta[1] = 1, p-1
        self.assertEqual(r.add(e, r.swap(e)), r.power(delta, p-1))
        self.assertEqual(r.partial_trace(e), [1])
        with self.assertRaises(ValueError):
            O.verify_orientation(p, f, e)

    def test_nonsplit_and_nonreduced_rejected(self):
        for p, f in [(3, [1, 0, 1]), (5, [0, 0, 1])]:
            with self.assertRaises(ValueError):
                O.construct(p, f, p-1)


if __name__ == '__main__':
    unittest.main()
