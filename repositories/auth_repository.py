import flask_login

from models.error import CustomError, Error
from models.user import User


def is_not_none_or_empty(email, password):
    return email is not None and len(email) > 0 and \
           password is not None and len(password) > 0


def login_user(email, password):
    if is_not_none_or_empty(email, password):
        user = User.query.filter_by(email=email).first()
        if user is None or user.deleted:
            raise CustomError(Error.AUTH_LOGIN_USER_NOT_FOUND_ERROR, 404)
        elif not user.is_active:
            raise CustomError(Error.AUTH_LOGIN_USER_NOT_ACTIVATED, 400)
        elif user.verify_password(password):
            flask_login.login_user(user)
        else:
            raise CustomError(Error.AUTH_LOGIN_WRONG_PASSWORD, 400)

    else:
        raise CustomError(Error.AUTH_LOGIN_NOT_VALID_DATA_ERROR, 400)
