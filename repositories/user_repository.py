import traceback

from models.error import CustomError, Error
from models.user import User
from tools.database import get_db


def add_user(user: User):
    try:
        get_db().session.add(user)
        get_db().session.commit()
    except Exception as e:
        print(e)
        #TODO: logger
        raise CustomError(Error.USER_ADD_ERROR, 400, traceback.print_exc())


