import unittest

from tools.two_subspace_obstruction import (
    add_vector, negative_vector, component_hypergraph, obstruction_report,
    enumerate_dimension_two_component)


class TwoSubspaceObstructionTests(unittest.TestCase):
    def test_dimension_two_kernel_and_explicit_nonaffine_function(self):
        report = obstruction_report(2)
        self.assertEqual((report['vertex_count'], report['edge_count']), (16, 16))
        self.assertEqual((report['incidence_rank'], report['incidence_kernel_dimension']), (10, 6))
        self.assertEqual(report['ambient_affine_dimension'], 5)
        self.assertEqual(report['nonaffine_augmented_dimension'], 6)
        self.assertEqual(report['connected_component_sizes'], [8, 8])
        self.assertEqual(report['full_automorphism_order'], 4608)
        self.assertEqual(report['scalar_frobenius_subgroup_order'], 64)

    def test_dimension_three_requires_no_field729_tables(self):
        report = obstruction_report(3)
        self.assertEqual(report['ambient_field_order'], 729)
        self.assertEqual((report['vertex_count'], report['edge_count']), (52, 208))
        self.assertEqual((report['incidence_rank'], report['incidence_kernel_dimension']), (44, 8))
        self.assertEqual(report['ambient_affine_dimension'], 7)
        self.assertEqual(report['nonaffine_augmented_dimension'], 8)
        self.assertEqual(report['connected_component_sizes'], [26, 26])
        self.assertEqual(report['component_gl_order'], 11232)
        self.assertEqual(report['full_automorphism_order'], 252315648)

    def test_full_eight_point_component_group_matches_gl(self):
        report = enumerate_dimension_two_component()
        self.assertEqual(report['all_vertex_permutations_examined'], 40320)
        self.assertEqual(report['automorphism_count'], 48)
        self.assertEqual(report['gl_action_count'], 48)

    def test_dimension_one_exception_is_empty_s4(self):
        report = obstruction_report(1)
        self.assertEqual((report['vertex_count'], report['edge_count']), (4, 0))
        self.assertEqual(report['incidence_kernel_dimension'], 4)
        self.assertEqual(report['ambient_affine_dimension'], 3)
        self.assertEqual(report['connected_component_sizes'], [1, 1, 1, 1])
        self.assertEqual(report['full_automorphism_order'], 24)
        self.assertEqual(report['scalar_frobenius_subgroup_order'], 8)

    def test_order_two_mode_is_the_extra_component_direction(self):
        for dimension in (2, 3):
            report = obstruction_report(dimension)
            s = 3**dimension
            self.assertEqual(report['order_two_mode'], [1]*(s-1)+[2]*(s-1))
            self.assertEqual(report['order_two_mode_cyclic_exponent'], s-1)
            self.assertEqual(report['extra_component_constant'],
                             [2*(1-x) % 3 for x in report['order_two_mode']])

    def test_component_edges_and_opposite_pair_boundary(self):
        vertices, edges = component_hypergraph(2)
        covered = {frozenset((a, b)) for edge in edges
                   for a in edge for b in edge if a != b}
        self.assertEqual(len(set(edges)), 8)
        for x in vertices:
            for y in vertices:
                if x != y:
                    self.assertEqual(frozenset((x, y)) in covered,
                                     y != negative_vector(x, 2))
        for a, b, c in edges:
            self.assertEqual(add_vector(add_vector(a, b, 2), c, 2), 0)

    def test_input_boundaries(self):
        for dimension in (0, -1, 1.5):
            with self.assertRaises(ValueError):
                component_hypergraph(dimension)
        with self.assertRaises(ValueError):
            obstruction_report(3, True)


if __name__ == '__main__':
    unittest.main()
