import unittest, day1, day2


class TestStringMethods(unittest.TestCase):
    def test_day_1(self):
        self.assertEqual(day1.solve_part_a('input/example1.txt'), 24000)
        self.assertEqual(day1.solve_part_a('input/input1.txt'), 66306)
        self.assertEqual(day1.solve_part_b('input/example1.txt'), 45000)
        self.assertEqual(day1.solve_part_b('input/input1.txt'), 195292)

    def test_day_2(self):
        self.assertEqual(day2.solve_part_a('input/example2.txt'), 15)
        self.assertEqual(day2.solve_part_a('input/input2.txt'), 15422)
        self.assertEqual(day2.solve_part_b('input/example2.txt'), 12)
        self.assertEqual(day2.solve_part_b('input/input2.txt'), 15442)


if __name__ == '__main__':
    unittest.main()

