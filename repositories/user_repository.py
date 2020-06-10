import traceback
from datetime import datetime

from models.error import CustomError, Error
from models.user import User
from repositories import commit_decorator
from tools.database import get_db


#TODO: validate
@commit_decorator(Error.USER_ADD_ERROR)
def add_user(user: User):
    get_db().session.add(user)


def get_user_by_id(user_id: int) -> User:
    user = User.query.filter(User.id == user_id).first()
    if user is not None:
        return user
    else:
        raise CustomError(Error.USER_NOT_FOUND, 404)


@commit_decorator(Error.USER_UPDATE_ERROR)
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
    else:
        raise CustomError(Error.USER_NOT_FOUND, 404)


@commit_decorator(Error.USER_DELETE_ERROR)
def delete_user(user_id: int):
    user = User.query.filter(User.id == user_id).first()
    if user is not None:
        if user.root:
            raise CustomError(Error.DELETE_ROOT_FORBIDDEN, 403)
        if user.deleted:
            raise CustomError(Error.USER_ALREADY_DELETED, 400)
        user.deleted = True
        user.deleted_at = datetime.now()
    else:
        raise CustomError(Error.USER_NOT_FOUND, 404)
