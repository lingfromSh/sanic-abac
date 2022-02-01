from sanic import Blueprint
from handler import authenticate, ws_authenticate

api_blueprint = Blueprint("api")
api_blueprint.add_route(authenticate, "/authenticate", methods=["post"])
api_blueprint.add_websocket_route(ws_authenticate, "/ws/authenticate")
