from marshmallow import Schema, fields as mf, post_load

from . import OrderSchema
from ..models import Worker


class WorkerSchema(Schema):
    id = mf.Integer()
    last_name = mf.String(required=True)
    first_name = mf.String(required=True)
    father_name = mf.String(required=True)
    birthday = mf.String(required=True)
    email = mf.String(required=True)
    position_id = mf.Integer()
    orders = mf.List(
        mf.Nested(OrderSchema(), dump_only=True)
    )

    class Meta:
        ordered = True

    @post_load
    def make_worker(self, data, **kwargs):
        return Worker(
            first_name=data['first_name'],
            last_name=data['last_name'],
            father_name=data['father_name'],
            email=data['email'],
            birthday=data['birthday'],
            position_id=data['position_id']
        )


