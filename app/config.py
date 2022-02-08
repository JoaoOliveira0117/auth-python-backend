from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine

from .db_credentials import DevelopmentConfig

blueprint = Blueprint("api", __name__)

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = MongoEngine()
db.init_app(app)

def create_app() -> Flask:
    app.register_blueprint(blueprint)
    
    return app