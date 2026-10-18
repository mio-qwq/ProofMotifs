from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools'))
import dynamic_readout as D


class DynamicReadoutTests(unittest.TestCase):
    def test_mixed_and_common(self):
        out = D.demo()
        self.assertEqual(out['mixed']['factor'], [6, 1])
        self.assertEqual(out['mixed']['operation'], 'test')
        self.assertEqual(out['same']['status'], 'COMMON')
        self.assertEqual(out['same']['label'], 'nonzero')

    def test_division_is_a_guarded_test(self):
        program = [{'op': 'inv', 'a': 'x', 'dest': 'z', 'next': 1},
                   {'op': 'return', 'label': 'defined'}]
        self.assertEqual(D.execute(7, [0, -1, 1], program, {'x': [0, 1]})['factor'], [0, 1])
        with self.assertRaises(ValueError):
            D.execute(7, [0, 1], program, {'x': []})

    def test_unit_inverse_and_identity(self):
        program = [{'op': 'inv', 'a': 'x', 'dest': 'z', 'next': 1},
                   {'op': 'mul', 'a': 'z', 'b': 'x', 'dest': 'product', 'next': 2},
                   {'op': 'const', 'value': 1, 'dest': 'one', 'next': 3},
                   {'op': 'sub', 'a': 'product', 'b': 'one', 'dest': 'w', 'next': 4},
                   {'op': 'test', 'a': 'w', 'zero': 5, 'nonzero': 6},
                   {'op': 'return', 'label': 'identity'},
                   {'op': 'return', 'label': 'incorrect'}]
        out = D.execute(7, [6, 2, 1], program, {'x': [0, 1]})
        self.assertEqual(out['label'], 'identity')

    def test_mixed_extension_components(self):
        program = [{'op': 'test', 'a': 'z', 'zero': 1, 'nonzero': 2},
                   {'op': 'return', 'label': 'zero'},
                   {'op': 'return', 'label': 'nonzero'}]
        # (X-1)(X^2+1) over F3; no splitting assumption.
        out = D.execute(3, [2, 1, 2, 1], program, {'z': [2, 1]})
        self.assertEqual(out['factor'], [2, 1])

    def test_raw_field_output_and_cycles_rejected(self):
        for program in [[{'op': 'return-register', 'a': 'x'}],
                        [{'op': 'return', 'label': [0, 1]}],
                        [{'op': 'test', 'a': 'x', 'zero': 0, 'nonzero': 0}]]:
            with self.assertRaises(ValueError):
                D.execute(7, [2, 4, 1], program, {'x': [0, 1]})

    def test_invalid_register_and_nonreduced(self):
        program = [{'op': 'test', 'a': 'undefined', 'zero': 1, 'nonzero': 1},
                   {'op': 'return', 'label': 'constant'}]
        with self.assertRaises(ValueError):
            D.execute(7, [2, 4, 1], program, {'x': [0, 1]})
        with self.assertRaises(ValueError):
            D.execute(7, [0, 0, 1], [{'op': 'return', 'label': 'constant'}], {})


if __name__ == '__main__':
    unittest.main()
