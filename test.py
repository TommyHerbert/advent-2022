import unittest
import advent1


class TestStringMethods(unittest.TestCase):
    def test_1a(self):
        self.assertEqual(advent1.solve('input/input1.txt'), 66306)


if __name__ == '__main__':
    unittest.main()

