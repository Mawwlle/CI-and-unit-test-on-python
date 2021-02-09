import unittest
from main import Calculator, array_sum


class TestCalc(unittest.TestCase):

    def setUp(self):
        self.a = 13
        self.b = 2
        self.calc = Calculator(self.a, self.b)

    def test_sum(self):
        self.assertEqual(self.calc.sum(), 15)

    def test_sub(self):
        self.assertEqual(self.calc.sub(), 11)

    def test_mul(self):
        self.assertEqual(self.calc.mul(), 26)

    def test_div(self):
        self.assertEqual(self.calc.div(), 13 / 2)


class TestArraySum(unittest.TestCase):

    def test_sum_array(self):
        self.assertEqual(array_sum([13, 2, 4, 5, 6]), 13 + 2 + 4 + 5 + 6)
        self.assertEqual(array_sum([13, "test", 32, 4]), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
