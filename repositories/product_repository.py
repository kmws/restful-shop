import logging
import traceback

from models.error import CustomError, Error
from models.product import Product
from repositories import group_repository
from tools.database import get_db


def get_product(product_id):
    product = Product.query.filter_by(deleted=False).filter_by(id=product_id).first()
    if product is not None:
        return product
    else:
        raise CustomError(Error.PRODUCT_NOT_FOUND, 404)


def get_product_list(price_from=None, price_to=None, group_name=None):
    product_list_query = Product.query.filter_by(deleted=False)
    if group_name is not None:
        group = group_repository.get_group_by_name(group_name)
        if group is not None:
            product_list_query = product_list_query.filter_by(group_id=group.id)
    try:
        price_from = float(price_from)
        product_list_query = product_list_query.filter(Product.price >= price_from)
    except ValueError:
        logging.warning("")
    try:
        price_to = float(price_to)
        product_list_query = product_list_query.filter(Product.price <= price_to)
    except ValueError:
        logging.warning("")

    return product_list_query.all()


def add_product(product: Product, user_id: int):
    product.added_by = user_id
    try:
        get_db().session.add(product)
        get_db().session.commit()
    except Exception as e:
        logging.warning('Problem with add new product: ' + product.name)
        traceback.print_exc()
        raise CustomError(Error.PRODUCT_ADD_ERROR, 400)


def update_product(product_data: dict, product_id: int, user_id: int):
    product = Product.query.filter_by(deleted=False).filter_by(id=product_id).first()
    if product is not None:
        for key, value in product_data.items():
            if hasattr(product, key):
                setattr(product, key, value)
            else:
                # TODO: raise error
                pass
        product.added_by = user_id
        #TODO except
        get_db().session.commit()
    else:
        raise CustomError(Error.PRODUCT_NOT_FOUND, 404)
