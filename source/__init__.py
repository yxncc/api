from flask import Flask
from .config_routes import init_routes
from .extensions import db, migrate
from .config import DevelopmentConfig
from . import models


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DevelopmentConfig())
    register_extensions(app)
    init_routes(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    return None
