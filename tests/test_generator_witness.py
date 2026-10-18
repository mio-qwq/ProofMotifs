import unittest
from tools.cancellation import Field,order
from tools.order_preservers import additive_map
from tools.ternary_differences import subset_weight
from tools.constructive_witness import verify_witness
from tools.generator_witness import (
    construct_generator_witness,generator_test_pairs,
    scan_normalized_generators,selected_generator_maps,
    annihilator_transvection,scan_one_query_adversaries,nongenerator_counterexample)


class GeneratorWitnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.f3 = Field(3,(0,1))
        cls.f9 = Field(3,(1,0,1))
        cls.f27 = Field(3,(1,2,0,1))
        cls.f81u = Field(3,(2,0,1,0,1))
        cls.f81plus = Field(3,(2,1,2,2,1))
        cls.f243 = Field(3,(1,2,0,0,0,1))

    def test_every_normalized_field27_map(self):
        report = scan_normalized_generators(self.f27)
        self.assertEqual(report['normalized_bijections'],432)
        self.assertEqual(report['statuses'],
                         {'semilinear':3,'exceptional_preserver':0,'witness':429})
        self.assertLessEqual(report['maximum_defect_queries'],3)

    def test_generator_square_alone_does_not_suffice(self):
        f = self.f27
        columns = (1,9,15)
        result = construct_generator_witness(f,columns)
        self.assertEqual(result['query_log'][0]['parameter'],3)
        self.assertEqual(result['query_log'][0]['defect'],0)
        self.assertEqual(result['status'],'witness')
        self.assertGreater(result['defect_query_count'],1)
        verified = verify_witness(f,columns,result)
        self.assertEqual((verified['before_order'],verified['after_order']),(7,5))

    def test_all_adaptive_branches_are_admissible(self):
        observed = set()
        for f in (self.f27,self.f81u,self.f81plus,self.f243):
            for pair in generator_test_pairs(f):
                observed.add(pair['branch'])
                for parameter in pair['parameters']:
                    self.assertNotEqual(f.pow(parameter,9),parameter)
        self.assertEqual(observed,{'ordinary','u_in_F9','alpha_plus_u_in_F9'})
        self.assertEqual(generator_test_pairs(self.f81u)[0]['branch'],'u_in_F9')
        self.assertEqual(generator_test_pairs(self.f81plus)[0]['branch'],'alpha_plus_u_in_F9')

    def test_selected_field81_and_field243_maps(self):
        for f,expected in ((self.f81u,18),(self.f81plus,18),(self.f243,32)):
            records = selected_generator_maps(f)
            self.assertEqual(len(records),expected)
            for record in records:
                self.assertEqual(record['verified_orders'],[7,5])
                self.assertEqual(record['complete_moments_per_side'],f.q)
                result = record['extraction']
                self.assertLessEqual(result['defect_query_count'],2*f.degree-3)
                self.assertTrue(all(f.pow(x['parameter'],9)!=x['parameter']
                                    for x in result['query_log']))

    def test_scaled_frobenius_controls_reach_full_linear_bound(self):
        for f in (self.f3,self.f9,self.f27,self.f81u,self.f81plus,self.f243):
            for scale in (1,2,f.q-1):
                for exponent in range(f.degree):
                    columns = tuple(f.mul[scale][f.pow(f.p**i,f.p**exponent)]
                                    for i in range(f.degree))
                    r = construct_generator_witness(f,columns)
                    self.assertEqual(r['status'],'semilinear')
                    self.assertEqual(r['semilinear_exponent'],exponent)
                    self.assertEqual(r['defect_query_count'],max(0,2*f.degree-3))

    def test_field9_exception(self):
        f = self.f9
        counts = {'semilinear':0,'exceptional_preserver':0}
        for b in range(3,9):
            columns = (1,b)
            r = construct_generator_witness(f,columns)
            counts[r['status']] += 1
            if r['status']=='exceptional_preserver':
                self.assertTrue(r['query_log'][0]['defect'])
            values = additive_map(f,columns)
            for a in range(9):
                for b in range(9):
                    for c in range(9):
                        source,target = (a,b,c),(values[a],values[b],values[c])
                        self.assertEqual(order(f.moments(subset_weight(f,source))),
                                         order(f.moments(subset_weight(f,target))))
        self.assertEqual(counts,{'semilinear':2,'exceptional_preserver':4})

    def test_nontrivial_scaling_keeps_query_parameters(self):
        f = self.f27
        columns = (1,9,15)
        initial = construct_generator_witness(f,columns)
        for scale in range(1,f.q):
            scaled = tuple(f.mul[scale][x] for x in columns)
            r = construct_generator_witness(f,scaled)
            self.assertEqual(r['parameter'],initial['parameter'])
            self.assertEqual([v['parameter'] for v in r['query_log']],
                             [v['parameter'] for v in initial['query_log']])
            verify_witness(f,scaled,r)

    def test_query_accounting_and_verification_are_separate(self):
        f = self.f81u
        columns = (1,4,16,27)
        r = construct_generator_witness(f,columns)
        before = dict(r)
        self.assertEqual(r['defect_query_count'],len(r['query_log']))
        self.assertLessEqual(r['map_oracle_calls_extraction'],1+2*r['defect_query_count'])
        self.assertGreaterEqual(r['map_oracle_calls_including_images'],r['map_oracle_calls_extraction'])
        verify_witness(f,columns,r)
        self.assertEqual(r,before)

    def test_every_field81_one_query_transcript_has_an_adversary(self):
        report = scan_one_query_adversaries(self.f81u)
        self.assertEqual(report['single_query_transcripts'],81)
        self.assertEqual(report['verified_nonsemilinear_adversaries'],81)
        self.assertGreater(report['distinct_map_count'],0)
        self.assertLessEqual(report['distinct_map_count'],81)
        self.assertLessEqual(report['maximum_extractor_defect_queries'],5)
        self.assertEqual(sum(report['transcript_span_dimension_histogram'].values()),81)

    def test_adversary_functional_and_full_span_boundary(self):
        f = self.f81u
        adversary = annihilator_transvection(f,(3,))
        self.assertEqual(adversary['queried_defects'],[0])
        self.assertEqual(adversary['fixed_space_dimension'],3)
        values = additive_map(f,tuple(adversary['columns']))
        self.assertEqual(sum(values[x]==x for x in range(f.q)),27)
        self.assertEqual(values[1],1)
        self.assertEqual(len(set(values)),81)
        self.assertIsNone(annihilator_transvection(f,(3,9,27)))

    def test_nongenerator_intertwiner_is_insufficient(self):
        report = nongenerator_counterexample(self.f81u)
        self.assertEqual(report['nongenerator'],11)
        self.assertEqual(report['nongenerator_subfield_size'],9)
        self.assertEqual(report['multiplication_intertwiner_defects'],[0]*81)
        self.assertEqual(report['generator_square_defect'],5)
        self.assertEqual(report['extraction']['status'],'witness')
        self.assertEqual((report['verification']['before_order'],
                          report['verification']['after_order']),(7,5))

    def test_invalid_inputs(self):
        for columns in ((1,), (1,3,27), (0,3,9), (1,3,3)):
            with self.assertRaises(ValueError):
                construct_generator_witness(self.f27,columns)
        with self.assertRaises(ValueError):
            construct_generator_witness(Field(2,(0,1)),(1,))
        with self.assertRaises(ValueError):
            generator_test_pairs(self.f9)
        with self.assertRaises(ValueError):
            scan_normalized_generators(self.f81u)
        with self.assertRaises(ValueError):
            annihilator_transvection(self.f9,(3,))
        with self.assertRaises(ValueError):
            annihilator_transvection(self.f81u,(81,))
        with self.assertRaises(ValueError):
            scan_one_query_adversaries(self.f27)


if __name__=='__main__':
    unittest.main()
