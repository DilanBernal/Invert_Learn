import http.client
import json
import re
from typing import Optional, Dict, Any

SERVER_HOST = "localhost"
SERVER_PORT = 8000
BASE_URL = "/"


class UserManagerClient:
    def __init__(self, host: str = SERVER_HOST, port: int = SERVER_PORT):
        self.host = host
        self.port = port
        self.base_url = BASE_URL

    def make_request(self, method: str, endpoint: str, data: Optional[Dict[str, Any]] = None, max_redirects: int = 5) -> Optional[Dict[str, Any]]:
        """Realiza una petición HTTP al servidor con manejo de redirecciones"""
        redirects = 0
        current_host = self.host
        current_port = self.port
        current_endpoint = f"{self.base_url}{endpoint}"
        
        while redirects < max_redirects:
            connection = http.client.HTTPConnection(current_host, current_port)
            headers = {'Content-Type': 'application/json'}
            
            try:
                body = json.dumps(data) if data else None
                connection.request(method, current_endpoint, body=body, headers=headers)
                
                response = connection.getresponse()
                response_data = response.read().decode()
                
                # Manejar redirecciones (3xx)
                if 300 <= response.status < 400:
                    location = response.getheader('Location')
                    if location:
                        print(f"🔄 Siguiendo redirección a: {location}")
                        # Parsear la nueva ubicación
                        if location.startswith('http://') or location.startswith('https://'):
                            # URL completa
                            from urllib.parse import urlparse
                            parsed = urlparse(location)
                            current_host = parsed.hostname
                            current_port = parsed.port or (443 if parsed.scheme == 'https' else 80)
                            current_endpoint = parsed.path + (f"?{parsed.query}" if parsed.query else "")
                        else:
                            # URL relativa
                            current_endpoint = location
                        
                        redirects += 1
                        connection.close()
                        continue
                    else:
                        print(f"❌ Redirección sin Location header (HTTP {response.status})")
                        return None
                
                # Verificar código de estado HTTP (después de las redirecciones)
                if 200 <= response.status < 300:
                    return json.loads(response_data) if response_data else {"success": True}
                else:
                    print(f"❌ Error HTTP {response.status}: {response.reason}")
                    if response_data:
                        try:
                            error_data = json.loads(response_data)
                            print(f"   Detalle: {error_data.get('message', 'Sin detalles')}")
                        except json.JSONDecodeError:
                            print(f"   Respuesta: {response_data}")
                    return None
                    
            except http.client.HTTPException as e:
                print(f"❌ Error de conexión HTTP: {e}")
                return None
            except json.JSONDecodeError as e:
                print(f"❌ Error al procesar respuesta JSON: {e}")
                return None
            except Exception as e:
                print(f"❌ Error inesperado: {e}")
                return None
            finally:
                connection.close()
                
            break  # Si llegamos aquí, no hubo redirección
            
        if redirects >= max_redirects:
            print(f"❌ Demasiadas redirecciones ({max_redirects})")
            return None

    @staticmethod
    def validate_email(email: str) -> bool:
        """Valida formato de email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_password(password: str) -> bool:
        """Valida que la contraseña tenga al menos 6 caracteres"""
        return len(password) >= 6

    @staticmethod
    def get_safe_int(prompt: str) -> Optional[int]:
        """Solicita entrada de entero con validación"""
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Por favor ingresa un número válido")
            return None

    @staticmethod
    def get_safe_float(prompt: str) -> Optional[float]:
        """Solicita entrada de float con validación"""
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Por favor ingresa un número válido")
            return None

    def crear_usuario(self):
        """Crear un nuevo usuario"""
        print("\n=== CREAR USUARIO ===")
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("❌ El nombre no puede estar vacío")
            return

        email = input("Correo electrónico: ").strip()
        if not self.validate_email(email):
            print("❌ Formato de correo electrónico inválido")
            return

        contrasena = input("Contraseña: ").strip()
        if not self.validate_password(contrasena):
            print("❌ La contraseña debe tener al menos 6 caracteres")
            return

        contrasena_confirm = input("Confirmar contraseña: ").strip()
        if contrasena != contrasena_confirm:
            print("❌ Las contraseñas no coinciden")
            return

        moneda_preferida = input("Moneda preferida (ej: USD, EUR, MXN): ").strip().upper()
        if not moneda_preferida:
            print("❌ La moneda preferida no puede estar vacía")
            return
        
        data = {
            "nombre": nombre,
            "email": email, 
            "contrasena": contrasena,
            "moneda_preferida": moneda_preferida
        }
        
        print("⏳ Creando usuario...")
        response = self.make_request("POST", "usuario", data) 
        if response:
            print("✅ Usuario creado exitosamente:")
            print(f"   ID: {response.get('id', 'N/A')}")
            print(f"   Nombre: {response.get('nombre', 'N/A')}")
            print(f"   Email: {response.get('email', 'N/A')}")

    def ver_usuarios(self):
        """Ver todos los usuarios"""
        print("\n=== LISTA DE USUARIOS ===")
        print("⏳ Obteniendo usuarios...")
        usuarios = self.make_request("GET", "usuario")  
        
        if usuarios:
            if isinstance(usuarios, list) and usuarios:
                for i, usuario in enumerate(usuarios, 1):
                    print(f"\n{i}. Usuario ID: {usuario.get('id', 'N/A')}")
                    print(f"   Nombre: {usuario.get('nombre', 'N/A')}")
                    print(f"   Email: {usuario.get('email', 'N/A')}")
                    print(f"   Moneda: {usuario.get('moneda', 'N/A')}")
            else:
                print("📝 No hay usuarios registrados")
        else:
            print("❌ No se pudieron obtener los usuarios")

    def actualizar_usuario(self):
        """Actualizar un usuario existente"""
        print("\n=== ACTUALIZAR USUARIO ===")
        
        usuario_id = self.get_safe_int("ID del usuario a actualizar: ")
        if usuario_id is None:
            return

        print("Deja en blanco los campos que no quieras cambiar:")
        nombre = input("Nuevo nombre: ").strip()
        email = input("Nuevo email: ").strip()
        moneda = input("Nueva moneda preferida: ").strip().upper()

        # Validar email si se proporciona
        if email and not self.validate_email(email):
            print("❌ Formato de correo electrónico inválido")
            return

        # Construir datos solo con campos no vacíos
        data = {}
        if nombre:
            data["nombre"] = nombre
        if email:
            data["email"] = email
        if moneda:
            data["moneda_preferida"] = moneda

        if not data:
            print("❌ No se proporcionaron datos para actualizar")
            return

        print("⏳ Actualizando usuario...")
        response = self.make_request("PUT", f"usuario/{usuario_id}", data)  
        if response:
            print("✅ Usuario actualizado exitosamente")
        else:
            print("❌ No se pudo actualizar el usuario")

    def eliminar_usuario(self):
        """Eliminar un usuario"""
        print("\n=== ELIMINAR USUARIO ===")
        
        usuario_id = self.get_safe_int("ID del usuario a eliminar: ")
        if usuario_id is None:
            return

        confirmacion = input(f"¿Estás seguro de eliminar el usuario {usuario_id}? (s/N): ").strip().lower()
        if confirmacion != 's':
            print("❌ Operación cancelada")
            return

        print("⏳ Eliminando usuario...")
        response = self.make_request("DELETE", f"usuario/{usuario_id}")  # Cambiado a plural
        if response:
            print("✅ Usuario eliminado exitosamente")
        else:
            print("❌ No se pudo eliminar el usuario")



    def mostrar_menu_principal(self):
        """Mostrar menú principal"""
        print("\n" + "="*50)
        print("    INVERTLEARN – GESTOR DE USUARIOS")
        print("="*50)
        print("📋 GESTIÓN DE USUARIOS:")
        print("  1. Crear usuario")
        print("  2. Ver todos los usuarios")
        print("  3. Actualizar un usuario")
        print("  4. Eliminar un usuario")
        print("\n  0. Salir")
        print("="*50)

    def ejecutar(self):
        """Ejecutar el cliente"""
        print("🚀 Iniciando cliente del gestor de usuarios...")
        print(f"🔗 Conectando a {self.host}:{self.port}")

        while True:
            self.mostrar_menu_principal()
            opcion = input("Elige una opción (0-4): ").strip()

            if opcion == "1":
                self.crear_usuario()
            elif opcion == "2":
                self.ver_usuarios()
            elif opcion == "3":
                self.actualizar_usuario()
            elif opcion == "4":
                self.eliminar_usuario()
            elif opcion == "0":
                print("\n👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción inválida. Por favor elige una opción del 0 al 4.")

            # Pausa para que el usuario pueda leer la respuesta
            input("\nPresiona Enter para continuar...")


def main():
    """Función principal"""
    client = UserManagerClient()
    try:
        client.ejecutar()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")


if __name__ == "__main__":
    main()