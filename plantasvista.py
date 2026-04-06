import os
import tkinter as tk
from tkinter import ttk

# Usamos una ruta genérica para el icono para que sea comercializable
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ICON_PATH = os.path.join(BASE_DIR, "iconom.ico")

def crear_ventana(parent):
    ventana = tk.Toplevel(parent)
    ventana.title("Gestión de Plantas / Unidades")
    ventana.state("zoomed")
    ventana.configure(bg="#f0f4f8")
    ventana.transient(parent)
    ventana.grab_set()
    if os.path.exists(ICON_PATH):
        ventana.iconbitmap(ICON_PATH)
    return ventana

def crear_toolstrip(ventana):
    toolstrip = tk.Frame(ventana, bg="#dde6ed", height=70)
    toolstrip.pack(fill=tk.X, side=tk.TOP)
    toolstrip.pack_propagate(False)

    fuente = ("Segoe UI", 12, "bold")
    fg, bg, hover = "#003366", "#cfe2f3", "#a4c2f4"

    def boton(texto, x):
        b = tk.Button(toolstrip, text=texto, font=fuente, fg=fg, bg=bg,
                      activebackground=hover, bd=0, relief="flat")
        b.place(x=x, y=15, width=140, height=40)
        return b

    return {
        "agregar": boton("Agregar Planta", 10),
        "modificar": boton("Modificar", 160),
        "eliminar": boton("Eliminar", 310),
        "atras": boton("Cerrar", 460)
    }

def crear_tabla(ventana):
    contenedor = tk.Frame(ventana, bg="#f0f4f8")
    contenedor.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

    tree = ttk.Treeview(contenedor, columns=("id", "nombre"), show="headings")
    tree.heading("id", text="ID")
    tree.heading("nombre", text="Nombre de la Planta / Unidad")
    tree.column("id", width=100, anchor="center")
    tree.column("nombre", width=600)

    scroll_y = ttk.Scrollbar(contenedor, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll_y.set)

    tree.grid(row=0, column=0, sticky="nsew")
    scroll_y.grid(row=0, column=1, sticky="ns")
    contenedor.grid_rowconfigure(0, weight=1)
    contenedor.grid_columnconfigure(0, weight=1)

    return tree