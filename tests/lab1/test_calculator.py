import unittest
from src.lab1.calculator import calculator

class CalculatorTest(unittest.TestCase):
       
    def test_sum(self):
        self.assertEqual(calculator(1, '+', 1), 2)

    def test_difference(self):
        self.assertEqual(calculator(9, '-', 4), 5)

    def test_multiplication(self):
        self.assertEqual(calculator(2, '*', 22), 44)

    def test_division(self):
        self.assertEqual(calculator(100, '/', 10), 10.0)

    def test_int_division(self):
        self.assertEqual(calculator(22, '//', 7), 3)

    def test_mod(self):
        self.assertEqual(calculator(22, '%', 7), 1)

    def test_invalid_operator(self):
        with self.assertRaises(KeyError):
            calculator(15, '?', 3)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator(50, '/', 0)

