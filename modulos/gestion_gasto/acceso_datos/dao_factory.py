from modulos.gestion_gasto.acceso_datos.mysql_factory import MySQLGastoDAOFactory
# from modulos.gestion_gasto.acceso_datos.postgres_factory import PostgresGastoDAOFactory
import json
from pathlib import Path

def cargar_config():
    return json.loads((Path("config")/"db_config.json").read_text())

def obtener_fabrica():
    cfg = cargar_config()
    if cfg.get("db_engine") == "postgres":
        # return PostgresGastoDAOFactory()
        raise NotImplementedError
    return MySQLGastoDAOFactory()
