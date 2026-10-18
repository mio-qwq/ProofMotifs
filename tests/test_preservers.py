import unittest
from tools.cancellation import Field, order
from tools.ternary_differences import subset_weight
from tools.order_preservers import additive_map, scan_preservers, parameter_identity_check


class PreserverTests(unittest.TestCase):
    def test_exceptional_field9(self):
        r=scan_preservers(Field(3,(1,0,1)))
        self.assertEqual((r['normalized_bijections'],r['normalized_preservers']),(6,6))
        self.assertEqual(r['full_preserver_count'],48)
        self.assertEqual(len(r['normalized_frobenius_columns']),2)

    def test_field27_rejection(self):
        f=Field(3,(1,2,0,1)); t=additive_map(f,(1,3,10)); a=(1,3,15)
        self.assertEqual(len(set(t)),27)
        self.assertEqual(order(f.moments(subset_weight(f,a))),7)
        self.assertEqual(order(f.moments(subset_weight(f,tuple(t[x] for x in a)))),5)

    def test_field27_log_multiplication(self):
        # Second multiplication algorithm: use alpha^3=alpha+2 to generate
        # the cyclic table, then add discrete exponents. No polynomial division.
        f=Field(3,(1,2,0,1)); powers=[]; value=(1,0,0)
        for _ in range(26):
            powers.append(value)
            u,v,w=value
            value=((2*w)%3,(u+w)%3,v)
        self.assertEqual(value,(1,0,0))
        self.assertEqual(len(set(powers)),26)
        encode=lambda t: t[0]+3*t[1]+9*t[2]
        antilog=[encode(t) for t in powers]
        logs={x:i for i,x in enumerate(antilog)}
        for a in range(27):
            for b in range(27):
                expected=0 if not a or not b else antilog[(logs[a]+logs[b])%26]
                self.assertEqual(f.mul[a][b],expected)

    def test_parameter_identity(self):
        self.assertEqual(parameter_identity_check(Field(3,(1,0,1)))['identity_instances'],729)

    def test_invalid_columns(self):
        f=Field(3,(1,0,1))
        with self.assertRaises(ValueError): additive_map(f,(1,))
        with self.assertRaises(ValueError): additive_map(f,(1,9))
        with self.assertRaises(ValueError): scan_preservers(Field(2,(0,1)))

    def test_even_extension81_rejection(self):
        f=Field(3,(2,1,0,0,1)); t=additive_map(f,(1,3,9,28))
        self.assertEqual(len(set(t)),81)
        found=False
        for x in range(81):
            xx=f.mul[x][x]
            a=f.add[f.add[1][f.neg[xx]]][x]
            b=f.add[f.add[1][f.neg[xx]]][f.neg[x]]
            c=f.neg[f.add[1][xx]]
            if a and b and c:
                before=order(f.moments(subset_weight(f,(a,b,c))))
                after=order(f.moments(subset_weight(f,(t[a],t[b],t[c]))))
                if before != after:
                    self.assertEqual((before,after),(7,5)); found=True; break
        self.assertTrue(found)


if __name__=='__main__': unittest.main()
