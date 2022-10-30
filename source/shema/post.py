from marshmallow import Schema, fields as mf


class Post (Schema):
    id = mf.Integer()
    name= mf.String()