import sqlite3 as sql
import json
import os
import glob
from pathlib import Path
from tqdm import tqdm
import sys

class DBHandler:
    def __init__(
            self, 
            db_path: str = "testdb.db", 
            config_path: str = "configs"
        ):

        print(f"Relative path: {os.path.dirname(__file__)}")

        self.db_path = db_path
        self.config_path = config_path
        self.config = {}

        self.load_db_config()
        self.create_db_if_not_exists()
        for table in self.config.keys():
            self.create_table_if_not_exists(table)

    def load_db_config(self):
        print("Loading database config")
        configs = glob.glob(os.path.join(self.config_path, "*.json"))
        print(f"Found {len(configs)} configs: {configs}")
        for config in configs:
            table_name = Path(config).stem
            if table_name in self.config.keys():
                print(f"config {config} already loaded")
                #TODO config updating
            else:
                with open(config, "r") as f:
                    loaded_config = json.load(f)
                    self.config[table_name] = loaded_config
                    print(f"Loaded {table_name} config")

    def connect_to_db(self):
        self.conn = sql.connect(self.db_path)
        self.cursor = self.conn.cursor()
        print("Connected to db")

    def disconnect_from_db(self):
        self.conn.commit()
        self.conn.close()

    def create_db_if_not_exists(self):
        if not os.path.exists(self.db_path):
            with open(self.db_path, "w") as f:
                print("Created db")

    def create_table_if_not_exists(self, table: str):
        self.connect_to_db()

        column_names_and_types = []
        for column in self.config[table]["columns"]:
            if "create_sql" not in column.keys() or column["create_sql"]:
                column_names_and_types.append(" ".join([column["internal_name"], column["internal_type"]]))

        query = f"CREATE TABLE IF NOT EXISTS {table} (id INTEGER PRIMARY KEY AUTOINCREMENT, {','.join(column_names_and_types)})"
        self.cursor.execute(query)
        self.disconnect_from_db()

    def insert_single_row(self, table: str, row):
        self.connect_to_db()
        column_names = []
        for column in self.config[table]["columns"]:
            if "create_sql" not in column.keys() or column["create_sql"]:
                column_names.append(column["internal_name"])

        query = f"""
        INSERT INTO {table} ({','.join(column_names)}) VALUES ('{"','".join(row)}')
        """
        print(query, file=sys.stderr)
        self.cursor.execute(query)

        self.disconnect_from_db()

        

    def get_all_rows(self, table) -> list:
        self.connect_to_db()
        query = f"SELECT * FROM {table}"

        self.cursor.execute(query)

        out = self.cursor.fetchall()
        print(out, file=sys.stderr)
        return out


if __name__ == "__main__":
    handler = DBHandler()

    with open("utils/tmp.txt", "r") as f:
        x = f.read()
        for r in x.split("\\n"):
            handler.insert_single_row("clients", r.split("\\t"))

    print(handler.get_all_rows("clients"))
        

