from flask import Flask
from flask_cors import CORS
from flask_migrate import MigrateCommand
from flask_login import LoginManager
from flask_restx import Api
from flask_script import Manager

from app.routes import register_routes
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
    api_admin = Api(version='1.0', title='admin api')
    register_routes(app, api)

    return app


def get_manager():
    app = init_app()

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    return manager
