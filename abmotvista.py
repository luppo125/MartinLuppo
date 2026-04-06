import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from principalvista import BASE_DIR
import os

ICON_PATH = os.path.join(BASE_DIR, "iconom.ico")


# =========================
# VENTANA
# =========================
def crear_ventana(parent):
    ventana = tk.Toplevel(parent)
    ventana.title("Orden de Trabajo")
    ventana.geometry("1920x900")
    ventana.configure(bg="#e8eef3")
    ventana.transient(parent)
    ventana.grab_set()

    if os.path.exists(ICON_PATH):
        try:
            ventana.iconbitmap(ICON_PATH)
        except Exception:
            pass

    return ventana


# =========================
# TOOLSTRIP
# =========================
def crear_toolstrip(ventana, estado_texto, comando_guardar, comando_cancelar):
    barra = tk.Frame(ventana, bg="#dde6ed", height=55)
    barra.pack(fill=tk.X)
    barra.pack_propagate(False)

    tk.Label(
        barra,
        text=estado_texto,
        bg="#dde6ed",
        fg="#003366",
        font=("Segoe UI", 11, "bold")
    ).pack(side=tk.LEFT, padx=15)

    tk.Button(
        barra,
        text="Cancelar",
        font=("Segoe UI", 10, "bold"),
        bg="#ffc7ce",
        fg="#9c0006",
        command=comando_cancelar
    ).pack(side=tk.RIGHT, pady=8)

    tk.Button(
        barra,
        text="Guardar",
        font=("Segoe UI", 10, "bold"),
        bg="#c6efce",
        fg="#006100",
        command=comando_guardar
    ).pack(side=tk.RIGHT, padx=10, pady=8)


# =========================
# FORMULARIO
# =========================
def crear_formulario(ventana):

    contenedor = tk.Frame(ventana, bg="#e8eef3")
    contenedor.pack(fill="both", expand=True, padx=20, pady=20)

    frm_pre = tk.LabelFrame(
        contenedor,
        text="Pre Resolución",
        bg="#e8eef3",
        font=("Segoe UI", 11, "bold")
    )
    frm_pre.pack(side="left", padx=20, anchor="n")

    frm_post = tk.LabelFrame(
        contenedor,
        text="Post Resolución / Cierre",
        bg="#e8eef3",
        font=("Segoe UI", 11, "bold")
    )
    frm_post.pack(side="left", padx=20, anchor="n")

    entradas = {}

    # =========================
    # PRE
    # =========================
    campos_pre = [
        "ID", "Codigo", "Version", "Mantenimiento correctivo",
        "Fecha", "Planta", "Sector", "Parte", "Nave", "Equipo",
        "Elemento", "Nombre del solicitante", "Area",
        "Descripcion del defecto", "Observaciones",
        "Prioridad", "Realizada"
    ]

    areas = [
        "Producción", "Calidad", "Depósito y Logística",
        "Seguridad", "Mantenimiento", "Otros"
    ]

    fila = 0
    for campo in campos_pre:

        tk.Label(
            frm_pre,
            text=f"{campo}:",
            bg="#e8eef3",
            font=("Segoe UI", 10)
        ).grid(row=fila, column=0, sticky="w", pady=4)

        if campo in ("Descripcion del defecto", "Observaciones"):
            widget = tk.Text(frm_pre, width=40, height=4)

        elif campo == "Fecha":
            widget = DateEntry(frm_pre, width=37, date_pattern="dd/mm/yyyy")

        elif campo == "Mantenimiento correctivo":
            widget = ttk.Combobox(
                frm_pre,
                values=["Correctivo inmediato", "Correctivo diferido", "Mejora"],
                state="readonly",
                width=37
            )

        elif campo == "Area":
            widget = ttk.Combobox(
                frm_pre,
                values=areas,
                state="readonly",
                width=37
            )

        elif campo in ("Planta", "Sector"):
            widget = ttk.Combobox(frm_pre, state="readonly", width=37)

        elif campo == "Prioridad":
            widget = ttk.Combobox(
                frm_pre,
                values=["BAJA", "MEDIA", "ALTA", "CRITICA"],
                state="readonly",
                width=37
            )

        elif campo == "Realizada":
            widget = ttk.Combobox(
                frm_pre,
                values=["NO", "SI"],
                state="readonly",
                width=37
            )

        else:
            widget = tk.Entry(frm_pre, width=40)

        widget.grid(row=fila, column=1, pady=4)
        entradas[campo] = widget
        fila += 1

    # =========================
    # POST
    # =========================
    campos_post = [
        "Solucion", "Fecha cierre ot", "Descripcion solucion",
        "Material utilizado", "NombreRealizo",
        "Aprobo solicitante", "Aprobo mant", "Aprobo calidad"
    ]

    soluciones = [
        "Mantenimiento mecánico",
        "Mantenimiento eléctrico",
        "Mantenimiento electrónico",
        "Mantenimiento edilicio",
        "Otro"
    ]

    fila = 0
    for campo in campos_post:

        tk.Label(
            frm_post,
            text=f"{campo}:",
            bg="#e8eef3",
            font=("Segoe UI", 10)
        ).grid(row=fila, column=0, sticky="w", pady=4)

        if campo == "Solucion":
            widget = ttk.Combobox(
                frm_post,
                values=soluciones,
                state="readonly",
                width=37
            )

        elif campo == "Descripcion solucion":
            widget = tk.Text(frm_post, width=45, height=4)

        elif campo.startswith("Aprobo"):
            widget = ttk.Combobox(
                frm_post,
                values=["NO", "SI"],
                state="readonly",
                width=37
            )

        elif campo == "Fecha cierre ot":
            widget = DateEntry(frm_post, width=37, date_pattern="dd/mm/yyyy")

        elif campo == "NombreRealizo":
            widget = ttk.Combobox(frm_post, state="readonly", width=37)

        else:
            widget = tk.Entry(frm_post, width=40)

        widget.grid(row=fila, column=1, pady=4)
        widget.configure(state="disabled")

        entradas[campo] = widget
        fila += 1

    return entradas


# =========================
# HELPERS
# =========================

def habilitar_campos(campos, lista_campos):
    for campo in lista_campos:
        widget = campos.get(campo)
        if widget:
            widget.configure(state="normal")


def deshabilitar_campos(campos, lista_campos):
    for campo in lista_campos:
        widget = campos.get(campo)
        if widget:
            widget.configure(state="disabled")


# ✅ FUNCION CORREGIDA Y ROBUSTA
def limpiar_campos(campos, lista_campos):

    for campo in lista_campos:

        widget = campos.get(campo)
        if not widget:
            continue

        try:
            # TEXT
            if isinstance(widget, tk.Text):
                widget.delete("1.0", "end")

            # DATEENTRY (tkcalendar)
            elif isinstance(widget, DateEntry):
                widget.delete(0, "end")

            # ENTRY / COMBOBOX
            elif hasattr(widget, "delete"):
                widget.delete(0, "end")

            elif hasattr(widget, "set"):
                widget.set("")

        except Exception:
            pass
