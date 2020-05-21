from flask_restx import fields
from marshmallow import Schema


class AddProductSchema(Schema):
    name = fields.String(required=True)
    code = fields.String(required=True)
    description = fields.String()
    group_id = fields.Integer()
