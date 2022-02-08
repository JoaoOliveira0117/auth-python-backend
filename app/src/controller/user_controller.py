import uuid
from flask import request
from flask_restx import Namespace, Resource, fields

from app.src.model.user import UserModel
from app.utils.encrypt import encrypt, validate

api = Namespace("user", description="user registration")

_user = api.model("user", {
    "uid": fields.String(description="user id"),
    "username": fields.String(description="user username"), 
    "name": fields.String(description="user name"),
})


@api.route("/register")
class User(Resource):
    @api.marshal_list_with(_user, envelope="data")
    def post(self):
        uid = str(uuid.uuid4())
        user = {
            "uid": uid,
            "username": request.json["username"],
            "name": request.json["name"],
            "password": encrypt(request.json["password"])
        }
        try:
            return UserModel.objects.create(**user), 201
        except:
            return "error", 403

@api.route("/login")
class Login(Resource):
    def post(self):
        credentials = {
            "username": request.json["username"],
            "password": request.json["password"],
        }

        user = UserModel.objects.get(username=credentials["username"])

        return validate(credentials["password"], user["password"])
        