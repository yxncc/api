class Config(object):
    TESTING = False


class ProductionConfig(Config):
    DB_SERVER = ''


class DevelopmentConfig(Config):
    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your secret key'
    DEBUG = False
