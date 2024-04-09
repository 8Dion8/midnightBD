import sqlite3 as sql
import json
import os
import glob
from pathlib import Path

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

    def create_db_if_not_exists(self):
        if not os.path.exists(self.db_path):
            with open(self.db_path, "w") as f:
                print("Created db")

    def create_table_if_not_exists(self, table: str):
        self.connect_to_db()
        column_names_and_types = [column["sql_name"] + " " + column["type"] for column in self.config[table]["sqlite_columns"]]
        query = f"CREATE TABLE IF NOT EXISTS {table} (id INTEGER PRIMARY KEY AUTOINCREMENT, {', '.join(column_names_and_types)})"
        print(query)
        self.cursor.execute(query)


if __name__ == "__main__":
    handler = DBHandler()
