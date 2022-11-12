from marshmallow import Schema, fields as mf, post_load, pre_load

from . import ProductSchema
from ..models import Order, Product
from ..extensions import db


class ReducedOrderSchema(Schema):
    id = mf.Integer()
    worker_id = mf.Integer()
    user_id = mf.Integer()


class OrderSchema(Schema):
    id = mf.Integer()
    worker_id = mf.Integer(required=True)
    user_id = mf.Integer(required=True)
    is_active = mf.Boolean(load_default=True)

    product_ids = mf.List(mf.Integer(), required=True, load_only=True)
    products = mf.List(
        mf.Nested(ProductSchema(), dump_only=True)
    )

    class Meta:
        ordered = True

    @post_load
    def make_order(self, data, **kwargs):
        data['products'] = [Product.query.get(product_id) for product_id in data['product_ids']]
        return data

