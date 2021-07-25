import math
import traceback

from modules.calculator.calc_helpers import AdditionOperationStrategy, SubtractionOperationStrategy, \
    DivisionOperationStrategy, ExponentiationOperationStrategy, MultiplicationOperationStrategy
from modules.calculator.utils.util import read_excel_file, create_excel_file, check_input, convert_result
from modules.common.exception import ZeroDivisibleError
from settings.config import logger
from settings.options import file_storage_path, input_file

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


class ExecuteReportExcelFile:

    def __init__(self):
        self.file = None
        self.results = []

    def create_excel(self):
        """
        Function call to create excel file.
        """
        logger.info(f"Creating Submission Output in {file_storage_path}.")
        create_excel_file({'x': self.file['x'],
                           'y': self.file['y'],
                           'operation': self.file['operation'],
                           'result': self.results},
                          file_storage_path)

    def iterate_file(self):
        """
        Iterates over the rows in the file and sends it to the strategy class. Appends the results in list.
        """
        for idx, row in self.file.iterrows():
            calculator = CalculatorStrategy(row['operation'], row['x'], row['y'])
            result = convert_result(calculator.get_result())
            self.results.append(result)
            logger.info(f"Executed Row {idx + 1}, x: {row['x']}, y: {row['y']}, "
                        f"operation: {row['operation']}, result: {result}")

    def do_action(self):
        """
        This functions reads the rows of the file and passes the x, y, and operation parameters to get the result.
        Results are displayed upto 2 decimal places. Additionally, it prints out the log and finally calls a
        function to create new excel file.
        """
        try:
            self.file = read_excel_file(input_file)
            self.iterate_file()
            self.create_excel()
            return 201, 'Success: Check Binary Storage!!!'
        except FileNotFoundError:
            return 400, "File with the given location doesn't exists"
        except Exception:
            return 500, "Something went wrong"
