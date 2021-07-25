from modules.calculator.actions.calculator_operator import CalculatorStrategy
from modules.calculator.utils.util import read_excel_file, create_excel_file, convert_result
from settings.config import logger
from settings.options import file_storage_path, input_file


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
        This functions reads the rows of the file and passes the x, y, and operation parameters to get the result.
        Iterates over the rows in the file and sends it to the strategy class.
        Results are displayed upto 2 decimal places. Finally, Appends the results in list.
        Additionally, it prints out the log.
        """
        for idx, row in self.file.iterrows():
            calculator = CalculatorStrategy(row['operation'], row['x'], row['y'])
            result = convert_result(calculator.get_result())
            self.results.append(result)
            logger.info(f"Executed Row {idx + 1}, x: {row['x']}, y: {row['y']}, "
                        f"operation: {row['operation']}, result: {result}")

    def do_action(self):
        """
        Do action calls all the necessary function required for the process.
        """
        self.file = read_excel_file(input_file)
        self.iterate_file()
        self.create_excel()

