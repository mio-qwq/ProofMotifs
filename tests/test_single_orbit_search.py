import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import single_orbit_search as s


class SingleOrbitSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = s.build_report()
        cls.receipt = s.verify_report(cls.report)

    def test_bounded_positive_certificates(self):
        rows = self.receipt['bounded_degrees']
        self.assertEqual([row['m'] for row in rows], [3, 4, 5, 6, 7, 8])
        self.assertEqual([row['good_seed']['gcd_degree'] for row in rows], [4, 5, 6, 7, 8, 9])
        self.assertFalse(self.receipt['universal_existence_claim'])
        self.assertEqual([row['complete_orbit_scan'] for row in rows], [True] * 4 + [False] * 2)

    def test_complete_degree_six_classification(self):
        row = self.receipt['bounded_degrees'][3]
        self.assertEqual(row['tested_orbits'], 30)
        self.assertEqual(row['index_nullity_counts'],
                         [[1, 7, 18], [1, 13, 3], [2, 14, 3],
                          [4, 40, 2], [14, 56, 3], [28, 112, 1]])
        # q729 graph has 30 full-size square-multiplication orbits.
        self.assertEqual(30 * row['N'], 10920)

    def test_connected_counterexample_and_trace_separator(self):
        bad = self.receipt['connected_bad_seed']
        self.assertEqual((bad['connectivity_index'], bad['gcd_degree']), (1, 13))
        self.assertEqual(bad['root_exponents'],
                         [0, 1, 3, 9, 27, 34, 81, 102, 190, 206, 243, 254, 306])
        witness = self.report['nonlinear_trace_witness']
        self.assertEqual(witness['seed_translate_violations'], [])
        self.assertEqual([witness['values'][e] for e in witness['full_edge']], [0, 0, 1])

    def test_existing_degree_four_disconnected_control(self):
        rows = self.receipt['bounded_degrees'][1]['index_nullity_counts']
        self.assertEqual(rows, [[1, 5, 2], [5, 15, 1]])

    def test_reject_corrupted_bezout(self):
        certificate = copy.deepcopy(self.report['connected_bad_certificate'])
        certificate['bezout_seed'][0] = (certificate['bezout_seed'][0] + 1) % 3
        with self.assertRaisesRegex(ValueError, 'Bezout'):
            s.verify_seed_certificate(s.CompactField(6), certificate)

    def test_reject_corrupted_gcd(self):
        certificate = copy.deepcopy(self.report['connected_bad_certificate'])
        certificate['gcd'][0] = (certificate['gcd'][0] + 1) % 3
        with self.assertRaisesRegex(ValueError, 'divisibility'):
            s.verify_seed_certificate(s.CompactField(6), certificate)

    def test_reject_corrupted_divisibility(self):
        certificate = copy.deepcopy(self.report['fields'][3]['good_seed_certificate'])
        certificate['quotient_h'][0] = (certificate['quotient_h'][0] + 1) % 3
        with self.assertRaisesRegex(ValueError, 'divisibility'):
            s.verify_seed_certificate(s.CompactField(6), certificate)

    def test_reject_orbit_scan_omission(self):
        report = copy.deepcopy(self.report)
        report['fields'][3]['orbits'].pop()
        with self.assertRaisesRegex(ValueError, 'omits an orbit'):
            s.verify_report(report)

    def test_reject_forged_completeness_flag(self):
        report = copy.deepcopy(self.report)
        report['fields'][4]['complete_orbit_scan'] = True
        with self.assertRaisesRegex(ValueError, 'completeness flag'):
            s.verify_report(report)

    def test_reject_forged_gcd_degree(self):
        report = copy.deepcopy(self.report)
        report['fields'][3]['orbits'][0]['gcd_degree'] += 1
        with self.assertRaisesRegex(ValueError, 'root-count mismatch'):
            s.verify_report(report)

    def test_reject_forged_connectivity(self):
        report = copy.deepcopy(self.report)
        report['fields'][3]['orbits'][0]['connectivity_index'] = 1
        with self.assertRaisesRegex(ValueError, 'connectivity index'):
            s.verify_report(report)

    def test_reject_forged_trace_witness(self):
        report = copy.deepcopy(self.report)
        report['nonlinear_trace_witness']['values'][255] = 0
        with self.assertRaisesRegex(ValueError, 'trace witness mismatch'):
            s.verify_report(report)

    def test_reject_nonprimitive_field_modulus(self):
        with self.assertRaisesRegex(ValueError, 'cycle'):
            s.CompactField(6, [2, 0, 0, 0, 0, 0, 1])


if __name__ == '__main__':
    unittest.main()
