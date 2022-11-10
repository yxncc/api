
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from ..extensions import db
from ..models import Provider
from ..schemas import ProviderSchema


class ProviderListResource(Resource):
    def get(self):
        provider_list = Provider.query.order_by(Provider.id)
        response = ProviderSchema().dump(provider_list, many=True)
        return response, 200

    def post(self):
        try:
            new_provider = ProviderSchema().load(request.json)
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

        db.session.add(new_provider)
        db.session.commit()

        new_provider = Provider.query.get(new_provider.id)
        response = ProviderSchema().dump(new_provider)
        return response, 200


class ProviderDetailResource(Resource):
    def get(self, provider_id):
        provider = Provider.query.get(provider_id)
        response = ProviderSchema().dump(provider)
        return response, 200

    def put(self, provider_id):
        try:
            data = ProviderSchema().load(request.json)
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

        provider = Provider.query.get(provider_id)
        if provider is None:
            return {'message': "Provider with given id not found"}, 404

        provider.update(data)
        db.session.commit()

        response = ProviderSchema().dump(Provider.query.get(provider_id))
        return response, 200

    def delete(self, provider_id):
        provider = Provider.query.get(provider_id)
        db.session.delete(provider)
        db.session.commit()

        return {'message': 'Provider deleted successfully'}, 200
