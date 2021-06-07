from api_factory import Factory
from utils.database import settings
from flask import Flask
from utils.database.db_base import db

def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def initialize_app(flask_app):
    configure_app(flask_app)
    flask_app.register_blueprint(Factory().get_blueprint())
    db.init_app(flask_app)

app = Flask(__name__)
initialize_app(app)

'''-----------------------Testing---------------------------'''
@app.route("/")
def hello():
    return "Hey I'm using Docker!"
'''--------------------End of Testing-----------------------'''

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=settings.FLASK_DEBUG)
