from copy import deepcopy
import unittest
from tools import finite_algebra_jet as fj


class FiniteAlgebraJetTests(unittest.TestCase):
    def test_infinite_example_is_only_budget_obstruction(self):
        m = fj.TupleModel([[[(0, 1)]]])
        for budget in (1, 2, 5):
            cert = fj.generate(m, budget)
            self.assertEqual(cert['status'], 'rank_budget_exceeded')
            self.assertEqual(cert['independent_words'], budget+1)
            self.assertTrue(fj.verify(m, cert)[0])

    def test_finite_cycle_and_constant_case(self):
        m = fj.TupleModel([[[(1,), (0, 1)], [(0,), (0,)]]])
        cert = fj.generate(m, 2)
        self.assertTrue(fj.verify(m, cert)[0])
        self.assertEqual((cert['d'], cert['E']), (2, 2))
        self.assertEqual(fj.independent_rank(fj.jets(m, [m.word(w) for w in cert['words']], 1), m.k), 2)
        scalar = fj.TupleModel([[[(3,)]]])
        cert = fj.generate(scalar, 1)
        self.assertEqual((cert['d'], cert['E']), (1, 1))

    def test_dimension_does_not_bound_delay(self):
        for power in (1, 4, 11):
            m = fj.TupleModel([[[(0,), tuple([0]*power+[1])], [(0,), (0,)]]], p=3)
            cert = fj.generate(m, 2)
            self.assertTrue(fj.verify(m, cert)[0])
            basis = [m.word(w) for w in cert['words']]
            self.assertEqual((cert['d'], cert['E']), (2, power+1))
            self.assertEqual(fj.independent_rank(fj.jets(m, basis, power), m.k), 1)
            self.assertEqual(fj.independent_rank(fj.jets(m, basis, power+1), m.k), 2)

    def test_constant_not_rational_function_closure(self):
        m = fj.TupleModel([[[(0, 1)]]])
        fake = {'status': 'closed', 'words': [()], 'd': 1, 'D': 1, 'b': 1,
                'E': 1, 'initial': [1], 'C': [[[[0, 1]]]]}
        self.assertEqual(fj.verify(m, fake), (False, 'closure coefficients must be constant field scalars'))

    def test_input_and_understated_degree_certificates(self):
        m = fj.TupleModel([[[(1,), (0, 1)], [(0,), (0,)]]])
        cert = fj.generate(m, 2)
        bad = deepcopy(cert)
        bad['E'] = 1
        self.assertEqual(fj.verify(m, bad), (False, 'jet bound'))
        for budget in (True, 0, 2.0):
            with self.assertRaises(ValueError):
                fj.generate(m, budget)
        with self.assertRaises(ValueError):
            fj.TupleModel([[[(1,)]]], delta=(0, 1))


if __name__ == '__main__':
    unittest.main()
