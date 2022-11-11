from flask_restful import Api
from .resources import ProviderDetailResource, ProviderListResource, PositionDetailResource, PositionListResource


def init_routes(app):
    api = Api(app)
    api.add_resource(ProviderListResource, '/providers/')
    api.add_resource(ProviderDetailResource, '/providers/<int:provider_id>')

    api.add_resource(PositionListResource, '/positions/')
    api.add_resource(PositionDetailResource, '/positions/<int:position_id>')




