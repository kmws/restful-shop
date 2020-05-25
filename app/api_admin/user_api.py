from flask import request
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

from app.schemes.user_schema import GetUserSchema, PutUserSchema
from repositories import user_repository
from tools.auth_utils import login_required_admin_api

ns = Namespace('user', description='User')


@ns.route('/<int:user_id>')
class UserItemResource(Resource):
    @login_required_admin_api
    @responds(schema=GetUserSchema, api=ns)
    def get(self, user_id):
        user = user_repository.get_user_by_id(user_id)
        return user

    @login_required_admin_api
    @accepts(schema=PutUserSchema, api=ns)
    @responds(status_code=204, api=ns)
    def put(self, user_id):
        schema = PutUserSchema()
        result = schema.load(request.json)
        user_repository.update_user(user_id, result)

    @login_required_admin_api
    @responds(status_code=204, api=ns)
    def delete(self, user_id):
        user_repository.delete_user(user_id)