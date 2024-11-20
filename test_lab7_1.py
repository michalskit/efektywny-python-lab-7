# Testy - Zadanie 1

import unittest
from lab7_1 import newton_method, derivative

class TestNewtonMethod(unittest.TestCase):

    def test_newton_method_basic(self):
        test_cases = [
            (lambda x: x**2 - 4, 1.0, 2.0),  
            (lambda x: x**3 - x - 2, 2.0, 1.5214),  
            (lambda x: x - 1, 0.0, 1.0), 
        ]
        
        for f, x0, expected in test_cases:
            with self.subTest(f=f, x0=x0, expected=expected):
                root = newton_method(f, x0, 1e-6, 1000, 1e-5)
                self.assertAlmostEqual(root, expected, places=4)

    def test_newton_method_convergence(self):
        f = lambda x: x**2 - 4
        root = newton_method(f, 1.0, 1e-6, 1000, 1e-5)
        self.assertAlmostEqual(root, 2.0, places=4)

    def test_newton_method_no_convergence(self):
        f = lambda x: x**2 - 4
        with self.assertRaises(ValueError):
            newton_method(f, 1.0, 1e-6, 3, 1e-5)  # Too few iterations to converge

if __name__ == '__main__':
    unittest.main()
