import tkinter as tk
from tkinter import messagebox
from modulos.gestion_gasto.logica.gestion_gasto_service import GastoService

service = GastoService()

def crear_gasto():
    try:
        data = {
            "usuario_id": int(usuario_entry.get()),
            "categoria": categoria_entry.get(),
            "descripcion": descripcion_entry.get(),
            "monto": float(monto_entry.get())
        }
        gasto = service.crear_gasto(data)
        messagebox.showinfo("Éxito", f"Gasto creado:\n{gasto.to_dict()}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# UI
ventana = tk.Tk()
ventana.title("InvertLearn – Gestor de Gastos")
ventana.geometry("400x300")

tk.Label(ventana, text="Usuario ID").pack()
usuario_entry = tk.Entry(ventana)
usuario_entry.pack()

tk.Label(ventana, text="Categoría").pack()
categoria_entry = tk.Entry(ventana)
categoria_entry.pack()

tk.Label(ventana, text="Descripción").pack()
descripcion_entry = tk.Entry(ventana)
descripcion_entry.pack()

tk.Label(ventana, text="Monto").pack()
monto_entry = tk.Entry(ventana)
monto_entry.pack()

tk.Button(ventana, text="Crear gasto", command=crear_gasto).pack(pady=10)

ventana.mainloop()
