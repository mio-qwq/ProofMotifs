"""Certificate rejection tests for the odd-degree sparse obstruction."""
import copy
import unittest

from tools.linearized_seed_certificate import pgcd, solve, verify_report


class LinearizedSeedCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate=solve()

    def test_complete_certificate_and_limits(self):
        receipt=verify_report(self.certificate)
        self.assertEqual(receipt['fixed_frequency_parameters'],78)
        self.assertEqual(receipt['fixed_frequency_seed_orbits'],13)
        self.assertEqual(receipt['sparse_kernel_dimension_lower_bound'],27)
        self.assertFalse(receipt['exact_sparse_kernel_dimension_claimed'])
        self.assertFalse(receipt['all_field_seed_orbits_scanned'])

    def test_rejects_reducible_field_modulus(self):
        damaged=copy.deepcopy(self.certificate)
        damaged['modulus'][0]=0
        with self.assertRaisesRegex(ValueError,'Rabin'):
            verify_report(damaged)

    def test_rejects_changed_seed_coordinate(self):
        damaged=copy.deepcopy(self.certificate)
        damaged['valid_square_seeds'][0]['a'][0]=1
        with self.assertRaisesRegex(ValueError,'ratios'):
            verify_report(damaged)

    def test_rejects_incomplete_or_duplicate_parameter_cover(self):
        for mutation in ('delete','duplicate'):
            with self.subTest(mutation=mutation):
                damaged=copy.deepcopy(self.certificate)
                if mutation=='delete':
                    damaged['valid_square_seeds'].pop()
                else:
                    damaged['valid_square_seeds'][-1]=damaged['valid_square_seeds'][0]
                with self.assertRaises(ValueError):
                    verify_report(damaged)

    def test_rejects_false_nullspace_basis(self):
        damaged=copy.deepcopy(self.certificate)
        damaged['nullspace_basis'][-1][0]=1
        with self.assertRaisesRegex(ValueError,'basis'):
            verify_report(damaged)

    def test_rejects_incomplete_prime_division_receipt(self):
        damaged=copy.deepcopy(self.certificate)
        damaged['N_prime_trial_division_bound']=891
        with self.assertRaisesRegex(ValueError,'prime bound'):
            verify_report(damaged)

    def test_repeated_frobenius_factor_keeps_multiplicity(self):
        # T6-1 is not squarefree in F3. Here 1+T+T²=(T-1)².
        self.assertEqual(pgcd([2,0,0,0,0,0,1],[1,1,1]),[1,1,1])

    def test_rejects_false_trace_witness(self):
        damaged=copy.deepcopy(self.certificate)
        damaged['trace_separator']['trace_values']=[0,0,0]
        damaged['trace_separator']['trace_sum']=0
        with self.assertRaisesRegex(ValueError,'trace separator'):
            verify_report(damaged)

    def test_rejects_forged_frequency_orbit_and_partition(self):
        for key,value in [('frequency_orbit',[1]),('fixed_frequency_orbit_count',14),
                          ('all_fixed_frequency_seed_orbits_one_frobenius_orbit',False)]:
            with self.subTest(key=key):
                damaged=copy.deepcopy(self.certificate)
                damaged[key]=value
                with self.assertRaises(ValueError):
                    verify_report(damaged)


if __name__=='__main__':
    unittest.main()
