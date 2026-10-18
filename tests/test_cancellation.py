import unittest
from fractions import Fraction
from itertools import product
from math import comb
from tools.cancellation import Field, order, carry_free, standard_fields


class ExactCancellationTests(unittest.TestCase):
    def test_bad_parameters(self):
        for p, modulus in [(4,(0,1)), (2,(1,)), (2,(1,0,1)), (3,(0,0,1))]:
            with self.assertRaises(ValueError): Field(p, modulus)
        f=Field(2,(0,1))
        with self.assertRaises(ValueError): f.weights([0])
        with self.assertRaises(ValueError): f.weights([0,2])
        with self.assertRaises(ValueError): f.pow(1,-1)
        with self.assertRaises(ValueError): carry_free(0,1,4)

    def test_field_axioms(self):
        for f in standard_fields():
            for a in range(f.q):
                self.assertEqual(f.add[a][f.neg[a]],0)
                self.assertEqual(f.mul[a][1],a)
                self.assertEqual(f.pow(a,f.q),a)
                if a: self.assertEqual(f.pow(a,f.q-1),1)
            for a,b,c in product(range(f.q),repeat=3):
                self.assertEqual(f.add[a][f.add[b][c]], f.add[f.add[a][b]][c])
                self.assertEqual(f.mul[a][f.mul[b][c]], f.mul[f.mul[a][b]][c])
                self.assertEqual(f.mul[a][f.add[b][c]], f.add[f.mul[a][b]][f.mul[a][c]])

    def test_moment_map_injective(self):
        for f in standard_fields()[:3]:
            vectors=list(product(range(f.q),repeat=f.q))
            self.assertEqual(len({f.moments(v) for v in vectors}),len(vectors))

    def test_rational_characteristic_zero(self):
        nodes=(-1,0,1)
        for u,v in product(product((-1,0,1),repeat=3), repeat=2):
            if not any(u) or not any(v): continue
            a=[sum(Fraction(w)*x**n for w,x in zip(u,nodes)) for n in range(5)]
            b=[sum(Fraction(w)*x**n for w,x in zip(v,nodes)) for n in range(5)]
            c=[sum(Fraction(u[i]*v[j])*(x+y)**n for i,x in enumerate(nodes)
                   for j,y in enumerate(nodes)) for n in range(5)]
            for n in range(5):
                self.assertEqual(c[n],sum(comb(n,i)*a[i]*b[n-i] for i in range(n+1)))
            self.assertEqual(order(c),order(a)+order(b))

    def test_characteristic_two_annihilation(self):
        f=Field(2,(0,1));d=f.difference(1)
        self.assertEqual(order(f.moments(d)),1)
        self.assertEqual(f.convolution(d,d),(0,0))

    def test_finite_order_jump(self):
        f=Field(2,(1,1,1));a,b=f.difference(1),f.difference(2)
        self.assertEqual((order(f.moments(a)),order(f.moments(b))),(1,1))
        self.assertEqual(f.moments(f.convolution(a,b)),(0,0,0,1))
        self.assertEqual(f.convolution(a,a),(0,0,0,0))

    def test_odd_characteristic_jump(self):
        f=Field(3,(1,0,1));mu=f.saturated([1,3])
        self.assertEqual(mu,(1,)*9)
        self.assertEqual(order(f.moments(mu)),8)
        self.assertEqual(order(f.moments(f.saturated([1]))),2)
        self.assertEqual(f.saturated([1,2]),(0,)*9)

    def test_zero_and_empty_directions(self):
        for f in standard_fields():
            self.assertEqual(f.saturated([]), f.delta(0))
            self.assertEqual(order(f.moments(f.saturated([]))),0)
            self.assertEqual(f.saturated([0]),(0,)*f.q)
            self.assertEqual(f.derivative_constant({0}),1)
            self.assertEqual(f.moore_det([]),1)

    def test_no_carry(self):
        for p in (2,3,5):
            for a,b in product(range(30),repeat=2):
                self.assertEqual(carry_free(a,b,p),comb(a+b,a)%p != 0)

    def test_missing_analytic_hypothesis(self):
        # Constant F=1 has Lipschitz constant zero. Without zero mass,
        # L(F)=1 while the proposed cancellation bound would be zero.
        value=Fraction(1); claimed_bound=Fraction(0)
        self.assertGreater(value,claimed_bound)


if __name__ == '__main__': unittest.main()
