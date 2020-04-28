from flask import Blueprint


def register_routes(app, api):
    from app.api.dummy_api import ns as dummy_namespace
    api.add_namespace(dummy_namespace)

    api_bp = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(api_bp)
    app.register_blueprint(api_bp)
