from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base
from models.product import Product
from models.user import User
from tools.database import get_db


class CartItem(Base, get_db().Model):
    __tablename__ = 'cart_table'

    user_id = Column(Integer, ForeignKey(User.id))
    product_id = Column(Integer, ForeignKey(Product.id))
    quantity = Column(Integer)

    product = relationship('Product', foreign_keys='Cart.product_id')

    def from_json(self, data):
        self.product_id = data['product_id']
        self.quantity = data['quantity']
