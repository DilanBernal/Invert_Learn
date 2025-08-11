import json
from fastapi import APIRouter, Request, HTTPException, status
from datetime import datetime
from modulos.usuario.acceso_datos.usuario_dto import UsuarioDTO, UsuarioEditDTO
from modulos.usuario.acceso_datos.get_factory import obtener_fabrica

dao = obtener_fabrica().crear_dao()
router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def crear_usuario(req: Request):
  data = await req.json()
  try:
    if await dao.obtener_por_email(data["email"]) is not None:
      raise HTTPException(status_code=409, detail="El email ya está en uso.")
    usuario = UsuarioDTO(
      nombre=data["nombre"],
      email=data["email"],
      contrasena_hash=data["contrasena"],
      fecha_registro=datetime.now(),
      moneda_preferida=data["moneda_preferida"]
    ) 
    dao.guardar(usuario)
    return {"mensaje": "Usuario almacenado correctamente."}
  except KeyError as e:
    raise HTTPException(status_code=400, detail=f"Falta el campo: {e}")
  except HTTPException as e:
    raise e
  except Exception as e:
    raise HTTPException(status_code=502, detail=f"Error al guardar el usuario: {e}")

@router.get("/")
def obtener_usuarios():
  return [c.__dict__ for c in dao.obtener_todos()]

@router.get("/{id}")
async def obtener_usuario(id: int):
  usuario = await dao.obtener_por_id(id)
  if not usuario:
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
  return usuario.__dict__

@router.put("/{id}")
async def actualizar_usuario(id: int, req: Request):
  try:
    data = await req.json()
    if not data:
      raise HTTPException(status_code=400, detail="No se puede enviar vacio")
    
    if data.get("email") is not None:
      existing_email = await dao.obtener_por_email(data["email"])
      if existing_email is not None:
        if existing_email.usuario_id != id:
          raise HTTPException(status_code=403, detail="Otro usuario ya tiene el correo")
      
    user_data = await dao.obtener_por_id(id)
    
    actualizado = UsuarioDTO(
      id=id,
      nombre=data.get("nombre") or user_data.nombre,
      email=data.get("email") or user_data.email,
      contrasena_hash=data.get("contrasena") or user_data.contrasena_hash,
      fecha_registro=user_data.fecha_registro,
      moneda_preferida=data.get("moneda_preferida") or user_data.moneda_preferida
    )
    
    
    response = dao.actualizar(actualizado)
    return {"mensaje": f"Usuario actualizado ${response}"}
  except HTTPException as e:
    raise e
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{id}")
def eliminar_usuario(id: int):
  dao.eliminar(id)
  return {"mensaje": "Usuario eliminado"}