from flask import Flask
from flask_migrate import MigrateCommand
from flask_restx import Api
from flask_script import Manager

from app.routes import register_routes
from tools.database import DATABASE


def init_app():
    app = Flask(__name__, instance_relative_config=True, template_folder='site/templates', static_folder='site/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:mysecretpassword@0.0.0.0:5566/sdn_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DATABASE.init(app)
    api = Api(version='1.0', title='api')
    register_routes(app, api)
    return app


def get_manager():
    app = init_app()

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    return manager
