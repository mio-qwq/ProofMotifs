import copy
from fractions import Fraction as Q
from itertools import product
import unittest

from tools import acyclic_jet as aj


# Independent rational-polynomial arithmetic, not the production jet routines.
def pt(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pa(a, b):
    return pt([(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
               for i in range(max(len(a), len(b)))])


def pm(a, b):
    return pt([sum((a[j]*b[k-j] for j in range(len(a)) if 0 <= k-j < len(b)), Q(0))
               for k in range(len(a)+len(b)-1)])


def ra(a, b):
    return pa(pm(a[0], b[1]), pm(b[0], a[1])), pm(a[1], b[1])


def rm(a, b):
    return pm(a[0], b[0]), pm(a[1], b[1])


ZERO, ONE = ([Q(0)], [Q(1)]), ([Q(1)], [Q(1)])


def matmul(a, b, add, multiply, zero):
    m = len(a)
    out = [[zero for _ in range(m)] for _ in range(m)]
    for u in range(m):
        for v in range(m):
            for k in range(m):
                out[u][v] = add(out[u][v], multiply(a[u][k], b[k][v]))
    return out


def rational_tuple(instance):
    m, n = instance['vertices'], instance['variables']
    out = [[[ZERO for _ in range(m)] for _ in range(m)] for _ in range(n)]
    for e in instance['edges']:
        d = [Q(1)]
        for q, k in zip(instance['denominators'], e['exp']):
            for _ in range(k):
                d = pm(d, list(map(Q, q)))
        v = (list(map(Q, e['num'])), d)
        out[e['var']][e['src']][e['dst']] = ra(out[e['var']][e['src']][e['dst']], v)
    return out


class AcyclicJetTests(unittest.TestCase):
    def instance(self):
        return {'p': 0, 'vertices': 3, 'variables': 2,
                # Deliberately noncoprime/repeated factors; still a valid bound.
                'denominators': [[1, -1], [1, -2, 1]],
                'edges': [{'src': 0, 'dst': 1, 'var': 0, 'num': [0, 1], 'exp': [1, 0]},
                          {'src': 1, 'dst': 2, 'var': 1, 'num': [1, 2], 'exp': [0, 1]},
                          {'src': 0, 'dst': 2, 'var': 1, 'num': [1, 0, 1], 'exp': [1, 0]}]}

    def test_longest_paths_signed_costs_and_empty(self):
        cert = aj.analyze(self.instance())
        self.assertEqual(cert['max_exponents'], [1, 1])
        self.assertEqual(cert['denominator_degree'], 3)
        self.assertEqual(cert['max_degree_excess'], 1)
        self.assertEqual(cert['jet_length'], 5)
        aj.verify_bound(self.instance(), cert)
        bad = dict(cert, jet_length=4)
        with self.assertRaises(ValueError):
            aj.verify_bound(self.instance(), bad)

    def test_rational_full_word_crosscheck(self):
        inst = self.instance()
        cert, compiled = aj.compile_tuple(inst)
        vs = rational_tuple(inst)
        m, length = inst['vertices'], cert['jet_length']
        checked = 0
        for degree in range(4):
            for w in product(range(2), repeat=degree):
                original = [[ONE if u == v else ZERO for v in range(m)] for u in range(m)]
                dense = [[Q(int(u == v)) for v in range(m*length)] for u in range(m*length)]
                for a in w:
                    original = matmul(original, vs[a], ra, rm, ZERO)
                    dense = matmul(dense, compiled[a], lambda x, y: x+y, lambda x, y: x*y, Q(0))
                nonzero = False
                for u in range(m):
                    for v in range(m):
                        num, den = original[u][v]
                        coeffs = [dense[u*length+k][v*length] for k in range(length)]
                        # denominator * computed series = independent numerator mod t^E
                        residue = pm(den, coeffs)
                        self.assertEqual((residue+[0]*length)[:length], (num+[0]*length)[:length])
                        nonzero |= any(num)
                self.assertEqual(any(any(row) for row in dense), nonzero)
                checked += 1
        self.assertEqual(checked, 15)

    def test_delayed_cancellation_and_insufficient_jet(self):
        # x-y evaluates to t/(1-t) E_01, so E=1 loses a genuine nonzero.
        inst = {'p': 0, 'vertices': 2, 'variables': 2, 'denominators': [[1, -1]],
                'edges': [{'src': 0, 'dst': 1, 'var': 0, 'num': [1], 'exp': [1]},
                          {'src': 0, 'dst': 1, 'var': 1, 'num': [1], 'exp': [0]}]}
        cert, ts = aj.compile_tuple(inst)
        self.assertEqual(cert['jet_length'], 2)
        self.assertTrue(any(x-y for a, b in zip(ts[0], ts[1]) for x, y in zip(a, b)))
        short = aj.entry_jets(inst, 1)
        self.assertEqual(short[0], short[1])

    def test_prime_field_and_characteristic_cancellation(self):
        self.assertEqual(aj.scalar(Q(1, 2), 3), 2)
        with self.assertRaises(ValueError):
            aj.scalar(Q(1, 2), 2)
        with self.assertRaises(ValueError):
            aj.scalar(0.5, 3)
        for p in (2, 3, 5, 7):
            inst = self.instance()
            inst['p'] = p
            cert, ts = aj.compile_tuple(inst)
            for q in inst['denominators']:
                inv = aj.inverse_jet(q, cert['jet_length'], p)
                result = pm(list(map(Q, q)), list(map(Q, inv)))
                self.assertEqual([int(x) % p for x in (result+[0]*cert['jet_length'])[:cert['jet_length']]],
                                 [1]+[0]*(cert['jet_length']-1))
            self.assertTrue(all(0 <= x < p for t in ts for row in t for x in row))
        inst = {'p': 0, 'vertices': 2, 'variables': 1, 'denominators': [],
                'edges': [{'src': 0, 'dst': 1, 'var': 0, 'num': [2], 'exp': []}]}
        self.assertEqual(aj.analyze(inst)['nonzero_edges'], 1)
        inst['p'] = 2
        self.assertEqual(aj.analyze(inst)['nonzero_edges'], 0)

    def test_reject_cycles_poles_and_malformed_exponents(self):
        cases = []
        for key, value in [('src', 2), ('dst', 0), ('exp', [-1, 0]), ('exp', [0])]:
            inst = self.instance()
            inst['edges'][0][key] = value
            cases.append(inst)
        inst = self.instance()
        inst['vertices'] = 3.0
        cases.append(inst)
        inst = self.instance()
        inst['edges'][0]['src'] = 0.0
        cases.append(inst)
        inst = self.instance()
        inst['denominators'][0] = [0, 1]
        cases.append(inst)
        for inst in cases:
            with self.assertRaises(ValueError):
                aj.analyze(inst)

    def test_parametric_bound_not_minimality_claim(self):
        panels = aj.demo()['panels']
        for row in panels:
            h = row['h']
            self.assertEqual(row['path_aware_jet_bound'], h+1)
            self.assertEqual(row['naive_repeated_global_denominator_bound'], h*h+1)
            self.assertEqual(row['paths_0_to_h'], 2**(h-1))


if __name__ == '__main__':
    unittest.main()
