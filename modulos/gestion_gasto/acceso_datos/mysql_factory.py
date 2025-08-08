from modulos.gestion_gasto.acceso_datos.gestion_gasto_dao import GastoDAO

class MySQLGastoDAOFactory:
    def get_gasto_dao(self):
        return GastoDAO()
