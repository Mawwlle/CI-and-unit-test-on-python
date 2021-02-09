import unittest
from main import Calculator, array_sum, Circle


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


class TestCircleOperations(unittest.TestCase):

    def setUp(self):
        self.diameter = 6
        self.circle = Circle(self.diameter)

    def test_radius(self):
        self.assertEqual(self.circle.radius(), self.diameter / 2)

    def test_square(self):
        self.assertEqual(round(self.circle.square()), round(3.1415 * (self.diameter * self.diameter)/4))
        self.assertEqual(self.circle.square(), 3.1415 * self.circle.radius() * self.circle.radius())

    def test_line_length(self):
        self.assertEqual(self.circle.line_length(), 3.1415 * self.diameter)


if __name__ == '__main__':
    unittest.main(verbosity=2)
