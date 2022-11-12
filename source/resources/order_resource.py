from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from ..extensions import db
from ..models import Order
from ..schemas import OrderSchema


class OrderListResource(Resource):
    def get(self):
        order_list = Order.query.order_by(Order.id)
        response = OrderSchema().dump(order_list, many=True)
        return response, 200

    def post(self):
        try:
            new_order = OrderSchema().load(request.json)
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

        db.session.add(new_order)
        db.session.commit()

        new_order = Order.query.get(new_order.id)
        response = OrderSchema().dump(new_order)
        return response, 200


class OrderDetailResource(Resource):
    def get(self, order_id):
        order = Order.query.get(order_id)
        response = OrderSchema().dump(order)
        return response, 200

    def put(self, order_id):
        try:
            data = OrderSchema().load(request.json)
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

        order = Order.query.get(order_id)
        if order is None:
            return {'message': "Order with given id not found"}, 404

        order.update(data)
        db.session.commit()

        response = OrderSchema().dump(Order.query.get(order_id))
        return response, 200

    def delete(self, order_id):
        order = Order.query.get(order_id)
        db.session.delete(order)
        db.session.commit()

        return {'message': 'Order deleted successfully'}, 200
