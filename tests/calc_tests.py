import os
import sys
import unittest

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.calculator.actions.calculator_operator import CalculatorStrategy


class CalculatorStrategyTestCases(unittest.TestCase):

    def test_addition(self):
        addition = CalculatorStrategy('Addition', 5, 6)
        self.assertEqual(addition.get_result(), 11)

    def test_subtraction(self):
        subtraction = CalculatorStrategy('subtraction', 5, 10)
        self.assertEqual(subtraction.get_result(), -5)

    def test_multiplication(self):
        multiplication = CalculatorStrategy('Multiplication', 5, 10)
        self.assertEqual(multiplication.get_result(), 50)

    def test_dec_multiplication(self):
        multiplication = CalculatorStrategy('multiplication', 0.5, 10)
        self.assertEqual(multiplication.get_result(), 5)

    def test_division(self):
        division = CalculatorStrategy('DIVISION', 5, 10)
        self.assertEqual(division.get_result(), 0.5)

    def test_exception(self):
        division = CalculatorStrategy('Division', 5, 0)
        self.assertEqual(division.get_result(), 'Not Divisible')

    def test_exponentiation(self):
        exponent = CalculatorStrategy('exponentiation', 5, 10)
        self.assertEqual(exponent.get_result(), 9765625)

    def test_fn(self):
        res = CalculatorStrategy('sub', 5, 6)
        self.assertEqual(res.get_result(), 'Not Implemented')

    def test_string_input(self):
        res = CalculatorStrategy('subtraction', '5', '6')
        self.assertEqual(res.get_result(), -1)

    def test_string_input_alphabet(self):
        res = CalculatorStrategy('SUBTRACTION', 's', 6)
        self.assertEqual(res.get_result(), 'N/A')

    def test_missing_operation(self):
        res = CalculatorStrategy(float("NaN"), '6', 6)
        self.assertEqual(res.get_result(), 'N/A')

    def test_missing_operand(self):
        res = CalculatorStrategy('SUBTRACTION', float("NaN"), float("NaN"))
        self.assertEqual(res.get_result(), 'N/A')

    def test_missing_all(self):
        res = CalculatorStrategy(float("NaN"), float("NaN"), float("NaN"))
        self.assertEqual(res.get_result(), 'N/A')


# run the actual unittests
unittest.main()
