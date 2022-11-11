from marshmallow import Schema, fields as mf, post_load

from ..models import Product


class ProductSchema(Schema):
    id = mf.Integer()
    name = mf.String(required=True)
    provider_id = mf.Integer(required=True)

    class Meta:
        ordered = True

    @post_load
    def make_position(self, data, **kwargs):
        return Product(
            name=data['name'],
            provider_id=data['provider_id']
        )
