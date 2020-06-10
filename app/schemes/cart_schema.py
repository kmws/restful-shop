from flask_restx import fields
from marshmallow import Schema


class UpdateCartItemSchema(Schema):
    quantity = fields.Integer()


class AddCartItemSchema(UpdateCartItemSchema):
    product_id = fields.Integer(data_key='productId')


class GetCartItemSchema(UpdateCartItemSchema):
    name = fields.String(attribute='product.name')
    price = fields.Float(attribute='product.price')
