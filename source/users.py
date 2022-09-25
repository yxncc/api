from flask_restful import Resource, Api
from flask import Flask, request

my_list = [
    {
        "id": 1,
        "text": "кцкцц"
    },
    {
        "id": 2,
        "text": "dsfdf"
    }



]


class UserResource(Resource):
    def get(self):
        return my_list, 200

