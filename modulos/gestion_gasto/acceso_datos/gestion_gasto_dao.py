from datetime import datetime
from modulos.gestion_gasto.acceso_datos.get_factory import get_connection
from modulos.gestion_gasto.acceso_datos.gestion_gasto_dto import GastoDTO

class GastoDAO:
    def __init__(self):
        self.conn  = get_connection()
        self.table = "transacciones"

    def crear(self, dto: GastoDTO) -> GastoDTO:
        sql = f"""
            INSERT INTO {self.table}
            (usuario_id, tipo, categoria, descripcion, monto)
            VALUES (%s, 'gasto', %s, %s, %s)
        """
        cur = self.conn.cursor()
        cur.execute(sql, (
            dto.usuario_id,
            dto.categoria,
            dto.descripcion,
            dto.monto
        ))
        self.conn.commit()
        dto.transaccion_id = cur.lastrowid
        dto.fecha          = datetime.now()
        cur.close()
        return dto

    def listar_por_usuario(self, usuario_id: int):
        sql = f"""
            SELECT transaccion_id, usuario_id, categoria,
                   descripcion, monto, fecha
            FROM {self.table}
            WHERE tipo='gasto' AND usuario_id=%s
            ORDER BY fecha DESC
        """
        cur = self.conn.cursor(dictionary=True)
        cur.execute(sql, (usuario_id,))
        rows = cur.fetchall()
        cur.close()
        return [GastoDTO.from_dict(r) for r in rows]

    def buscar_por_id(self, transaccion_id: int):
        sql = f"""
            SELECT transaccion_id, usuario_id, categoria,
                   descripcion, monto, fecha
            FROM {self.table}
            WHERE tipo='gasto' AND transaccion_id=%s
        """
        cur = self.conn.cursor(dictionary=True)
        cur.execute(sql, (transaccion_id,))
        row = cur.fetchone()
        cur.close()
        return GastoDTO.from_dict(row) if row else None

    def actualizar(self, dto: GastoDTO) -> GastoDTO:
        sql = f"""
            UPDATE {self.table}
            SET categoria=%s, descripcion=%s, monto=%s
            WHERE tipo='gasto' AND transaccion_id=%s
        """
        cur = self.conn.cursor()
        cur.execute(sql, (
            dto.categoria,
            dto.descripcion,
            dto.monto,
            dto.transaccion_id
        ))
        self.conn.commit()
        cur.close()

        # Retornar el gasto actualizado desde la base de datos con todos los campos
        return self.buscar_por_id(dto.transaccion_id)


    def eliminar(self, transaccion_id: int):
        sql = f"""
            DELETE FROM {self.table}
            WHERE tipo='gasto' AND transaccion_id=%s
        """
        cur = self.conn.cursor()
        cur.execute(sql, (transaccion_id,))
        self.conn.commit()
        cur.close()
