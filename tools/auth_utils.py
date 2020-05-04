from flask import request
from flask_login import current_user
from flask_login.config import EXEMPT_METHODS


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
    elif not current_user.is_authenticated:
        if handler is None:
            return None, 401
        else:
            return None, 401
    return func(*args, **kwargs)
