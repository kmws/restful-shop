from sqlalchemy import Column, Integer, ForeignKey

from models.base import Base
from models.product import Product
from models.user import User
from tools.database import get_db


class Cart(Base, get_db().Model):
    __tablename__ = 'cart_table'

    user_id = Column(Integer, ForeignKey(User.id))
    product_id = Column(Integer, ForeignKey(Product.id))
    quantity = Column(Integer)
