import unittest
from Calculate import is_prime, calc_sum, calc_multiply, calc_subtract, calc_division


class TestClass(unittest.TestCase):
    def test_equal_check(self):
        a = 20
        b = 20
        self.assertEqual(a, b)

    def test_prime_check(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(30))

    def test_add_numbers(self):
        self.assertEqual(10, calc_sum(8, 2))
        self.assertEqual(40, calc_sum(19, 21))

    def test_multiply_numbers(self):
        self.assertEqual(10, calc_multiply(5, 2))
        self.assertEqual(120, calc_multiply(8, 15))

    def test_sub_numbers(self):
        self.assertEqual(50, calc_subtract(80, 30))
        self.assertEqual(40, calc_subtract(120, 80))

    def test_div_numbers(self):
        self.assertEqual(5, calc_division(10, 2))
        self.assertEqual(25, calc_division(75, 3))
        self.assertRaises(ValueError, calc_division, 10, 0)
        with self.assertRaises(ValueError):
            calc_division(25, 0)
