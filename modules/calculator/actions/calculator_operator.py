import math
import traceback

from modules.calculator.actions.base import OperationStrategy
from modules.calculator.actions.calculator_helpers import AdditionOperationStrategy, SubtractionOperationStrategy, \
    DivisionOperationStrategy, ExponentiationOperationStrategy, MultiplicationOperationStrategy
from modules.calculator.utils.util import check_input
from modules.common.exception import ZeroDivisibleError
from settings.config import logger

PERMITTED_OPERATIONS = {
    'addition': AdditionOperationStrategy(),
    'subtraction': SubtractionOperationStrategy(),
    'multiplication': MultiplicationOperationStrategy(),
    'division': DivisionOperationStrategy(),
    'exponentiation': ExponentiationOperationStrategy(),
}


class CalculatorStrategy:

    def __init__(self, operation, x, y):
        self.strategy = None
        self.x = check_input(x)
        self.y = check_input(y)
        self.operation = operation
        self.strategy = OperationStrategy

    def get_result(self):
        """
        This function is responsible for getting the result according to the strategy. If parameters are missing
        returns N/A. Zero divisible error is handled which only throws an custom exception in the log and results in
        Not Divisible. If any of the operation is not implemented it throws an KeyError with result Not Implemented.
        Alphabet String exception in place of operand handled by a broader exception.
        """
        try:
            if math.isnan(self.x) or math.isnan(self.y):
                return 'N/A'

            self.strategy = PERMITTED_OPERATIONS[self.operation.lower()]
            return self.strategy.create_operations(self.x, self.y)
        except ZeroDivisibleError:
            traceback.print_exc()
            logger.warning("Exception handled.")
            return 'Not Divisible'
        except KeyError:
            traceback.print_exc()
            logger.warning("Exception handled.")
            return 'Not Implemented'
        except Exception:
            traceback.print_exc()
            logger.warning("Exception handled.")
            return 'N/A'
