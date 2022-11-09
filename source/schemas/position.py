from marshmallow import Schema, fields as mf

from . import WorkerSchema


class PositionSchema(Schema):
    id = mf.Integer()
    name = mf.String()
    workers = mf.List(
        mf.Nested(WorkerSchema())
    )
