import os
import sys
import unittest

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.calculator.calc import CalculatorStrategy


class CalculatorStrategyTestCases(unittest.TestCase):

    def test_addition(self):
        addition = CalculatorStrategy('add', 5, 6)
        self.assertEqual(addition.get_result(), 11)

    def test_subtraction(self):
        subtraction = CalculatorStrategy('subtract', 5, 10)
        self.assertEqual(subtraction.get_result(), -5)

    def test_multiplication(self):
        multiplication = CalculatorStrategy('multiplication', 5, 10)
        self.assertEqual(multiplication.get_result(), 50)

    def test_dec_multiplication(self):
        multiplication = CalculatorStrategy('multiplication', 0.5, 10)
        self.assertEqual(multiplication.get_result(), 5)

    def test_division(self):
        division = CalculatorStrategy('division', 5, 10)
        self.assertEqual(division.get_result(), 0.5)

    def test_exception(self):
        division = CalculatorStrategy('division', 5, 0)
        self.assertEqual(division.get_result(), 'Not Divisible')

    def test_exponentiation(self):
        exponent = CalculatorStrategy('exponentiation', 5, 10)
        self.assertEqual(exponent.get_result(), 9765625)

    def test_fn(self):
        res = CalculatorStrategy('sub', 5, 6)
        self.assertEqual(res.get_result(), 'Not Implemented')

    def test_string_input(self):
        res = CalculatorStrategy('subtract', '5', '6')
        self.assertEqual(res.get_result(), -1)

    def test_string_input2(self):
        res = CalculatorStrategy('subtract', 's', 6)
        self.assertEqual(res.get_result(), 'N/A')


# run the actual unittests
unittest.main()
