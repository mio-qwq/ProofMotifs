import unittest
from itertools import product
from tools.cancellation import Field,order
from tools.ternary_differences import subset_weight,invariants,predicted_order,symbolic_moments


class TernaryTests(unittest.TestCase):
    def test_symbolic(self):
        self.assertEqual(len(symbolic_moments()[5]),3)

    def test_field27_axioms(self):
        f=Field(3,(1,2,0,1))
        for a,b,c in product(range(27),repeat=3):
            self.assertEqual(f.mul[a][f.mul[b][c]],f.mul[f.mul[a][b]][c])
            self.assertEqual(f.mul[a][f.add[b][c]],f.add[f.mul[a][b]][f.mul[a][c]])
        for a in range(27):
            self.assertEqual(f.pow(a,27),a)
            if a: self.assertEqual(f.pow(a,26),1)

    def test_rank_three_counterexample(self):
        f=Field(3,(1,2,0,1))
        for directions,expected in [((1,3,9),5),((1,3,15),7)]:
            self.assertEqual(len(f.span(directions)),27)
            self.assertEqual(order(f.moments(subset_weight(f,directions))),expected)
            self.assertEqual(predicted_order(*invariants(f,*directions)),expected)

    def test_degenerate_cases(self):
        f=Field(3,(1,2,0,1))
        for a in range(27):
            self.assertFalse(any(subset_weight(f,(a,a,a))))
            self.assertFalse(any(subset_weight(f,(a,a,f.neg[a]))))
            self.assertFalse(any(subset_weight(f,(0,a,1))))
        with self.assertRaises(ValueError): invariants(Field(2,(0,1)),1,1,1)


if __name__=='__main__': unittest.main()
