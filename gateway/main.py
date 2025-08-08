from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modulos.usuario.logic.usuario_service import router as usuario_router

app = FastAPI(title="API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(comentarios_router, prefix="/comentarios")
app.include_router(usuario_router, prefix="/usuario")