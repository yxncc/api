from flask_restful import Api, Resource
from .resources.post_resource import PostResource
from .resources.file_resource import FileResource
from .resources.qwe_resource import QweResource


def init_routes(app):
    api = Api(app)
    api.add_resource(PostResource, '/post/<int:post_id>')
    api.add_resource(FileResource, '/')
    api.add_resource(QweResource, '/ee')



class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
