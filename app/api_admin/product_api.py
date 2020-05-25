from flask import request
from flask_accepts import accepts, responds
from flask_login import current_user
from flask_restx import Namespace, Resource

from app.schemes.product_schema import AddProductSchema, PutProductSchema
from models.product import Product
from repositories import product_repository
from tools.auth_utils import login_required_admin_api

ns = Namespace('product', description='Product')


@ns.route('/')
class ProductAddItemResource(Resource):
    @login_required_admin_api
    @accepts(schema=AddProductSchema, api=ns)
    @responds(status_code=204, api=ns)
    def post(self):
        product = Product()
        product.from_json(request.json)
        product_repository.add_product(product=product, user_id=current_user.id)


@ns.route('/<int:product_id>')
@ns.param('product_id', 'Product ID')
class ProductUpdateItemResource(Resource):
    @login_required_admin_api
    @accepts(schema=PutProductSchema, api=ns)
    @responds(status_code=204, api=ns)
    def put(self, product_id):
        schema = PutProductSchema()
        result = schema.load(request.json)
        product_repository.update_product(product_data=result, product_id=product_id, user_id=current_user.id)

