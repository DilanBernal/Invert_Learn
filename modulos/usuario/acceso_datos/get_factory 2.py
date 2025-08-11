from modulos.usuario.config.config import cargar_configuracion
from modulos.usuario.acceso_datos.mysql_factory import MySQLUsuarioDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "mysql":
        return MySQLUsuarioDAOFactory()
    raise ValueError("Motor de base de datos no soportado")