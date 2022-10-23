from marshmallow import Schema, fields as mf


class PostSchema (Schema):
    id = mf.Integer()
    user_id = mf.Integer()
    content = mf.String()