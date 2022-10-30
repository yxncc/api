from marshmallow import Schema, fields as mf


class Zakaz (Schema):
    id = mf.Integer()
    worker_id = mf.Integer()
    users_id = mf.Integer()
    content = mf.String
    tovar_id = mf.Integer