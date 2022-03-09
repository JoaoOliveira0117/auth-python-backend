from flask_restx import Api
from app.config import blueprint

from .src.controller.helloworld_controller import api as helloworld_ctlr
from .src.controller.user_controller import api as user_ctlr
from .src.controller.posts_controller import api as posts_ctlr

api = Api(
    blueprint,
    title="SIMPLE JWT TOKEN-BASED AUTHENTICATION API",
    version="1.0",
    description="a application created for studying purposes"
)

api.add_namespace(helloworld_ctlr,path="/")
api.add_namespace(user_ctlr,path="/")
api.add_namespace(posts_ctlr, path="/posts")