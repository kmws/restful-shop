from flask import Blueprint


def register_routes(app, api):
    from app.api.auth_api import ns as auth_namespace
    api.add_namespace(auth_namespace)

    api_bp = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(api_bp)
    app.register_blueprint(api_bp)
