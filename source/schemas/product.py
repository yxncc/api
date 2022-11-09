from marshmallow import Schema, fields as mf


class ProductSchema(Schema):
    id = mf.Integer(required=True)
    provider_id = mf.Integer(required=True)

