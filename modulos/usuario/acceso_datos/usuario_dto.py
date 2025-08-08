from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UsuarioDTO(BaseModel):
    usuario_id: Optional[int] = None
    nombre: str
    email: str
    contrasena_hash: str
    fecha_registro: Optional[datetime] = datetime.now()
    moneda_preferida: Optional[str] = "COL"