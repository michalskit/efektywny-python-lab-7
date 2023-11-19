# Testy - Zadanie 1

import unittest
from lab7_1 import derivative, newton_method, parse_expression

class TestNewtonMethod(unittest.TestCase):

    def test_derivative(self):
        f = lambda x: x ** 2
        df = derivative(f)
        self.assertAlmostEqual(df(3), 6, places=5)

    def test_newton_method_convergence(self):
        f = lambda x: x**2 - 4
        df = derivative(f)
        root = newton_method(f, df, 1, 1000, 0.00001)
        self.assertAlmostEqual(root, 2.0, places=5)

    def test_newton_method_no_convergence(self):
        f = lambda x: x**2 - 4
        df = derivative(f)
        with self.assertRaises(ValueError):
            newton_method(f, df, 1, 3, 0.00001)

if __name__ == '__main__':
    unittest.main()
