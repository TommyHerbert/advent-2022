import unittest, day1, day2, day3, day4, day5


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

    def test_day_3(self):
        self.assertEqual(day3.solve_part_a('input/example3.txt'), 157)
        self.assertEqual(day3.solve_part_a('input/input3.txt'), 8243)
        self.assertEqual(day3.solve_part_b('input/example3.txt'), 70)
        self.assertEqual(day3.solve_part_b('input/input3.txt'), 2631)

    def test_day_4(self):
        self.assertEqual(day4.solve_part_a('input/example4.txt'), 2)
        self.assertEqual(day4.solve_part_a('input/input4.txt'), 511)
        self.assertEqual(day4.solve_part_b('input/example4.txt'), 4)
        self.assertEqual(day4.solve_part_b('input/input4.txt'), 821)

    def test_day_5(self):
        self.assertEqual(day5.solve_part_a('input/example5.txt'), 'CMZ')
        self.assertEqual(day5.solve_part_a('input/input5.txt'), 'ZRLJGSCTR')
        self.assertEqual(day5.solve_part_b('input/example5.txt'), 'MCD')
        self.assertEqual(day5.solve_part_b('input/input5.txt'), 'PRTTGRFPB')


if __name__ == '__main__':
    unittest.main()

