from api_factory import Factory
from flask import Flask
from utils.database import settings
from utils.database.db_base import db
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

#testing commit

class db_setup:
    def __init__(self):
        app = Flask(__name__)
        if(self.create_db()):
            with app.app_context():
                self.initialize_db(app)
        else:
            print('db already exists...')

    def create_db(self):
        engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
        if not database_exists(engine.url):
            print('creating new db')
            create_database(engine.url)
            return True
        print(database_exists(engine.url))
        return False

    def configure_app(self, flask_app):
        flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
        flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
        flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
        flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
        flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
        flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

    def initialize_db(self, flask_app):
        self.configure_app(flask_app)
        db.init_app(flask_app)
        db.drop_all() #TODO: Don't use this unless you want to delete everything
        db.session.commit()

        api_factory = Factory() #pulling models from here

        #create tables
        db.create_all()
        db.session.commit()
        migrate = Migrate(flask_app, db)
        #api_factory.init_org_data()

db_setup()
