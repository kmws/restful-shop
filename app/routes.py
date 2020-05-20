from flask import Blueprint


def register_routes(app, api, api_user, api_admin):
    from app.api.auth_api import ns as auth_namespace
    api.add_namespace(auth_namespace)
    from app.api.user_api import ns as user_namespace
    api.add_namespace(user_namespace)

    api_bp = Blueprint('api', __name__)
    api.init_app(api_bp)
    api_user_bp = Blueprint('api_user', __name__, url_prefix='/api-user')
    api_user.init_app(api_user_bp)
    api_admin_bp = Blueprint('api_admin', __name__, url_prefix='/api-user-admin')
    api_admin.init_app(api_admin_bp)

    app.register_blueprint(api_bp)
    app.register_blueprint(api_user_bp)
    app.register_blueprint(api_admin_bp)
