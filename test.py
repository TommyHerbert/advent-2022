import unittest, advent1, advent2


class TestStringMethods(unittest.TestCase):
    def test_1a_example(self):
        self.assertEqual(advent1.solve_part_a('input/example1.txt'), 24000)

    def test_1a_input(self):
        self.assertEqual(advent1.solve_part_a('input/input1.txt'), 66306)

    def test_1b_example(self):
        self.assertEqual(advent1.solve_part_b('input/example1.txt'), 45000)

    def test_1b_input(self):
        self.assertEqual(advent1.solve_part_b('input/input1.txt'), 195292)

    def test_2a_example(self):
        self.assertEqual(advent2.solve_part_a('input/example2.txt'), 15)

    def test_2a_input(self):
        self.assertEqual(advent2.solve_part_a('input/input2.txt'), 15422)

    def test_2b_example(self):
        self.assertEqual(advent2.solve_part_b('input/example2.txt'), 12)

    def test_2b_input(self):
        pass # TODO
        #self.assertEqual(advent2.solve_part_b('input/input2.txt'), XXX)


if __name__ == '__main__':
    unittest.main()

