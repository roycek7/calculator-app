import os

from flask import Flask
from flask_restful import Api
from waitress import serve

from modules.common.error import errors
from settings.config import logger
from settings.routes import routes

app = Flask(__name__)
app.config.from_object('settings.config.Config')
logger.info(f"Running {os.getenv('FLASK_ENV').upper()} Server, {os.getenv('CONFIG_TYPE').upper()} Configuration:")

api = Api(app, errors=errors)

routes(api)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080, server_name='calculator_app')
