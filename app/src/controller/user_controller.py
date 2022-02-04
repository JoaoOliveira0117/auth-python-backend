from flask import request
from flask_restx import Namespace, Resource, fields

from app.config import db
from app.src.model.user import UserModel

api = Namespace("user", description="user registration")

_user = api.model("user", {
    "id": fields.Integer(description="user id"),
    "username": fields.String(description="user username"), 
    "name": fields.String(description="user name"),
    "password": fields.String(description="user password"),
    "confirm_password": fields.String(description="user password confirmation")
})


@api.route("/register")
class User(Resource):
    @api.marshal_list_with(_user, envelope="data")
    def get(self):
        args = request.json
        user = UserModel(id=args['id'], username=args['username'], name=args['name'],password=args['password'],confirm_password=args['confirm_password'])
        db.session.add(user)
        db.session.commit()
        return user, 201