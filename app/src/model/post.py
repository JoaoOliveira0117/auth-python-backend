from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentListField
from mongoengine.fields import StringField

class PostDetails(EmbeddedDocument):
    meta = {"strict": False}
    day = StringField(default="00")
    month = StringField(default="00")
    year = StringField(default="0000")

class PostModel(Document):
    uid = StringField(db_field='id', unique=True)
    title = StringField(default="")
    message = StringField(default="")
    details = EmbeddedDocumentListField(PostDetails)

    meta = {
        "collection": "posts",
        "strict": False,
    }