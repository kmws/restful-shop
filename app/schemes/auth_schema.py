from marshmallow import Schema, fields


class LoginSchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)
