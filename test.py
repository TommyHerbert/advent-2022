import day1
import day2
import day3
import day4
import day5
import day6
import day7
import unittest


class TestStringMethods(unittest.TestCase):
    def test_day_1(self):
        self.assertEqual(24000, day1.solve_part_a('input/example1.txt'))
        self.assertEqual(66306, day1.solve_part_a('input/input1.txt'))
        self.assertEqual(45000, day1.solve_part_b('input/example1.txt'))
        self.assertEqual(195292, day1.solve_part_b('input/input1.txt'))

    def test_day_2(self):
        self.assertEqual(15, day2.solve_part_a('input/example2.txt'))
        self.assertEqual(15422, day2.solve_part_a('input/input2.txt'))
        self.assertEqual(12, day2.solve_part_b('input/example2.txt'))
        self.assertEqual(15442, day2.solve_part_b('input/input2.txt'))

    def test_day_3(self):
        self.assertEqual(157, day3.solve_part_a('input/example3.txt'))
        self.assertEqual(8243, day3.solve_part_a('input/input3.txt'))
        self.assertEqual(70, day3.solve_part_b('input/example3.txt'))
        self.assertEqual(2631, day3.solve_part_b('input/input3.txt'))

    def test_day_4(self):
        self.assertEqual(2, day4.solve_part_a('input/example4.txt'))
        self.assertEqual(511, day4.solve_part_a('input/input4.txt'))
        self.assertEqual(4, day4.solve_part_b('input/example4.txt'))
        self.assertEqual(821, day4.solve_part_b('input/input4.txt'))

    def test_day_5(self):
        self.assertEqual('CMZ', day5.solve_part_a('input/example5.txt'))
        self.assertEqual('ZRLJGSCTR', day5.solve_part_a('input/input5.txt'))
        self.assertEqual('MCD', day5.solve_part_b('input/example5.txt'))
        self.assertEqual('PRTTGRFPB', day5.solve_part_b('input/input5.txt'))

    def test_day_6(self):
        self.assertEqual(7, day6.solve_part_a('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 'string'))
        self.assertEqual(5, day6.solve_part_a('bvwbjplbgvbhsrlpgdmjqwftvncz', 'string'))
        self.assertEqual(6, day6.solve_part_a('nppdvjthqldpwncqszvftbrmjlhg', 'string'))
        self.assertEqual(10, day6.solve_part_a('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 'string'))
        self.assertEqual(11, day6.solve_part_a('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 'string'))
        self.assertEqual(1757, day6.solve_part_a('input/input6.txt', 'file'))
        self.assertEqual(19, day6.solve_part_b('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 'string'))
        self.assertEqual(23, day6.solve_part_b('bvwbjplbgvbhsrlpgdmjqwftvncz', 'string'))
        self.assertEqual(23, day6.solve_part_b('nppdvjthqldpwncqszvftbrmjlhg', 'string'))
        self.assertEqual(29, day6.solve_part_b('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 'string'))
        self.assertEqual(26, day6.solve_part_b('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 'string'))
        self.assertEqual(2950, day6.solve_part_b('input/input6.txt', 'file'))

    def test_day_7(self):
        # self.assertEqual(XXX, day7.solve_part_a('input/example7.txt', 100000))
        self.assertEqual(1915606, day7.solve_part_a('input/input7.txt', 100000))
        # self.assertEqual(XXX, day7.solve_part_b('input/example7.txt', 40000000))
        # self.assertEqual(XXX, day7.solve_part_b('input/input7.txt', 40000000))


if __name__ == '__main__':
    unittest.main()
