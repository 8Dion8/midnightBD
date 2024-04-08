import flask
from flask_cors import CORS

APP = flask.Flask("server")
CORS(APP)

@APP.route("/")
def api_root():
    return "Hello, world!"

@APP.route("/ping")
def api_ping():
    return {"ping", "pong"}


