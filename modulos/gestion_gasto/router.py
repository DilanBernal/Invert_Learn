import json
import urllib.parse as up
from http.server import BaseHTTPRequestHandler, HTTPServer
from modulos.gestion_gasto.logica.gestion_gasto_service import GastoService

service = GastoService()

class RequestHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        # Listar gastos por usuario_id => /gestion_gasto/?usuario_id=1
        if self.path.startswith("/gestion_gasto/") and "?" in self.path:
            qs     = up.urlparse(self.path).query
            params = dict(up.parse_qsl(qs))
            if "usuario_id" in params:
                lista = service.listar_gastos(int(params["usuario_id"]))
                self._send_json([g.to_dict() for g in lista])
            else:
                self._send_json({"error":"Falta usuario_id"}, 400)

        # Obtener uno por ID => /gestion_gasto/1
        elif self.path.startswith("/gestion_gasto/"):
            _, _, id_str = self.path.rstrip("/").partition("/gestion_gasto/")
            gasto = service.obtener_gasto(int(id_str))
            if gasto:
                self._send_json(gasto.to_dict())
            else:
                self._send_json({"error":"No encontrado"}, 404)

        else:
            self._send_json({"error":"Ruta inválida"}, 404)

    def do_POST(self):
        if self.path == "/gestion_gasto/":
            length = int(self.headers.get("Content-Length","0"))
            body   = json.loads(self.rfile.read(length))
            gasto  = service.crear_gasto(body)
            self._send_json(gasto.to_dict(), 201)
        else:
            self._send_json({"error":"Ruta inválida"}, 404)

    def do_PUT(self):
        if self.path.startswith("/gestion_gasto/"):
            _, _, id_str = self.path.rstrip("/").partition("/gestion_gasto/")
            length = int(self.headers.get("Content-Length","0"))
            body   = json.loads(self.rfile.read(length))
            gasto  = service.actualizar_gasto(int(id_str), body)
            self._send_json(gasto.to_dict())
        else:
            self._send_json({"error":"Ruta inválida"}, 404)

    def do_DELETE(self):
        if self.path.startswith("/gestion_gasto/"):
            _, _, id_str = self.path.rstrip("/").partition("/gestion_gasto/")
            service.eliminar_gasto(int(id_str))
            self._send_json({"status":"eliminado"})
        else:
            self._send_json({"error":"Ruta inválida"}, 404)

def run(port=8001):
    print(f"Gestión de gastos escuchando en http://localhost:{port}")
    HTTPServer(("", port), RequestHandler).serve_forever()

if __name__ == "__main__":
    run()
