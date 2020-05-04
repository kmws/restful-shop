from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

from app.schemes.user_schema import AddUserSchema
from models.user import User
from repositories import user_repository

ns = Namespace('user', description='User')

#TODO: verify if exists
@ns.route('')
class UserAddResource(Resource):
    @accepts(schema=AddUserSchema)
    @responds(status_code=204, api=ns)
    def post(self):
        user = User()
        user.from_json(request.json)
        user_repository.add_user(user)
