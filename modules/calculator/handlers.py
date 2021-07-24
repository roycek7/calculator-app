from flask import Response, Blueprint

from modules.calculator.calc import ExecuteReportExcelFile

main = Blueprint('calculator', __name__)


@main.route('/')
def CalculatorHandler():
    application = ExecuteReportExcelFile()
    result = application.do_action()
    return Response(result['message'], status=result['http_status_code'], mimetype='application/json')
