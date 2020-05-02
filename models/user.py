from flask_login import UserMixin
from sqlalchemy import Column, String, Boolean, DateTime
from werkzeug.security import generate_password_hash, check_password_hash

from models.base import Base
from tools.database import get_db


class User(UserMixin, Base, get_db().Model):
    __tablename__ = 'user_table'

    email = Column(String(60), index=True, unique=True)
    first_name = Column(String(60))
    last_name = Column(String(60))
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    last_login = Column(DateTime)
    password_hash = Column(String(128))
    blocked = Column(Boolean, default=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        # TODO: validate if password is in proper format
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)





