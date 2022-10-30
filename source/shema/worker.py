from marshmallow import Schema, fields as mf


class Worker (Schema):
    id = mf.Integer()
    last_name = mf.String()
    first_name = mf.String()
    father_name = mf.String()
    birthday = mf.String()
    post_id = mf.Integer()