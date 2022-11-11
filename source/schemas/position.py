from marshmallow import Schema, fields as mf, post_load

from . import WorkerSchema
from ..models import Position


class PositionSchema(Schema):
    id = mf.Integer()
    name = mf.String(required=True)
    workers = mf.List(
        mf.Nested(WorkerSchema())
    )

    class Meta:
        ordered = True

    @post_load
    def make_position(self, data, **kwargs):
        return Position(
            name=data['name']
        )
