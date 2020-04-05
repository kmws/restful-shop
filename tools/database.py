from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


class Database:

    def __init__(self):
        self.db = None

    def init(self, app):
        self.db = SQLAlchemy(app)
        migrate = Migrate(app, self.db)


DATABASE = Database()


def get_db():
    return DATABASE.db
