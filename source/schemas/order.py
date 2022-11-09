from marshmallow import Schema, fields as mf

from . import ProductSchema


class ReducedOrderSchema(Schema):
    id = mf.Integer()
    worker_id = mf.Integer()
    user_id = mf.Integer()


class OrderSchema(Schema):
    id = mf.Integer()
    worker_id = mf.Integer()
    user_id = mf.Integer()
    content = mf.String()
    products = mf.List(
        mf.Nested(ProductSchema())
    )
