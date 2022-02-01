import orjson
from sanic import Sanic
from sanic_openapi import openapi3_blueprint
from router import api_blueprint
from tortoise.contrib.sanic import register_tortoise

app = Sanic(name="abac", dumps=orjson.dumps)
app.blueprint(openapi3_blueprint)
app.blueprint(api_blueprint)

register_tortoise(app, db_url='postgres://postgres:rbac2022@crazy-postgres:5432', modules={'models': ['models']}, generate_schemas=True)
