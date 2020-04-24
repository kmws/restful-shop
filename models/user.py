from sqlalchemy import Column, Integer, String, Boolean, DateTime

from tools.database import get_db


class User(get_db().Model):
    __tablename__ = 'user_table'


    id = Column(Integer, primary_key=True)
    email = Column(String(60), index=True, unique=True)
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    last_login = Column(DateTime)
    password = Column(String(32), nullable=False)




