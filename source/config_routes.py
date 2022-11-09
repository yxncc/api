from flask_restful import Api
from .resources.provider_resource import ProviderDetailResource, ProviderListResource


def init_routes(app):
    api = Api(app)
    api.add_resource(ProviderListResource, '/providers/')
    api.add_resource(ProviderDetailResource, '/providers/<int:provider_id>')



