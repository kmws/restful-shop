import logging
import traceback

from models.error import CustomError, Error
from models.product import Product
from tools.database import get_db


def add_product(product: Product, user_id: int):
    product.added_by = user_id
    try:
        get_db().session.add(product)
        get_db().session.commit()
    except Exception as e:
        logging.warning('Problem with add new product: ' + product.name)
        traceback.print_exc()
        raise CustomError(Error.PRODUCT_ADD_ERROR, 400, traceback.print_exc())


