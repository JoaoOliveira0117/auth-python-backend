import uuid
from flask import jsonify, make_response, request
from flask_restx import Namespace, Resource, fields

from app.src.model.user import UserModel
from app.src.services.user_services import create_user, get_by_username
from app.utils.encrypt import encrypt, validate

api = Namespace("user", description="user registration")

_user = api.model("user", {
    "uid": fields.String(description="user id"),
    "username": fields.String(description="user username"), 
    "name": fields.String(description="user name"),
})


@api.route("/register")
class User(Resource):
    def post(self):
        args = {
            "username": request.json["username"],
            "name": request.json["name"],
            "password": encrypt(request.json["password"])
        }
        
        user = create_user(**args)

        if not user:
            return make_response(jsonify({'message': 'Error creating user'}), 403)

        return make_response(jsonify(user), 201)

@api.route("/login")
class Login(Resource):
    def post(self):
        credentials = {
            "username": request.json["username"],
            "password": request.json["password"],
        }
        
        user = get_by_username(credentials["username"])

        if not user:
            return make_response(jsonify({'message': 'Error creating user'}), 403)

        check_password = validate(credentials["password"], user["password"])

        if not check_password:
            return make_response(jsonify({'message': 'Incorrect Password'}), 403)
        
        return make_response(jsonify({'message': "Success!"}), 200)