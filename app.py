from dotenv import dotenv_values
from app.config import create_app

config = dotenv_values(".env")
app = create_app()

if __name__ == '__main__':
    app.run(host=config.get("HOST"), port=config.get("PORT"))