from mongoengine import Document
from mongoengine.fields import StringField

class UserModel(Document):
    uid = StringField(db_field='id', unique=True)
    username = StringField(unique=True)
    name = StringField()
    password = StringField()

    meta = {
        "collection": "users",
        "strict": False,
    }