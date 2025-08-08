from modulos.usuario.acceso_datos.conexion import ConexionDB
from modulos.usuario.acceso_datos.usuario_dto import UsuarioDTO

conn = ConexionDB().obtener_conexion()

class UsuarioDAOMySQL:
    def guardar(self, usuario: UsuarioDTO) -> UsuarioDTO:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO usuarios (nombre, email, contrasena_hash, fecha_registro, moneda_preferida)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql,
                           (usuario.nombre,
                            usuario.email,
                            usuario.contrasena_hash,
                            usuario.fecha_registro,
                            usuario.moneda_preferida))
            usuario.usuario_id = cursor.lastrowid
        conn.commit()
        return usuario

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT usuario_id, nombre, email, contrasena_hash, fecha_registro, moneda_preferida FROM usuarios"
            )
            rows = cursor.fetchall()
        return [
            UsuarioDTO(usuario_id=r[0], nombre=r[1], email=r[2], contrasena_hash=r[3], fecha_registro=r[4], moneda_preferida=r[5])
            for r in rows
        ]

    def obtener_por_id(self, id: int):
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT usuario_id, nombre, email, contrasena_hash, fecha_registro, moneda_preferida FROM usuarios WHERE id = %s",
                (id)
            )
            row = cursor.fetchone()
        if row:
            return UsuarioDTO(id=row[0], nombre=row[1], email=row[2], contrasena_hash=row[3], fecha_registro=row[4], moneda_preferida=row[5])
        return None

    def actualizar(self, producto: UsuarioDTO):
        with conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE usuarios
                SET nombre=%s, email=%s, contrasena_hash=%s, fecha_registro=%s, moneda_preferida=%s
                WHERE usuario_id = %s
                """,
                (producto.nombre,
                 producto.email,
                 producto.contrasena_hash,
                 producto.fecha_registro,
                 producto.moneda_preferida,
                 producto.usuario_id)
            )
        conn.commit()

    def eliminar(self, id: int):
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM usuarios WHERE usuario_id = %s",
                (id,)
            )
        conn.commit()


# Para Postgres podrías copiar exactamente la misma clase y llamarla ProductoDAOPostgres,
# ya que psycopg2 usa también %s, o incluso usar esta misma si tu ConexionDB ya abstrae ambos.
class ProductoDAOPostgres(UsuarioDAOMySQL):
    pass
