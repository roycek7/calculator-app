class ZeroDivisibleError(Exception):
    def __init__(self, message=''):
        # Call the base class constructor with the parameters it needs
        super(ZeroDivisibleError, self).__init__(message)


class InternalServerError(Exception):
    pass


class FileDoesNotExistsError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "FileDoesNotExistsError": {
        "message": "File with the given location doesn't exists",
        "status": 404
    }
}
