from functools import wraps

from flask import request, url_for, Response
from flask_login import current_user
from flask_login.config import EXEMPT_METHODS
from werkzeug.utils import redirect


def response(status=202, headers=None):
    resp = Response(status=status, mimetype='application/json')
    if headers is not None:
        for (title, value) in headers:
            resp.headers[title] = value
    return resp


def response_error_simple(status: int):
    return response(status=status)


def response_error_web(status: int):
    if status == 401:
        return redirect(url_for('auth_web.login'))
    else:
        return Response(str(status), mimetype="text/html")


def admin_login_required(func, handler=None, *args, **kwargs):
    if request.method in EXEMPT_METHODS:
        return func(*args, **kwargs)
    elif not current_user.is_authenticated:
        if handler is None:
            return None, 401
        else:
            return None, 401
    elif not current_user.is_admin:
        return None, 403
    return func(*args, **kwargs)


def login_required(func, handler=None, *args, **kwargs):
    if request.method in EXEMPT_METHODS:
        return func(*args, **kwargs)
    elif not current_user.is_authenticated or not current_user.is_active:
        if handler is None:
            return None, 401
        else:
            return None, 401
    return func(*args, **kwargs)


def login_required_user_api(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        return login_required(func, response_error_simple(401), *args, **kwargs)
    return decorated_view


def login_required_admin_api(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        return admin_login_required(func, response_error_simple(401), *args, **kwargs)
    return decorated_view


def load_user(user_id):
    from models.user import User
    return User.query.get(int(user_id))
