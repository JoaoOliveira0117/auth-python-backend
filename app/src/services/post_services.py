import uuid

from app.src.model.post import PostModel

def create_post(req):
    uid = str(uuid.uuid4())

    try:
        return PostModel.objects.create(uid=uid,**req)
    except:
        return None