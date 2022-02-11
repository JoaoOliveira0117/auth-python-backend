class DevelopmentConfig():
    DEBUG = True
    MONGODB_SETTINGS = {
        "db": "python",
        "host": "localhost:27017"
    }
    SECRET_KEY = "key"