from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

from app.schemes.auth_schema import LoginSchema
from repositories import auth_repository

#  Namespace is to API what :class:`flask:flask.Blueprint` is for :class:`flask:flask.Flask`.
ns = Namespace('auth', description='Auth')


@ns.route('/login')
class LoginResource(Resource):
    @accepts(schema=LoginSchema, api=ns)
    @responds(status_code=204, api=ns)
    def post(self):
        auth_repository.login_user(request.json['email'], request.json['password'])
