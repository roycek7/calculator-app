import traceback

from modules.calculator.calc_helpers import AdditionOperationStrategy
from modules.calculator.calc_helpers import DivisionOperationStrategy
from modules.calculator.calc_helpers import ExponentiationOperationStrategy
from modules.calculator.calc_helpers import MultiplicationOperationStrategy
from modules.calculator.calc_helpers import SubtractionOperationStrategy
from modules.calculator.utils.util import read_file, create_excel, check_input
from modules.common.exception import ZeroDivisibleError
from modules.common.http_message import http_message_information
from settings.options import file_storage_path, logging, input_file

logger = logging.getLogger(__name__)

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
        if self.x and self.y is None:
            return 'N/A'

        try:
            self.strategy = PERMITTED_OPERATIONS[self.operation.lower()]
            return self.strategy.create_operations(self.x, self.y)
        except ZeroDivisibleError:
            traceback.print_exc()
            logger.warning(f"Exception handled.")
            return 'Not Divisible'
        except KeyError:
            traceback.print_exc()
            logger.warning(f"Exception handled.")
            return 'Not Implemented'
        except Exception:
            traceback.print_exc()
            logger.warning(f"Exception handled.")
            return 'N/A'


class ExecuteReportExcelFile:

    def __init__(self):
        self.file = None
        self.results = []

    def do_action(self):
        """
        This functions reads the rows of the file and passes the x, y, and operation parameters to get the result.
        Additionally, it prints out the log and finally calls a function to create new excel file.
        """
        try:
            self.file = read_file(input_file)
            for idx, row in self.file.iterrows():
                calculator = CalculatorStrategy(row['operation'], row['x'], row['y'])
                result = calculator.get_result()

                self.results.append(result)
                logger.info(f"Executed Row {idx + 1}, x: {row['x']}, y: {row['y']}, "
                            f"operation: {row['operation']}, result: {result}")

            logger.info(f"Creating Submission Output in {file_storage_path}.")
            create_excel({'x': self.file['x'],
                          'y': self.file['y'],
                          'operation': self.file['operation'],
                          'result': self.results},
                         file_storage_path)
            return http_message_information(201, 'Success: Check Binary Storage!!!')
        except FileNotFoundError:
            traceback.print_exc()
            logger.error("Input file not found.")
            return http_message_information(404, '404 File Not Found!')
        except Exception:
            traceback.print_exc()
            logger.error("Something went wrong!")
            return http_message_information(500, 'Internal Server Error!')
