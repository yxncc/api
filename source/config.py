from flask.cli import load_dotenv
load_dotenv(".env")


class Config(object):
    TESTING = False


class ProductionConfig(Config):
    DB_SERVER = ''


class DevelopmentConfig(Config):
    SQLALCHEMY_POOL_TIMEOUT = 360
    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:W4L3R6Af@localhost:5433/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your secret key'
    DEBUG = False