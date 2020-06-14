import logging
import traceback

from models.cart_item import CartItem
from models.error import CustomError, Error
from repositories import commit_decorator
from tools.database import get_db


def add_cart_item(cart_item: CartItem, user_id: int):
    try:
        get_db().session.commit()
    except Exception as e:
        logging.warning('Problem with add new cart item: ' + str(cart_item.product_id))
        traceback.print_exc()
        # TODO: set id of product and user id
        raise CustomError(Error.CART_ITEM_ADD_ERROR, 400)
#

def get_cart_list_products(user_id: int):
    cart_list = CartItem.query.filter_by(user_id=user_id).all()
    return cart_list


def put_cart_items(quantity: int, cart_item_id: int, user_id: int):
    cart_item = CartItem.query.filter_by(user_id).filter_by(cart_item_id).first()
    cart_item.quantity = quantity
    try:
        get_db().session.commit()
    except Exception as e:
        # TODO: set id of product and user id
        logging.warning('Problem with update cart item: ' + str(cart_item.product_id))
        traceback.print_exc()
        # TODO: set id of product and user id
        raise CustomError(Error.CART_ITEM_UPDATE_ERROR, 400)


def delete_cart_items(cart_item_id: int, user_id: int):
    cart_item = CartItem.query.filter_by(user_id).filter_by(cart_item_id).delete()
    try:
        get_db().session.commit()
    except Exception as e:
        # TODO: set id of product and user id
        logging.warning('Problem with delete new cart item: ' + str(cart_item.product_id))
        traceback.print_exc()
        # TODO: set id of product and user id
        raise CustomError(Error.CART_ITEM_ADD_ERROR, 400)
