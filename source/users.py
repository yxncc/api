from flask_restful import Resource, Api, reqparse
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

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("text")
        params = parser.parse_args()

        val = {
            "id": len(my_list),
            "text": params["text"],
        }
        my_list.append(val)
        return val, 201

