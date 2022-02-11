import uuid

from app.src.model.user import UserModel


def create_user(username, name, password):
    uid = str(uuid.uuid4())

    try:
        return UserModel.objects.create(uid=uid,username=username, name=name, password=password)
    except:
        return None

def get_by_username(username):
    try:
        return UserModel.objects.get(username=username)
    except:
        return None