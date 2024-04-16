import flask
from flask_cors import CORS

from utils.db import DBHandler

from time import sleep

APP = flask.Flask("server")
CORS(APP)

HANDLER = DBHandler()

@APP.route("/")
def api_root():
    return "Hello, world!"

@APP.route("/ping")
def api_ping():
    return {"ping", "pong"}



@APP.route("/fetch/data_column_names")
def api_fetch_data_column_sql_names():
    handler_config = HANDLER.config
    table_config_to_fetch = flask.request.args.get("table")
    data = list(
        {
            "field": i["sql_name"],
            "header": i["display_name"],
            "display_type": i["display_type"]
        } for i in handler_config[table_config_to_fetch]["sqlite_columns"])
    data.insert(0, 
        {
            "field": "id",
            "header": "ID",
            "display_type": "monotext"
        })
    
    for col in data:
        if not col["field"]:
            col["field"] = ''.join(filter(str.isalpha, col["header"]))

    return flask.jsonify({"data": data})
        
@APP.route("/fetch/data_rows")
def api_fetch_rows_data():
    handler_config = HANDLER.config
    table_config_to_fetch = flask.request.args.get("table")

    data = []
    column_names = list(i["sql_name"] for i in handler_config[table_config_to_fetch]["sqlite_columns"])
    rows = HANDLER.get_all_rows(table_config_to_fetch)

    for row in rows:
        tmp_row = {}
        for column_id, column_name in enumerate(column_names):
            tmp_row[column_name] = row[column_id+1]

        data.append(tmp_row)

    return flask.jsonify({"data": data})


@APP.route("/post/single_row", methods = ["POST"])
def api_post_single_row():
    table = flask.request.json["table"]
    row = flask.request.json["row"]
    HANDLER.insert_single_row(table, row)

