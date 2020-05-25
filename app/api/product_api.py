from flask import request
from flask_accepts import responds
from flask_restx import Namespace, Resource

from app.schemes.product_schema import GetProductSchema
from repositories import product_repository

ns = Namespace('product', description='Product')


@ns.route('/list')
class ProductGetItemListResource(Resource):
    @responds(schema=GetProductSchema, status_code=201, many=True, api=ns)
    def get(self):
        price_from = request.args.get('price_from')
        price_to = request.args.get('price_to')
        group_name = request.args.get('group')
        product_list = product_repository.get_product_list(price_from, price_to, group_name)
        return product_list


@ns.route('/<int:product_id>')
@ns.param('product_id', 'Product Id')
class ProductGetItemResource(Resource):
    @responds(schema=GetProductSchema, status_code=201, api=ns)
    def get(self, product_id):
        product = product_repository.get_product(product_id=product_id)
        return product
