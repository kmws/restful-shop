from marshmallow import Schema, fields


class BaseSchema(Schema):
    created_at = fields.DateTime(data_key='createdAt')
    updated_at = fields.DateTime(data_key='updatedAt')
    deleted_at = fields.DateTime(data_key='deletedAt')
    deleted = fields.Boolean()
