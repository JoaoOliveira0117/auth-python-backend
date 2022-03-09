from mongoengine import Document
from mongoengine.fields import StringField

class UserModel(Document):
    username = StringField(unique=True)
    name = StringField()
    password = StringField()

    meta = {
        "collection": "users",
        "strict": False,
    }