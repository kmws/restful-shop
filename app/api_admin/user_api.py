from flask import request
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

from app.schemes.user_schema import GetUserSchema, UpdateUserSchema
from repositories import user_repository
from tools.auth_utils import admin_login_required

ns = Namespace('user', description='User')


@ns.route('/<int:user_id>')
class UserItemResource(Resource):
    @admin_login_required
    @responds(schema=GetUserSchema, api=ns)
    def get(self, user_id):
        user = user_repository.get_user_by_id(user_id)
        return user

    @admin_login_required
    @accepts(schema=UpdateUserSchema, api=ns)
    @responds(status_code=204, api=ns)
    def put(self, user_id):
        user_repository.update_user(user_id, request.json)

    @admin_login_required
    @responds(status_code=204, api=ns)
    def delete(self, user_id):
        user_repository.delete_user(user_id)