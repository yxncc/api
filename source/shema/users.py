from marshmallow import Schema, fields as mf


class Users (Schema):
    id = mf.Integer()
    last_name = mf.String()
    first_name = mf.String()
    father_name = mf.String()
    email = mf.String()
