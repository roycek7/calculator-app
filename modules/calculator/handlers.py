from flask import Response, Blueprint

from modules.calculator.calc import ExecuteReportExcelFile

main = Blueprint('calculator', __name__)


@main.route('/')
def SimpleCalculator():
    application = ExecuteReportExcelFile()
    result = application.get_parameters()
    return Response(result['message'], status=result['http_status_code'], mimetype='application/json')
