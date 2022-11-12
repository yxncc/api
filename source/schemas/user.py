from marshmallow import Schema, fields as mf, post_load

from . import OrderSchema
from ..models import User


class UserSchema(Schema):
    id = mf.Integer()
    first_name = mf.String(required=True)
    last_name = mf.String(required=True)
    father_name = mf.String(required=True)
    email = mf.String(required=True)

    orders = mf.List(
        mf.Nested(OrderSchema(), dump_only=True)
    )

    class Meta:
        ordered = True

    @post_load
    def make_provider(self, data, **kwargs):
        return User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            father_name=data['father_name'],
            email=data['email'],
        )
