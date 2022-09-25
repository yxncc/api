import os

from flask import Flask
from flask_restful import Api

from source.users import UserResource


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # a simple page that says hello

    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app


api = Api(create_app())
api.add_resource(UserResource, '/users/')