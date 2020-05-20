from marshmallow import Schema, fields

from app.schemes.base_schema import BaseSchema


class ReturnAddUserSchema(Schema):
    id = fields.Integer(required=True)


class AddUserSchema(Schema):
    email = fields.String(required=True)
    first_name = fields.String(data_key='firstName')
    last_name = fields.String(data_key='lastName')
    password = fields.String(required=True)


class GetUserSchema(BaseSchema):
    email = fields.String()
    first_name = fields.String(data_key='firstName')
    last_name = fields.String(data_key='lastName')
    is_admin = fields.Boolean(data_key='isAdmin')
    is_active = fields.Boolean(data_key='isActive')
    last_login = fields.DateTime(data_key='lastLogin')
    blocked = fields.Boolean()


class UpdateUserSchema(Schema):
    email = fields.String()
    first_name = fields.String(data_key='firstName')
    last_name = fields.String(data_key='lastName')
    is_admin = fields.Boolean(data_key='isAdmin')
    is_active = fields.Boolean(data_key='isActive')
    blocked = fields.Boolean()
