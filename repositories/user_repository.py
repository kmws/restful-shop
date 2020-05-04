import traceback
from datetime import datetime

from models.error import CustomError, Error
from models.user import User
from tools.database import get_db


def add_user(user: User):
    try:
        get_db().session.add(user)
        get_db().session.commit()
    except Exception as e:
        print(e)
        # TODO: logger
        raise CustomError(Error.USER_ADD_ERROR, 400, traceback.print_exc())


def get_user_by_id(user_id: int) -> User:
    user = User.query.filter(User.id == user_id).first()
    if user is not None:
        return user
    else:
        raise CustomError(Error.USER_NOT_FOUND, 404)


def update_user(user_id: int, user_data: dict):
    user = User.query.filter_by(id=user_id).first()
    if user is not None:
        if user.root:
            raise CustomError(Error.UPDATE_ROOT_FORBIDDEN, 403)
        for key, value in user_data.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                # TODO: raise error
                pass
        get_db().session.commit()
    else:
        raise CustomError(Error.USER_NOT_FOUND, 404)


def delete_user(user_id: int):
    user = User.query.filter(User.id == user_id).first()
    if user is not None:
        if user.root:
            raise CustomError(Error.DELETE_ROOT_FORBIDDEN, 403)
        if user.deleted:
            raise CustomError(Error.USER_ALREADY_DELETED, 400)
        user.deleted = True
        user.deleted_at = datetime.now()
        get_db().session.commit()
    else:
        raise CustomError(Error.USER_NOT_FOUND, 404)
