import unittest
import advent1


class TestStringMethods(unittest.TestCase):
    def test_1a(self):
        self.assertEqual(advent1.solve_part_a('input/input1.txt'), 66306)

    def test_1b(self):
        self.assertEqual(advent1.solve_part_b('input/input1.txt'), 195292)


if __name__ == '__main__':
    unittest.main()

