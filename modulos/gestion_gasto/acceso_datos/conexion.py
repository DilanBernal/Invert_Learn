# modulos/comun/acceso_datos/conexion.py

import json
import mysql.connector
import psycopg2
# importa aquí pymysql si lo usaras también...

class ConexionDB:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._crear_conexion()
        return cls._instancia

    def _crear_conexion(self):
        with open("config/db_config.json", "r", encoding="utf-8") as f:
            cfg = json.load(f)

        motor = cfg["db_engine"]
        if motor == "mysql":
            self.conexion = mysql.connector.connect(
                host=cfg["host"],
                port=cfg["port"],
                user=cfg["user"],
                password=cfg["password"],
                database=cfg["database"],
            )
        elif motor == "postgres":
            self.conexion = psycopg2.connect(
                host=cfg["host"],
                port=cfg["port"],
                user=cfg["user"],
                password=cfg["password"],
                dbname=cfg["database"],
            )
        else:
            raise ValueError(f"Motor no soportado: {motor}")

    def obtener_conexion(self):
        return self.conexion
