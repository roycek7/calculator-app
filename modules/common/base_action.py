from flask import Response

from modules.common.exception import ActionException


class BaseAction:
    def __init__(self):
        super().__init__()

        self.http_status_code = None
        self.data = None

    def do_action(self):
        """
        This function tries to execute _produce_response which is overridden in the child class. Any exception
        encountered is thrown here. Finally returns response.
        """
        try:
            self._produce_response()
        except ActionException as e:
            self.http_status_code = e.http_status_code
            self.data = e.errors
        except Exception:
            self.http_status_code = 500
            self.data = 'Something went wrong!'

        return self._process_response()

    def _produce_response(self):
        pass

    def _process_response(self):
        """
        Return response with data passed in either produce response or action exception.
        """
        return Response(self.data, status=self.http_status_code, mimetype='application/json')
