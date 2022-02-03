
from flask import Blueprint
from flask_restx import Api

from .src.controller.helloworld_controller import api as helloworld_ctlr


blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="SIMPLE JWT TOKEN-BASED AUTHENTICATION API",
    version="1.0",
    description="a application created for studying purposes"
)

api.add_namespace(helloworld_ctlr,path="/")