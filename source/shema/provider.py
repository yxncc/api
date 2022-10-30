from marshmallow import Schema, fields as mf


class Provider (Schema):
    id = mf.Integer()
    name = mf.String()
