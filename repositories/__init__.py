import logging
import traceback

from models.error import CustomError
from tools.database import get_db


def process_commit(error_enum):
    try:
        get_db().session.commit()
    except Exception as e:
        logging.warning('traceback: ' + traceback.print_exc())
        raise CustomError(error_enum, 400)


def commit_decorator(error_enum):
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            retval = f(*args)
            process_commit(error_enum)
            return retval

        return wrapped_f

    return wrap
