import math
import unittest
from scientific_calculator import add,sin, cos, tan, sqrt, log, exp

class TestScientificCalculator(unittest.TestCase):

    # Sin Tests
    def test_sin_positive(self):
        self.assertAlmostEqual(sin(90), 1.0, places=5)

    def test_sin_negative(self):
        self.assertAlmostEqual(sin(-90), -1.0, places=5)

    def test_sin_zero(self):
        self.assertEqual(sin(0), 0)

    def test_sin_non_numeric(self):
        with self.assertRaises(ValueError):
            sin("hello")

    # for Cos Testcases
    def test_cos_positive(self):
        self.assertAlmostEqual(cos(0), 1.0, places=5)

    def test_cos_negative(self):
        self.assertAlmostEqual(cos(180), -1.0, places=5)

    def test_cos_non_numeric(self):
        with self.assertRaises(ValueError):
            cos("hello")

    # for tan testcases
    def test_tan(self):
        self.assertAlmostEqual(tan(45), 1.0, places=5)

    def test_tan_non_numeric(self):
        with self.assertRaises(ValueError):
            tan("Hi")

    # for sqrt testcases
    def test_sqrt_positive(self):
        self.assertEqual(sqrt(4), 2)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_sqrt_non_numeric(self):
        with self.assertRaises(ValueError):
            sqrt("hello")

    # for Log Testcases
    def test_log(self):
        self.assertAlmostEqual(log(1), 0.0, places=5)

    def test_log_negative(self):
        with self.assertRaises(ValueError):
            log(-1)

    def test_log_zero(self):
        with self.assertRaises(ValueError):
            log(0)

    def test_log_non_numeric(self):
        with self.assertRaises(ValueError):
            log("hello")

    # for Exp Testcases
    def test_exp(self):
        self.assertAlmostEqual(exp(1), math.e, places=5)

    def test_exp_non_numeric(self):
        with self.assertRaises(ValueError):
            exp("hello")

if __name__ == '__main__':
    unittest.main()
      

