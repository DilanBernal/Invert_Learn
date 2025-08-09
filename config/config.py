# config/config.py
import json
from pathlib import Path
from typing import Any, Dict

def cargar_configuracion(path: str = None) -> Dict[str, Any]:
    """
    Lee y devuelve la configuración JSON.
    Por defecto, busca 'config/db_config.json' en la raíz del proyecto.
    """
    if path is None:
        base = Path(__file__).parent.parent  # la carpeta raíz del proyecto
        path = base / "config" / "db_config.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
