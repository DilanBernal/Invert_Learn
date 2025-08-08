from modulos.gestion_gasto.logica.gestion_gasto_service import GastoService  # ✅ Correcto

def main():
    service = GastoService()

    print("=== INVERTLEARN – GESTOR DE GASTOS ===")
    print("1. Crear gasto")
    print("2. Ver gastos de un usuario")
    print("3. Actualizar gasto")
    print("4. Eliminar gasto")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        usuario_id = int(input("ID del usuario: "))
        categoria = input("Categoría: ")
        descripcion = input("Descripción: ")
        monto = float(input("Monto: "))

        data = {
            "usuario_id": usuario_id,
            "categoria": categoria,
            "descripcion": descripcion,
            "monto": monto
        }

        gasto = service.crear_gasto(data)
        print("✅ Gasto creado:", gasto.to_dict())

    elif opcion == "2":
        usuario_id = int(input("ID del usuario: "))
        gastos = service.listar_gastos(usuario_id)
        for g in gastos:
            print(g.to_dict())

    elif opcion == "3":
        transaccion_id = int(input("ID del gasto a actualizar: "))
        categoria = input("Nueva categoría: ")
        descripcion = input("Nueva descripción: ")
        monto = float(input("Nuevo monto: "))

        data = {
            "usuario_id": 0,  # no se usa en actualizar
            "categoria": categoria,
            "descripcion": descripcion,
            "monto": monto
        }

        gasto = service.actualizar_gasto(transaccion_id, data)
        if gasto:
            print("✅ Gasto actualizado:", gasto.to_dict())
        else:
            print("❌ Gasto no encontrado.")

    elif opcion == "4":
        transaccion_id = int(input("ID del gasto a eliminar: "))
        service.eliminar_gasto(transaccion_id)
        print("✅ Gasto eliminado")

    elif opcion == "0":
        print("👋 Hasta luego.")
    else:
        print("❌ Opción inválida")

if __name__ == "__main__":
    main()
