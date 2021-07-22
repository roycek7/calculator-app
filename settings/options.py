import logging

from modules.calculator.calc_helpers import AdditionOperationStrategy
from modules.calculator.calc_helpers import DivisionOperationStrategy
from modules.calculator.calc_helpers import ExponentiationOperationStrategy
from modules.calculator.calc_helpers import MultiplicationOperationStrategy
from modules.calculator.calc_helpers import SubtractionOperationStrategy

config = {
    'addition': AdditionOperationStrategy(),
    'add': AdditionOperationStrategy(),

    'subtraction': SubtractionOperationStrategy(),
    'subtract': SubtractionOperationStrategy(),

    'multiplication': MultiplicationOperationStrategy(),
    'mul': MultiplicationOperationStrategy(),

    'division': DivisionOperationStrategy(),
    'divide': DivisionOperationStrategy(),

    'exponentiation': ExponentiationOperationStrategy(),
    'exp': ExponentiationOperationStrategy()
}

input_file = 'Sample Input.xlsx'
file_storage_path = 'binary_storage/submission.xlsx'

logging.basicConfig(level=logging.INFO)
