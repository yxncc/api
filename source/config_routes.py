from flask_restful import Api
from .resources import ProviderDetailResource, ProviderListResource, ProductDetailResource, ProductListResource,\
    PositionDetailResource, PositionListResource, WorkerDetailResource, WorkerListResource,\
    UserDetailResource, UserListResource


def init_routes(app):
    api = Api(app)
    api.add_resource(ProviderListResource, '/providers/')
    api.add_resource(ProviderDetailResource, '/providers/<int:provider_id>')

    api.add_resource(ProductListResource, '/products/')
    api.add_resource(ProductDetailResource, '/products/<int:product_id>')

    api.add_resource(PositionListResource, '/positions/')
    api.add_resource(PositionDetailResource, '/positions/<int:position_id>')

    api.add_resource(UserListResource, '/users/')
    api.add_resource(UserDetailResource, '/users/<int:user_id>')

    api.add_resource(WorkerListResource, '/workers/')
    api.add_resource(WorkerDetailResource, '/workers/<int:worker_id>')




