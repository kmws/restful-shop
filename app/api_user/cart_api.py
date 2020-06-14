from flask import request
from flask_accepts import responds, accepts
from flask_login import current_user
from flask_restx import Namespace, Resource

from app.schemes.cart_schema import GetCartItemSchema, AddCartItemSchema, UpdateCartItemSchema
from models.cart_item import CartItem
from repositories import cart_repository
from tools.auth_utils import login_required_user_api

ns = Namespace('cart', description='Cart')


@ns.route('')
class CartItemResource(Resource):
    @login_required_user_api
    @accepts(schema=AddCartItemSchema, api=ns)
    @responds(status_code=204, api=ns)
    def post(self):
        cart_item = CartItem()
        cart_item.from_json(request.json)
        cart_repository.add_cart_item(cart_item=cart_item, user_id=current_user.id)


@ns.route('/list')
class CartItemListResource(Resource):
    @login_required_user_api
    @responds(schema=GetCartItemSchema, status_code=200, many=True, api=ns)
    def get(self):
        cart_products = cart_repository.get_cart_list_products(user_id=current_user.id)
        return cart_products


@ns.route('/<int:cart_item_id>')
@ns.param('cart_item_id', 'Cart item id')
class CartItemSelectedResource(Resource):
    @login_required_user_api
    @accepts(schema=UpdateCartItemSchema, api=ns)
    @responds(status_code=204, api=ns)
    def put(self, cart_item_id):
        quantity = request.json['quantity']
        if quantity < 1:
            cart_repository.delete_cart_items(cart_item_id=cart_item_id, user_id=current_user.id)
        else:
            cart_repository.put_cart_items(quantity=quantity, cart_item_id=cart_item_id, user_id=current_user.id)

    @login_required_user_api
    @responds(status_code=204, api=ns)
    def delete(self, cart_item_id):
        cart_repository.delete_cart_items(cart_item_id=cart_item_id, user_id=current_user.id)
