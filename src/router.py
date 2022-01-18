from sanic import Blueprint
from handler import authenticate

api_blueprint = Blueprint("api")
api_blueprint.add_route(authenticate, "/authenticate", methods=["get"])
api_blueprint.add_websocket_route(authenticate, "/authenticate")
