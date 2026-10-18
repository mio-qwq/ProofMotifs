import copy
import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location(
    'factor_readout', Path(__file__).resolve().parents[1]/'tools/factor_readout.py')
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def binary_fixture(p, roots):
    """Known roots ONLY manufacture test certificates, not solver inputs."""
    f = [1]
    for a in roots:
        f = M.mul(f, [-a, 1], p)
    cardinals = []
    for a in roots:
        numerator, den = [1], 1
        for b in roots:
            if a != b:
                numerator = M.mul(numerator, [-b, 1], p)
                den = den*(a-b) % p
        cardinals.append([x*pow(den, -1, p) % p for x in numerator])
    tests = []
    for j in range((len(roots)-1).bit_length()):
        e = []
        for i, cardinal in enumerate(cardinals):
            if (i >> j) & 1:
                e = M.add(e, cardinal, p)
        tests.append({'poly': e, 'labels': [0, 1]})
    return f, tests


class FactorReadoutTests(unittest.TestCase):
    def test_large_prime_no_field_loop(self):
        out = M.demo()
        self.assertEqual(out['partial']['fixed_dimension'], 3)
        self.assertEqual(len(out['partial']['blocks']), 2)
        self.assertEqual(len(out['complete']['blocks']), 3)

    def test_binary_sharp_length_and_incomplete(self):
        f, tests = binary_fixture(101, list(range(9)))
        self.assertEqual(len(tests), 4)
        self.assertEqual(M.readout(101, f, tests)['status'], 'COMPLETE')
        out = M.readout(101, f, tests[:3])
        self.assertEqual(out['status'], 'PARTIAL')
        self.assertEqual(len(out['blocks']), 8)

    def test_char_two_joint_generators(self):
        f = M.mul(M.mul([0, 1], [1, 1], 2), [1, 1, 1], 2)
        basis = M.fixed_basis(2, f)
        tests = [{'poly': b, 'labels': [0, 1]} for b in basis]
        out = M.readout(2, f, tests)
        self.assertEqual(out['fixed_dimension'], 3)
        self.assertEqual(out['status'], 'COMPLETE')
        self.assertTrue(all(M.readout(2, f, [t])['status'] == 'PARTIAL' for t in tests))

    def test_irreducible_empty_family(self):
        out = M.readout(3, [1, 0, 1], [])
        self.assertEqual(out['status'], 'COMPLETE')
        self.assertEqual(out['fixed_dimension'], 1)

    def test_nonreduced_rejected(self):
        with self.assertRaises(ValueError):
            M.readout(5, [0, 0, 1], [])

    def test_false_label_promise_rejected(self):
        with self.assertRaises(ValueError):
            M.readout(7, [0, -1, 1], [{'poly': [0, 1], 'labels': [0]}])

    def test_malformed_scalar_types(self):
        for p in [True, 0, 1, 3.0]:
            with self.assertRaises(ValueError):
                M.readout(p, [0, -1, 1], [])
        for labels in [[0, True], [0, 0], [-1, 0], [0, 7], []]:
            with self.assertRaises(ValueError):
                M.readout(7, [0, -1, 1], [{'poly': [0, 1], 'labels': labels}])

    def test_invalid_modulus(self):
        for f in [[], [1], [0], [1, 2], [0, True, 1]]:
            with self.assertRaises(ValueError):
                M.readout(7, f, [])

    def test_repeated_test_is_not_new_information(self):
        f, tests = binary_fixture(101, list(range(5)))
        out = M.readout(101, f, [tests[0], tests[0]])
        self.assertEqual(out['observable_algebra_dimension'], 2)
        self.assertEqual(out['status'], 'PARTIAL')

    def test_tampering_does_not_infer_good_labels(self):
        f, tests = binary_fixture(101, list(range(5)))
        tests = copy.deepcopy(tests)
        tests[0]['poly'] = [2]
        with self.assertRaises(ValueError):
            M.readout(101, f, tests)

    def test_test_shape_and_degree_are_explicit(self):
        for test in [None, [], {}, {'poly': [0, 0, 0], 'labels': [0, 1]}]:
            with self.assertRaises(ValueError):
                M.readout(7, [0, -1, 1], [test])

    def test_raw_generator_full_rank_is_not_a_readout(self):
        p, f = 1000000007, [4, -5, 5, -5, 1]
        basis, offers = M.generated_basis(p, f, [[0, 0, 1]])
        self.assertEqual(len(basis), 3)
        self.assertLessEqual(offers, 3)
        with self.assertRaises(ValueError):
            M.readout(p, f, [{'poly': [0, 0, 1], 'labels': [0, 1]}])


if __name__ == '__main__':
    unittest.main()
