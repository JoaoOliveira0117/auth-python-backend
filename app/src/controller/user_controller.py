from flask import jsonify, make_response, request
from flask_restx import Namespace, Resource
from app.src.helpers.auth import auth

from app.src.services.user_services import create_user
from app.utils.encrypt import encrypt

api = Namespace("user", description="User registration and login")

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

        return auth(credentials["username"], credentials["password"])