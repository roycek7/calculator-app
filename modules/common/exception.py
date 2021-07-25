class ZeroDivisibleError(Exception):
    def __init__(self, message=''):
        # Call the base class constructor with the parameters it needs
        super(ZeroDivisibleError, self).__init__(message)


class ActionException(Exception):
    def __init__(self, errors=None, http_status_code=None, http_status_reason=None):

        if not errors:
            errors = []

        self.http_status_code = http_status_code
        self.http_status_reason = http_status_reason

        # Errors
        if not isinstance(errors, type(list())):
            self.errors = [errors]
        else:
            self.errors = errors

        super(ActionException, self).__init__(str(self.errors))
