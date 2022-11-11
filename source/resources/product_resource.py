from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from ..extensions import db
from ..models import Product
from ..schemas import ProductSchema


class ProductListResource(Resource):
    def get(self):
        product_list = Product.query.order_by(Product.id)
        response = ProductSchema().dump(product_list, many=True)
        return response, 200

    def post(self):
        try:
            new_product = ProductSchema().load(request.json)
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

        db.session.add(new_product)
        db.session.commit()

        new_product = Product.query.get(new_product.id)
        response = ProductSchema().dump(new_product)
        return response, 200


class ProductDetailResource(Resource):
    def get(self, product_id):
        product = Product.query.get(product_id)
        response = ProductSchema().dump(product)
        return response, 200

    def put(self, product_id):
        try:
            data = ProductSchema().load(request.json)
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

        product = Product.query.get(product_id)
        if product is None:
            return {'message': "Product with given id not found"}, 404

        product.update(data)
        db.session.commit()

        response = ProductSchema().dump(Product.query.get(product_id))
        return response, 200

    def delete(self, product_id):
        product = Product.query.get(product_id)
        db.session.delete(product)
        db.session.commit()

        return {'message': 'Product deleted successfully'}, 200
