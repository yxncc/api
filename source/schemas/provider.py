from marshmallow import Schema, fields as mf, post_load

from .product import ProductSchema
from ..models import Provider


class ProviderSchema(Schema):
    id = mf.Integer()
    name = mf.String(required=True)
    products = mf.List(
        mf.Nested(ProductSchema(), dump_only=True)
    )

    class Meta:
        ordered = True

    @post_load
    def make_provider(self, data, **kwargs):
        return Provider(
            name=data['name']
        )
