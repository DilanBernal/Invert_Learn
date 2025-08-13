from fastapi.middleware.cors import CORSMiddleware
from modulos.usuario.logic.usuario_service import router as usuario_router
from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel

from modulos.gestion_gasto.logica.gestion_gasto_service import GastoService

app = FastAPI(title="InvertLearn – Gestión de Gastos")
service = GastoService()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Schemas para validación y serialización ---

class GastoIn(BaseModel):
    usuario_id: int
    categoria: str
    descripcion: Optional[str] = None
    monto: float

class GastoUpdate(BaseModel):
    categoria: str
    descripcion: Optional[str] = None
    monto: float

class GastoOut(GastoIn):
    transaccion_id: int
    fecha: str


# --- Endpoints de Gestión de gastos ---

@app.post(
    "/gestion_gasto/",
    response_model=GastoOut,
    status_code=201,
    summary="Crear un nuevo gasto"
)
def crear_gasto(payload: GastoIn):
    dto = service.crear_gasto(payload.dict())
    return dto.to_dict()


@app.get(
    "/gestion_gasto/",
    response_model=List[GastoOut],
    summary="Listar gastos de un usuario"
)
def listar_gastos(usuario_id: int = Query(..., description="ID del usuario")):
    lista = service.listar_gastos(usuario_id)
    return [dto.to_dict() for dto in lista]


@app.get(
    "/gestion_gasto/{transaccion_id}",
    response_model=GastoOut,
    summary="Obtener un gasto por su ID"
)
def obtener_gasto(transaccion_id: int):
    dto = service.obtener_gasto(transaccion_id)
    if not dto:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    return dto.to_dict()


@app.put(
    "/gestion_gasto/{transaccion_id}",
    response_model=GastoOut,
    summary="Actualizar un gasto existente"
)
def actualizar_gasto(transaccion_id: int, payload: GastoUpdate):
    # Validar si el gasto existe antes
    dto_existente = service.obtener_gasto(transaccion_id)
    if not dto_existente:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")

    # Actualizar usando los nuevos datos
    dto_actualizado = service.actualizar_gasto(transaccion_id, payload.dict())
    return dto_actualizado.to_dict()


@app.delete(
    "/gestion_gasto/{transaccion_id}",
    summary="Eliminar un gasto por su ID"
)
def eliminar_gasto(transaccion_id: int):
    dto = service.obtener_gasto(transaccion_id)
    if not dto:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    service.eliminar_gasto(transaccion_id)
    return {"status": "eliminado"}
  
app.include_router(usuario_router, prefix="/usuario")