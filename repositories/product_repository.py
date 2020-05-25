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


def update_product(product_data: dict, product_id: int, user_id: int):
    product = Product.query.filter_by(id=product_id).first()
    if product is not None:
        for key, value in product_data.items():
            if hasattr(product, key):
                setattr(product, key, value)
            else:
                # TODO: raise error
                pass
        product.added_by = user_id
        get_db().session.commit()
    else:
        raise CustomError(Error.PRODUCT_NOT_FOUND, 404)
