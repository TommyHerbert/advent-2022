import unittest, advent1, advent2


class TestStringMethods(unittest.TestCase):
    def test_1a(self):
        self.assertEqual(advent1.solve_part_a('input/input1.txt'), 66306)

    def test_1b(self):
        self.assertEqual(advent1.solve_part_b('input/input1.txt'), 195292)

    def test_2a(self):
        self.assertEqual(advent2.solve_part_a('input/example2.txt'), 15)


if __name__ == '__main__':
    unittest.main()

