from marshmallow import Schema, fields as mf


class Tovar (Schema):
    id = mf.Integer()
    provider_id = mf.String()
