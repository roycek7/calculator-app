from flask import Flask
from flask_restful import Api

from settings.routes import routes
from modules.common.error import errors

app = Flask(__name__)
api = Api(app, errors=errors)

routes(api)

if __name__ == "__main__":
    app.run()
