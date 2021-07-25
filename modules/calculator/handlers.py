from flask_restful import Resource

from modules.calculator.actions.calculator_xlsx import ExecuteReportExcel


class CalculatorHandler(Resource):
    """
    Restful Api of calculator.
    """
    def get(self):
        application = ExecuteReportExcel()
        return application.do_action()
