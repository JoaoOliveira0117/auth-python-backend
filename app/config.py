from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

blueprint = Blueprint("api", __name__)

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

def create_app() -> Flask:
    app.register_blueprint(blueprint)
    return app