from modules.calculator.handlers import CalculatorHandler


def routes(api):
    api.add_resource(CalculatorHandler, '/')
