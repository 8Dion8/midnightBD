import flask
from flask_cors import CORS

from utils.db import DBHandler

APP = flask.Flask("server")
CORS(APP)

HANDLER = DBHandler()

@APP.route("/")
def api_root():
    return "Hello, world!"

@APP.route("/ping")
def api_ping():
    return {"ping", "pong"}



@APP.route("/fetch/data_column_sql_names")
def api_fetch_data_column_sql_names():
    handler_config = HANDLER.config
    table_config_to_fetch = flask.request.args.get("table")

    column_sql_names = list(i["sql_name"] for i in handler_config[table_config_to_fetch]["sqlite_columns"])

    return {"data": column_sql_names}
    
