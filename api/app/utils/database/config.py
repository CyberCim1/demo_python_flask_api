import os

# uncomment the line below for postgres database url from environment variable
postgres_local_base = os.environ['postgres://postgres:poo@172.18.0.3:5432/iso']
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'cb9f_+xw649qe1@s9rc6#=)g^m^^vwqnyxsl=8_^@jum8*8$-k'
    SESSION_COOKIE_NAME='alertstatussessioncookie'
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
