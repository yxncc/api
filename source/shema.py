from marshmallow import Schema, fields as mf

class PostSchema (Schema):
    id = mf.Integer()
    link_type = mf.String()