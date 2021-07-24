from modules.calculator.handlers import CalculatorHandler


def initialize_routes(api):
    api.add_resource(CalculatorHandler, '/')
