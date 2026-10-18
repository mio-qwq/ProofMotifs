from copy import deepcopy
import unittest
from tools import q_polynomial_obstruction as qp


class PolynomialObstructionTests(unittest.TestCase):
    def test_all_input_symbolic_identity_not_sampled(self):
        seeds = [[0, 1], [0, 0, 1]]
        self.assertTrue(qp.verify_identity(seeds, [((1, 0), 1), ((0, 1), -2), ((0, 0, 0), -1)])[0])
        self.assertTrue(qp.verify_identity(seeds, [((0, 0, 1), 2), ((0, 1, 0), -3), ((1, 0, 0), 1)])[0])

    def test_generic_polynomial_size_word_budget(self):
        for seeds in ([[0, 1], [0, 0, 1]], [[0, 1, 1], [0, 2, -1]]):
            cert = qp.construct(seeds)
            self.assertLessEqual(cert['words_examined'], cert['coordinate_bound']+1)
            self.assertTrue(qp.verify_identity(seeds, cert['terms'])[0])
            bad = deepcopy(cert['terms'])
            bad[0] = (bad[0][0], bad[0][1]+1)
            self.assertFalse(qp.verify_identity(seeds, bad)[0])

    def test_down_up_shaped_does_not_supply_other_relation(self):
        seeds = [[0, 1], [0, 0, 1]]
        wrong = [((1, 1, 0), 1), ((1, 0, 1), -3), ((0, 1, 1), 2)]
        self.assertFalse(qp.verify_identity(seeds, wrong)[0])

    def test_zero_letter_and_contract_validation(self):
        cert = qp.construct([[0], [0, 1]])
        self.assertTrue(qp.verify_identity([[0], [0, 1]], cert['terms'])[0])
        with self.assertRaises(ValueError):
            qp.construct([[0, 1]])
        with self.assertRaises(ValueError):
            qp.construct([[1, 1], [0, 1]])
        self.assertFalse(qp.verify_identity([[0, 1], [0, 2]], [((0,), 0)])[0])


if __name__ == '__main__':
    unittest.main()
