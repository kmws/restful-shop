from flask_restx import fields
from marshmallow import Schema


class AddProductSchema(Schema):
    name = fields.String(required=True)
    code = fields.String(required=True)
    price = fields.Float(allow_none=True)
    description = fields.String()
    group_id = fields.Integer(data_key='groupId')


class GetProductSchema(AddProductSchema):
    pass


class PutProductSchema(Schema):
    name = fields.String()
    code = fields.String()
    price = fields.Float(allow_none=True)
    description = fields.String()
    group_id = fields.Integer(data_key='groupId')
