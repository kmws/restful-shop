from tokenize import String

from sqlalchemy import Column, Integer, ForeignKey, Text

from models.base import Base
from models.user import User
from tools.database import get_db


class Group(Base, get_db().Model):
    __tablename__ = 'group_table'

    name = Column(String(32), nullable=False, unique=True)
    description = Column(Text)
    added_by = Column(Integer, ForeignKey(User.id))
