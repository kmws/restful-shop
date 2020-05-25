from tokenize import String

from sqlalchemy import Column, Text, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from models.base import Base
from models.group import Group
from models.user import User
from tools.database import get_db


class Product(Base, get_db().Model):
    __tablename__ = 'product_table'

    name = Column(String(32), nullable=False, unique=True)
    code = Column(String(32), nullable=False, unique=True)
    price = Column(Float, nullable=True)
    description = Column(Text)

    added_by = Column(Integer, ForeignKey(User.id))
    group_id = Column(Integer, ForeignKey(Group.id))
    group = relationship('Group', foreign_keys='Product.group_id')

    def from_json(self, data):
        self.name = data['name']
        self.code = data['data']
        self.price = data['price']
        self.description = data['description']
        self.group = data['groupId'] if 'groupId' in data else None
