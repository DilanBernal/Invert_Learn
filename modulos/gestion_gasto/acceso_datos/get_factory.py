import json
import mysql.connector

def get_connection():
    # Lee tu configuración de conexión
    with open("config/db_config.json", "r", encoding="utf-8") as f:
        cfg = json.load(f)

    # Conecta a MySQL usando mysql-connector-python
    return mysql.connector.connect(
        host=cfg["host"],
        port=cfg["port"],
        user=cfg["user"],
        password=cfg["password"],
        database=cfg["database"],
    )
