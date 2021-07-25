import argparse
import os

from flask import Flask
from flask_restful import Api
from waitress import serve

from modules.common.error import errors
from settings.config import logger
from settings.routes import routes

app = Flask(__name__)
app.config.from_object(os.getenv('CONFIG_TYPE'))
logger.info(f"Running {app.config['FLASK_ENV'].upper()} Server")

api = Api(app, errors=errors)

routes(api)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='Host_Address', required=False)
    parser.add_argument('--port', help='Port_Number', required=False)

    args = vars(parser.parse_args())

    serve(app, host=args['host'] if args['host'] else app.config['HOST'],
          port=args['port'] if args['port'] else app.config['PORT'],
          server_name='calculator_app')
