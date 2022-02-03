from dotenv import dotenv_values
from flask import Flask

from app import blueprint


app = Flask(__name__)
app.config['DEBUG'] = True
config = dotenv_values(".env")
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(host=config.get("HOST"), port=config.get("PORT"))