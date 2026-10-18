import unittest
from tools import resolvent_certificate as r


class ResolventCertificateTests(unittest.TestCase):
    def test_universal_identity(self):
        self.assertTrue(r.verify_identity(r.build()))
        self.assertTrue(r.build()['P'])

    def test_json_encoding(self):
        import json
        rows = json.loads(json.dumps({k: r.encode(v) for k, v in r.build().items()}))
        self.assertTrue(r.verify_identity({k: r.decode(v) for k, v in rows.items()}))

    def test_corruption(self):
        d = r.build()
        d['P'] = r.add(d['P'], r.variable('AB'))
        self.assertFalse(r.verify_identity(d))

    def test_characteristic_and_zero_parameter(self):
        for p in [0, 2, 3, 5]:
            for c in [None, 0, 1, -2]:
                d = {k: r.specialization(v, c=c, characteristic=p) for k, v in r.build().items()}
                self.assertTrue(r.verify_identity(d, characteristic=p))
                self.assertTrue(d['P'])  # AB coefficient1 survives every allowed p.

    def test_parser_boundary(self):
        for row in [dict(q_degree=-1, c_degree=0, word='A', integer=1),
                    dict(q_degree=0, c_degree=False, word='A', integer=1),
                    dict(q_degree=0, c_degree=0, word='X', integer=1)]:
            with self.assertRaises(ValueError):
                r.decode([row])

    def test_no_unit_inference(self):
        # Concrete scalar counterexample: R0=R1=0 and P*S=0, but P is nonzero.
        q, c, A, B, Z = 2, 1, 0, 1, 1
        S = 1-c*Z
        self.assertEqual(Z*A-q*A*Z-(q-1)*A*A, 0)
        self.assertEqual(B*S-A, 0)
        self.assertEqual(A*B-q*B*A+(q-1)*B*B+c*(q-1)*B*A*B, 1)
        self.assertEqual(S, 0)


if __name__ == '__main__':
    unittest.main()
