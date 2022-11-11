from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from ..extensions import db
from ..models import Position
from ..schemas import PositionSchema


class PositionListResource(Resource):
    def get(self):
        position_list = Position.query.order_by(Position.id)
        response = PositionSchema().dump(position_list, many=True)
        return response, 200

    def post(self):
        try:
            new_position = PositionSchema().load(request.json)
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

        db.session.add(new_position)
        db.session.commit()

        new_position = Position.query.get(new_position.id)
        response = PositionSchema().dump(new_position)
        return response, 200


class PositionDetailResource(Resource):
    def get(self, position_id):
        position = Position.query.get(position_id)
        response = PositionSchema().dump(position)
        return response, 200

    def put(self, position_id):
        try:
            data = PositionSchema().load(request.json)
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

        position = Position.query.get(position_id)
        if position is None:
            return {'message': "Position with given id not found"}, 404

        position.update(data)
        db.session.commit()

        response = PositionSchema().dump(Position.query.get(position_id))
        return response, 200

    def delete(self, position_id):
        position = Position.query.get(position_id)
        db.session.delete(position)
        db.session.commit()

        return {'message': 'Position deleted successfully'}, 200
