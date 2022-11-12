from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from ..extensions import db
from ..models import User
from ..schemas import UserSchema


class UserListResource(Resource):
    def get(self):
        user_list = User.query.order_by(User.id)
        response = UserSchema().dump(user_list, many=True)
        return response, 200

    def post(self):
        try:
            new_user = UserSchema().load(request.json)
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

        db.session.add(new_user)
        db.session.commit()

        new_user = User.query.get(new_user.id)
        response = UserSchema().dump(new_user)
        return response, 200


class UserDetailResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        response = UserSchema().dump(user)
        return response, 200

    def put(self, user_id):
        try:
            data = UserSchema().load(request.json)
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

        user = User.query.get(user_id)
        if user is None:
            return {'message': "User with given id not found"}, 404

        user.update(data)
        db.session.commit()

        response = UserSchema().dump(User.query.get(user_id))
        return response, 200

    def delete(self, user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()

        return {'message': 'User deleted successfully'}, 200
