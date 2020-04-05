from marshmallow import Schema, fields


class DummySchema(Schema):
    name = fields.String(required=True, attribute='first_name')
    surname = fields.String(required=True, attribute='last_name')
    email = fields.String(required=True)


class DummyReturnSchema(DummySchema):
    id = fields.Integer(allow_none=True)
    is_active = fields.Boolean(default=True, data_key='isActive')
    is_admin = fields.Boolean(default=False, data_key='isAdmin')
