from flask import Flask
from flask_cors import CORS
from flask_migrate import MigrateCommand
from flask_login import LoginManager
from flask_restx import Api
from flask_script import Manager

from app.routes import register_routes
from models.user import User
from repositories import user_repository
from tools.config_properties import app_config, get_config
from tools.database import DATABASE

login_manager = LoginManager()


def init_app():
    app = Flask(__name__, instance_relative_config=True, template_folder='site/templates', static_folder='site/static')
    app.config.from_object(app_config[get_config().get_flask_config()])

    app.config['SQLALCHEMY_DATABASE_URI'] = get_config().get_db_config()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = get_config().get_secret_key()

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    CORS(app, headers=['Content-Type'], expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True)
    DATABASE.init(app)

    api = Api(version='1.0', title='api')
    api_user = Api(version='1.0', title='api user')
    api_admin = Api(version='1.0', title='api admin')
    register_routes(app, api, api_user, api_admin)

    return app


def create_root(email, password):
    root = User.query.filter_by(root=True).first()
    if root is None:
        root = User()
        root.email = email
        root.is_admin = True
        root.is_active = True
        root.password = password
        user_repository.add_user(root)
    else:
        if not(root.email != email or not root.verify_password(password)):
            exit(1)

def get_manager():
    app = init_app()

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    return manager
