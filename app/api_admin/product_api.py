from flask_accepts import accepts
from flask_restx import Namespace, Resource

from app.schemes.product_schema import AddProductSchema
from repositories import product_repository
from tools.auth_utils import login_required_admin_api

ns = Namespace('product', description='Product')


@ns.route('/')
class ProductAddItemResource(Resource):
    @login_required_admin_api
    @accepts(schema=AddProductSchema, api=ns)
    def post(self, user_id):
        product_repository
        pass
