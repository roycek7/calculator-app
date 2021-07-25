from modules.calculator.calculator_manager import ExecuteReportExcelFile
from modules.common.base_action import BaseAction


class ExecuteReportExcel(BaseAction):
    """
    Produces response for Api Execution
    """
    def _produce_response(self):
        application = ExecuteReportExcelFile()
        application.do_action()

        self.data = 'Success: Check Binary Storage!!!'
        self.http_status_code = 201
