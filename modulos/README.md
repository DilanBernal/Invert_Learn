# Carpeta de modulos inicial
En esta carpeta van los modulos por features segun la estructura
--
`
/modulos/nombre_modulo/
├── acceso_datos/
│   ├── nombre_dao.py
│   ├── nombre_dto.py
│   └── get_factory.py
├── logica/
│   └── nombre_service.py
└── notificaciones/ (opcional)

`

### Codigo para iniciar el gateway:
```
python -m uvicorn gateway.main:app --reload
```