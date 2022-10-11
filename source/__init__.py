import config
from flask import Flask
from .config_routes import init_routes
from .extensions import db, migrate

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config.DevelopmentConfig())
    register_extensions(app)


    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    return None
