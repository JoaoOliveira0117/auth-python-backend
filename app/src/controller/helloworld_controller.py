
from flask_restx import Namespace, Resource


api = Namespace("test", description="a small testing route")

@api.route("/test")
class Test(Resource):
    def get(self):
        return {"data": "Hello World!"}