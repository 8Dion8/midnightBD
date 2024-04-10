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



@APP.route("/fetch/data_column_names")
def api_fetch_data_column_sql_names():
    handler_config = HANDLER.config
    table_config_to_fetch = flask.request.args.get("table")

    if flask.request.args.get("format_for_sql") == "0":
        data = list(i["sql_name"] for i in handler_config[table_config_to_fetch]["sqlite_columns"])

    else:
        data = list(
            {
                "prop": i["sql_name"],
                "name": i["display_name"],
            } for i in handler_config[table_config_to_fetch]["sqlite_columns"])

    return flask.jsonify({"data": data})
        
@APP.route("/fetch/data_rows")
def api_fetch_rows_data():
    handler_config = HANDLER.config
    table_config_to_fetch = flask.request.args.get("table")

    if flask.request.args.get("format_for_sql") == "0":
        pass
        #TODO
    else:
        data = []
        column_names = list(i["sql_name"] for i in handler_config[table_config_to_fetch]["sqlite_columns"])
        rows = HANDLER.get_all_rows(table_config_to_fetch)
        print("@@@@@@@@@@@@@@@@@@@@@@", rows)

        for row in rows:
            tmp_row = {}
            for column_id, column_name in enumerate(column_names):
                tmp_row[column_name] = row[column_id]

            data.append(tmp_row)

    return flask.jsonify({"data": data})

