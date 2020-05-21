from sqlalchemy import Column, Integer, ForeignKey

from models.base import Base
from models.product import Product
from tools.database import get_db


class Magazine(Base, get_db().Model):
    __tablename__ = 'magazine_table'

    product_id = Column(Integer, ForeignKey(Product.id))
    quantity = Column(Integer, default=0)

