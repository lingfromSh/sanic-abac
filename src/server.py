import orjson
from sanic import Sanic
from sanic_openapi import openapi3_blueprint
from router import api_blueprint

app = Sanic(name="abac", dumps=orjson.dumps)
app.blueprint(openapi3_blueprint)
app.blueprint(api_blueprint)
