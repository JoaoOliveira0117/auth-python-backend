from flask import jsonify, make_response, request
from flask_restx import Namespace, Resource
from app.src.services.post_services import create_post

api = Namespace("post", description="Posts management route")

@api.route("/create")
class Post(Resource):
    def post(self):
        post = create_post(request.json)

        if not post:
            return make_response(jsonify({'message': 'Error creating Post'}), 403)

        return make_response(jsonify(post), 201)
