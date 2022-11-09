import bdb

from flask import request
from flask_restful import Resource

from ..extensions import db
from ..models import Provider
from ..schemas import ProviderSchema


class ProviderListResource(Resource):
    def get(self):
        provider_list = Provider.query.order_by(Provider.id)
        response = ProviderSchema().dump(provider_list, many=True)
        return response, 200

    def post(self):
        new_provider = ProviderSchema().load(request.json)

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
        pass

    def delete(self, provider_id):
        provider = Provider.query.get(provider_id)
        db.session.delete(provider)
        db.session.commit()

        return {'message': 'Provider deleted successfully'}, 200
