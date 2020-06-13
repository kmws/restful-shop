from flask import request
from flask_accepts import responds, accepts
from flask_login import current_user
from flask_restx import Namespace, Resource

from app.schemes.user_schema import GetUserSchema, PutUserSchema
from repositories import user_repository
from tools.auth_utils import login_required_user_api

ns = Namespace('user', description='User')


@ns.route('')
class UserAddResource(Resource):

    @login_required_user_api
    @responds(schema=GetUserSchema, status_code=200, api=ns)
    def get(self):
        user = user_repository.get_user_by_id(user_id=current_user.id)
        return user

    @login_required_user_api
    @accepts(schema=PutUserSchema, api=ns)
    @responds(status_code=204, api=ns)
    def put(self):
        schema = PutUserSchema()
        result = schema.load(request.json)
        user_repository.update_user(user_id=current_user.id, user_data=result)

    @login_required_user_api
    @responds(status_code=204, api=ns)
    def delete(self):
        user_repository.delete_user(user_id=current_user.id)
