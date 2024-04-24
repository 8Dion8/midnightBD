import flask
from flask_cors import CORS

from utils.db import DBHandler

from time import sleep

import sys

APP = flask.Flask("new_server")
CORS(APP)

HANDLER = DBHandler()

@APP.route("/")
def api_root():
    return "Hello, world!"

@APP.route("/ping")
def api_ping():
    return {"ping", "pong"}


@APP.route("/<table>/columns", methods = ["GET", "POST", "PATCH", "DELETE"])
def api_tables_columns(table):
    handler_config = HANDLER.config
    if flask.request.method == "GET":

        data = [{
            "field": "id",
            "header": "ID",
            "display_type": "monotext"
        }]

        for column in handler_config[table]["columns"]:
            data.append({
                "field": column["internal_name"],
                "header": column["display_name"],
                "display_type": column["display_type"]
            })

        return flask.jsonify({"data": data})


@APP.route("/<table>/rows", methods = ["GET", "POST", "PATCH", "DELETE"])
def api_tables_rows(table):
    handler_config = HANDLER.config

    if flask.request.method == "GET":
        data = []
        column_names = ["id"]
        for col in handler_config[table]["columns"]:
            if "create_sql" not in col.keys() or col["create_sql"]:
                column_names.append(col["internal_name"])
        raw_rows = HANDLER.get_all_rows(table)

        for row in raw_rows:
            tmp = {}
            for col_id, col_name in enumerate(column_names):
                tmp[col_name] = row[col_id] 

            data.append(tmp)
        
        return flask.jsonify({"data": data})
    
    elif flask.request.method == "POST":
        row = flask.request.json["row"]
        HANDLER.insert_single_row(table, row)


@APP.route("/<table>/config/<property>", methods = ["GET", "PATCH"])
def api_tables_config_table_display_type(table, property):
    handler_config = HANDLER.config
    return flask.jsonify({"data": handler_config[table][property]})

