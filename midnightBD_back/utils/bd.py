import sqlite3 as sql
import json
import os
import glob

class BDHandler:
    def __init__(
            self, 
            bd_path: str = "testbd.bd", 
            config_path: str = "configs"
        ):

        self.bd_path = bd_path
        self.config_path = config_path
        self.config = {}

        self.load_bd_config()
        self.create_bd_if_not_exists()
        for table in self.config.keys():
            self.create_table_if_not_exists()

    def load_bd_config(self):
        configs = glob.glob(f"{self.config}/*.json")
        for config in configs:
            table_name = config[:-5]
            if table_name in self.config.keys():
                print(f"config {config} already loaded")
                #TODO config updating
            else:
                with open(os.path.join(self.config_path, config), "r") as f:
                    loaded_config = json.load(f)
                    self.config[table_name] = loaded_config

    def connect_to_bd(self):
        self.conn = sql.connect(self.bd_path)
        self.cursor = self.conn.cursor()

    def create_bd_if_not_exists(self):
        if not os.path.exists(self.bd_path):
            with open(self.bd_path, "w") as f:
                pass

    def create_table_if_not_exists(self, table: str):
        self.connect_to_bd()
        column_names = [column["name"] for column in self.config[table]["sqlite_columns"]]
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {table} ({', '.join([column_names)})"
        )

