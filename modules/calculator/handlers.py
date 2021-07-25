from flask import Response
from flask_restful import Resource

from modules.calculator.calc import ExecuteReportExcelFile


class CalculatorHandler(Resource):

    def get(self):
        application = ExecuteReportExcelFile()
        http_status_code, message = application.do_action()
        return Response(message, status=http_status_code, mimetype='application/json')
