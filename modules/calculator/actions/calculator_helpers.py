from settings.config import logger

from modules.common.exception import ZeroDivisibleError
from modules.calculator.actions.base import OperationStrategy


class AdditionOperationStrategy(OperationStrategy):
    def create_operations(self, x, y):
        return x + y


class DivisionOperationStrategy(OperationStrategy):
    def create_operations(self, x, y):
        if y == 0:
            logger.error('Encountered zero division error following user input.')
            raise ZeroDivisibleError(f'Encountered Zero Division Error.')
        return x / y


class ExponentiationOperationStrategy(OperationStrategy):
    def create_operations(self, x, y):
        return x ** y


class MultiplicationOperationStrategy(OperationStrategy):
    def create_operations(self, x, y):
        return x * y


class SubtractionOperationStrategy(OperationStrategy):
    def create_operations(self, x, y):
        return x - y
