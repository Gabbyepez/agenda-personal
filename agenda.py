import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Para el DatePicker

# Lista donde se guardan los eventos
eventos = []

# ---------------- FUNCIONES ----------------

def agregar_evento():
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()

    if fecha == "" or hora == "" or descripcion == "":
        messagebox.showwarning("Error", "Todos los campos son obligatorios")
        return

    # Insertar en la tabla
    tabla.insert("", "end", values=(fecha, hora, descripcion))

    # Limpiar campos
    entrada_hora.delete(0, tk.END)
    entrada_descripcion.delete(0, tk.END)


def eliminar_evento():
    seleccionado = tabla.selection()

    if not seleccionado:
        messagebox.showwarning("Error", "Seleccione un evento para eliminar")
        return

    confirmacion = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento?")

    if confirmacion:
        for item in seleccionado:
            tabla.delete(item)


def salir():
    ventana.quit()


# ---------------- VENTANA PRINCIPAL ----------------

ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")

# ---------------- FRAMES ----------------

frame_tabla = tk.Frame(ventana)
frame_tabla.pack(pady=10)

frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# ---------------- TABLA (TreeView) ----------------

columnas = ("Fecha", "Hora", "Descripción")

tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=150)

tabla.pack()

# ---------------- ENTRADAS ----------------

# Fecha
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
entrada_fecha = DateEntry(frame_entrada)
entrada_fecha.grid(row=0, column=1)

# Hora
tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
entrada_hora = tk.Entry(frame_entrada)
entrada_hora.grid(row=1, column=1)

# Descripción
tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
entrada_descripcion = tk.Entry(frame_entrada)
entrada_descripcion.grid(row=2, column=1)

# ---------------- BOTONES ----------------

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=5)

# ---------------- EJECUCIÓN ----------------

ventana.mainloop()