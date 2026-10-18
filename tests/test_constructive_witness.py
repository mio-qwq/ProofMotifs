import unittest
from itertools import product
from tools.cancellation import Field, order
from tools.order_preservers import additive_map
from tools.ternary_differences import subset_weight
from tools.constructive_witness import (
    construct_witness, verify_witness, conic_directions, scan_normalized,
    selected_transvections)


class ConstructiveWitnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.f3 = Field(3, (0,1))
        cls.f9 = Field(3, (1,0,1))
        cls.f27 = Field(3, (1,2,0,1))
        cls.f81 = Field(3, (2,0,1,0,1))

    def test_all_normalized_field27_bijections(self):
        report = scan_normalized(self.f27)
        self.assertEqual(report['normalized_bijections'], 432)
        self.assertEqual(report['statuses'],
                         {'semilinear': 3, 'exceptional_preserver': 0, 'witness': 429})
        self.assertLessEqual(report['maximum_defect_queries'], 3)
        self.assertEqual(report['repairs'], 0)

    def test_all_field9_exceptions_really_preserve(self):
        f = self.f9
        counts = {'semilinear': 0, 'exceptional_preserver': 0}
        labels = {a: order(f.moments(subset_weight(f, a)))
                  for a in product(range(f.q), repeat=3)}
        for b in range(3,9):
            columns = (1,b)
            result = construct_witness(f, columns)
            counts[result['status']] += 1
            values = additive_map(f, columns)
            for triple, before in labels.items():
                self.assertEqual(before, labels[tuple(values[x] for x in triple)])
            if result['status'] == 'exceptional_preserver':
                self.assertTrue(result['query_log'][0]['defect'])
                self.assertFalse(all(conic_directions(f, result['initial_parameter'])))
        self.assertEqual(counts, {'semilinear': 2, 'exceptional_preserver': 4})

    def test_even_extension_repairs_degenerate_parameter(self):
        f = self.f81
        columns = (1,4,16,27)
        result = construct_witness(f, columns)
        self.assertEqual(result['status'], 'witness')
        self.assertTrue(result['repair_used'])
        self.assertEqual(result['initial_parameter'], 9)
        self.assertFalse(all(conic_directions(f, 9)))
        self.assertEqual(f.pow(9,9),9)
        self.assertNotEqual(f.pow(result['parameter'],9),result['parameter'])
        self.assertLessEqual(result['defect_query_count'], 9)
        verification = verify_witness(f, columns, result)
        self.assertEqual((verification['before_order'],verification['after_order']),(7,5))
        self.assertEqual(verification['complete_moments_per_side'],81)

    def test_all_scaled_frobenius_controls(self):
        for f in (self.f3,self.f9,self.f27,self.f81):
            for scale in range(1,f.q):
                for j in range(f.degree):
                    columns = tuple(f.mul[scale][f.pow(f.p**i,f.p**j)]
                                    for i in range(f.degree))
                    r = construct_witness(f,columns)
                    self.assertEqual(r['status'],'semilinear')
                    self.assertEqual(r['semilinear_exponent'],j)

    def test_selected_even_extension_transvections(self):
        records = selected_transvections(self.f81)
        self.assertEqual(len(records), 18)
        for record in records:
            self.assertEqual(record['status'],'witness')
            self.assertEqual(record['verified_orders'],[7,5])
            self.assertEqual(record['complete_moments_per_side'],81)

    def test_scaling_rejected_map_keeps_extracted_directions(self):
        f = self.f27
        columns = (1,3,10)
        initial = construct_witness(f,columns)
        for scale in range(1,f.q):
            scaled = tuple(f.mul[scale][x] for x in columns)
            r = construct_witness(f,scaled)
            self.assertEqual(r['directions'],initial['directions'])
            verify_witness(f,scaled,r)

    def test_parameter_identity_and_exact_degeneracy_set(self):
        for f in (self.f3,self.f9,self.f27,self.f81):
            for t in range(f.q):
                a,b,c = conic_directions(f,t)
                self.assertEqual(f.add[f.add[f.mul[a][a]][f.mul[b][b]]][f.mul[c][c]],0)
                self.assertEqual(not all((a,b,c)), f.pow(t,9)==t and t not in (0,1,2))

    def test_query_accounting_excludes_independent_verification(self):
        f = self.f27
        r = construct_witness(f,(1,3,10))
        self.assertEqual(r['defect_query_count'],len(r['query_log']))
        self.assertLessEqual(r['map_oracle_calls_extraction'],1+2*r['defect_query_count'])
        saved = dict(r)
        verify_witness(f,(1,3,10),r)
        self.assertEqual(r,saved)

    def test_invalid_inputs_and_status(self):
        for columns in ((1,), (1,3,27), (0,3,9), (1,3,3)):
            with self.assertRaises(ValueError):
                construct_witness(self.f27,columns)
        with self.assertRaises(ValueError):
            construct_witness(Field(2,(0,1)),(1,))
        with self.assertRaises(ValueError):
            verify_witness(self.f3,(1,),construct_witness(self.f3,(1,)))
        with self.assertRaises(ValueError):
            scan_normalized(self.f81)


if __name__ == '__main__':
    unittest.main()
