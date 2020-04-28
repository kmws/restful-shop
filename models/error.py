from flask import jsonify


class CustomError(Exception):
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


def register_custom_errors(app):
    @app.errorhandler(CustomError)
    def specify_auth_error(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response
