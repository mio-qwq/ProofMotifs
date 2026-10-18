import unittest
from itertools import product

from tools.cancellation import Field
from tools.nonadditive_preservers import (
    cancellation_label,
    hypergraph_automorphisms,
    semilinear_quotient_actions,
    sign_flip_map,
    square_hypergraph,
)


class NonadditivePreserverTests(unittest.TestCase):
    def test_f9_empty_quotient_hypergraph(self):
        f = Field(3, (1, 0, 1))
        vertices, edges = square_hypergraph(f)
        self.assertEqual((len(vertices), len(edges)), (4, 0))
        self.assertEqual(len(hypergraph_automorphisms(vertices, edges)), 24)
        self.assertEqual(len(semilinear_quotient_actions(f, vertices)), 8)

    def test_f27_exact_quotient_automorphisms(self):
        f = Field(3, (1, 2, 0, 1))
        vertices, edges = square_hypergraph(f)
        automorphisms = hypergraph_automorphisms(vertices, edges)
        self.assertEqual((len(vertices), len(edges)), (13, 13))
        self.assertEqual({sum(v in e for e in edges) for v in vertices}, {3})
        self.assertEqual(automorphisms, semilinear_quotient_actions(f, vertices))
        self.assertEqual(len(automorphisms), 39)

    def test_f81_exact_quotient_automorphisms(self):
        f = Field(3, (2, 0, 1, 0, 1))
        vertices, edges = square_hypergraph(f)
        automorphisms = hypergraph_automorphisms(vertices, edges)
        self.assertEqual((len(vertices), len(edges)), (40, 120))
        self.assertEqual({sum(v in e for e in edges) for v in vertices}, {9})
        self.assertEqual(automorphisms, semilinear_quotient_actions(f, vertices))
        self.assertEqual(len(automorphisms), 160)

    def test_independent_sign_flip_is_nonadditive_preserver(self):
        f = Field(3, (1, 2, 0, 1))
        t = sign_flip_map(f)
        self.assertEqual(len(set(t)), 27)
        for a, b, c in product(range(27), repeat=3):
            self.assertEqual(cancellation_label(f, a, b, c),
                             cancellation_label(f, t[a], t[b], t[c]))
        alpha = 3
        self.assertNotEqual(t[f.add[1][alpha]], f.add[t[1]][t[alpha]])

    def test_edge_count_formula(self):
        for f in (Field(3, (1, 0, 1)), Field(3, (1, 2, 0, 1)),
                  Field(3, (2, 0, 1, 0, 1))):
            vertices, edges = square_hypergraph(f)
            eta = 1 if f.degree % 2 == 0 else -1
            degree = (f.q - 6 - 3 * eta) // 8
            self.assertEqual(len(edges), (f.q - 1) * (f.q - 6 - 3 * eta) // 48)
            self.assertEqual({sum(v in e for e in edges) for v in vertices}, {degree})


if __name__ == "__main__":
    unittest.main()
