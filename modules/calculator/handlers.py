from flask import Response
from flask_restful import Resource

from modules.calculator.calc import ExecuteReportExcelFile


class CalculatorHandler(Resource):

    def get(self):
        application = ExecuteReportExcelFile()
        result = application.do_action()
        return Response(result['message'], status=result['http_status_code'], mimetype='application/json')
