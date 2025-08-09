# modulos/gestion_gasto/logica/gestion_gasto_service.py

from typing import List, Optional
from modulos.gestion_gasto.acceso_datos.dao_factory import obtener_fabrica
from modulos.gestion_gasto.acceso_datos.gestion_gasto_dto import GastoDTO

class GastoService:
    def __init__(self):
        # obtenemos la fábrica apropiada y de ella sacamos el DAO
        fabrica = obtener_fabrica()
        self.dao = fabrica.get_gasto_dao()

    def crear_gasto(self, data: dict) -> GastoDTO:
        dto = GastoDTO(
            usuario_id  = data["usuario_id"],
            categoria   = data["categoria"],
            descripcion = data.get("descripcion", ""),
            monto       = data["monto"]
        )
        return self.dao.crear(dto)

    def listar_gastos(self, usuario_id: int) -> List[GastoDTO]:
        return self.dao.listar_por_usuario(usuario_id)

    def obtener_gasto(self, transaccion_id: int) -> Optional[GastoDTO]:
        return self.dao.buscar_por_id(transaccion_id)

    def actualizar_gasto(self, transaccion_id: int, data: dict) -> GastoDTO:
        dto = GastoDTO(
            transaccion_id = transaccion_id,
            categoria      = data["categoria"],
            descripcion    = data.get("descripcion", ""),
            monto          = data["monto"]
        )
        return self.dao.actualizar(dto)

    def eliminar_gasto(self, transaccion_id: int) -> None:
        self.dao.eliminar(transaccion_id)
