import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import os
from principalvista import BASE_DIR

ICON_PATH = os.path.join(BASE_DIR, "iconom.ico")


class OTGraficosVista:

    def __init__(self, parent):

        self.controlador = None

        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Gráficos OT")
        self.ventana.state("zoomed")
        self.ventana.iconbitmap(ICON_PATH)
        self._crear_toolstrip()
        self._crear_filtros()
        self._crear_grafico()

    # =========================================================
    # CONECTAR CONTROLADOR
    # =========================================================
    def set_controlador(self, controlador):
        self.controlador = controlador

    # =========================================================
    # TOOLSTRIP
    # =========================================================
    def _crear_toolstrip(self):

        toolstrip = tk.Frame(self.ventana, bg="#dde6ed")
        toolstrip.pack(fill=tk.X)

        fuente = ("Segoe UI", 12, "bold")
        fg = "#003366"
        bg = "#cfe2f3"
        hover = "#a4c2f4"

        def boton(texto, comando):
            return tk.Button(
                toolstrip,
                text=texto,
                font=fuente,
                fg=fg,
                bg=bg,
                activebackground=hover,
                activeforeground=fg,
                bd=0,
                relief="flat",
                command=comando
            )

        boton("Volver", self.ventana.destroy).pack(
            side=tk.LEFT, padx=10, pady=10
        )

        # BOTONES MODO
        self.btn_mensual = boton(
            "Resumen Mensual",
            lambda: self.controlador.cambiar_modo("mensual")
            if self.controlador else None
        )
        self.btn_mensual.pack(side=tk.LEFT, padx=5)

        self.btn_anual = boton(
            "Evolución Anual",
            lambda: self.controlador.cambiar_modo("anual")
            if self.controlador else None
        )
        self.btn_anual.pack(side=tk.LEFT, padx=5)

        tk.Frame(toolstrip, bg="#dde6ed").pack(
            side=tk.LEFT, expand=True, fill=tk.X
        )

    # =========================================================
    # FILTROS
    # =========================================================
    def _crear_filtros(self):

        frame = tk.Frame(self.ventana)
        frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame, text="Mes:").pack(side=tk.LEFT, padx=5)
        self.combo_mes = ttk.Combobox(frame, width=10, state="readonly")
        self.combo_mes.pack(side=tk.LEFT, padx=5)

        tk.Label(frame, text="Año:").pack(side=tk.LEFT, padx=5)
        self.combo_anio = ttk.Combobox(frame, width=10, state="readonly")
        self.combo_anio.pack(side=tk.LEFT, padx=5)

        tk.Label(frame, text="Planta:").pack(side=tk.LEFT, padx=5)
        self.combo_planta = ttk.Combobox(frame, width=15, state="readonly")
        self.combo_planta.pack(side=tk.LEFT, padx=5)

        tk.Label(frame, text="Línea:").pack(side=tk.LEFT, padx=5)
        self.combo_linea = ttk.Combobox(frame, width=15, state="readonly")
        self.combo_linea.pack(side=tk.LEFT, padx=5)

    # =========================================================
    # CREAR ÁREA GRÁFICO
    # =========================================================
    def _crear_grafico(self):

        self.frame_grafico = tk.Frame(self.ventana)
        self.frame_grafico.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.figura = Figure(figsize=(7, 4), dpi=100)
        self.ax = self.figura.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(
            self.figura,
            master=self.frame_grafico
        )

        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # =========================================================
    # HELPER VALORES SOBRE BARRAS
    # =========================================================
    def _agregar_valores_barras(self, barras):

        alturas = [barra.get_height() for barra in barras]
        max_valor = max(alturas) if alturas else 1

        for barra in barras:
            altura = barra.get_height()

            self.ax.text(
                barra.get_x() + barra.get_width() / 2,
                altura + max_valor * 0.02,
                f"{int(altura)}",
                ha="center",
                fontsize=9,
                fontweight="bold"
            )

    # =========================================================
    # GRÁFICO MENSUAL
    # =========================================================
    def mostrar_grafico_resumen(self, datos):

        self.ax.clear()

        etiquetas = ["Generadas", "Cerradas", "Pendientes"]

        valores = [
            datos.get("generadas", 0),
            datos.get("cerradas", 0),
            datos.get("pendientes", 0)
        ]

        colores = ["#4a90e2", "#50b96b", "#f5a623"]

        barras = self.ax.bar(etiquetas, valores, width=0.55, color=colores)

        self._agregar_valores_barras(barras)

        self.ax.set_title(
            f"Resumen OT | % Cierre: {datos.get('porcentaje_cierre', 0)}%",
            fontsize=14,
            fontweight="bold"
        )

        max_valor = max(valores + [1])
        self.ax.set_ylim(0, max_valor * 1.3)

        self.ax.grid(axis="y", linestyle="--", alpha=0.4)

        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)

        self.canvas.draw()

    # =========================================================
    # GRÁFICO ANUAL
    # =========================================================
    def mostrar_grafico_anual(self, datos):

        self.ax.clear()

        meses = datos["meses"]

        x = np.arange(len(meses))
        ancho = 0.25

        barras1 = self.ax.bar(x - ancho, datos["generadas"], ancho, label="Generadas")
        barras2 = self.ax.bar(x, datos["cerradas"], ancho, label="Cerradas")
        barras3 = self.ax.bar(x + ancho, datos["pendientes"], ancho, label="Pendientes")

        self._agregar_valores_barras(barras1)
        self._agregar_valores_barras(barras2)
        self._agregar_valores_barras(barras3)

        self.ax.set_xticks(x)
        self.ax.set_xticklabels(meses)

        self.ax.set_title("Evolución Anual OT", fontsize=14, fontweight="bold")
        self.ax.set_ylabel("Cantidad")

        max_valor = max(
            max(datos["generadas"]),
            max(datos["cerradas"]),
            max(datos["pendientes"]),
            1
        )

        self.ax.set_ylim(0, max_valor * 1.25)

        self.ax.legend()
        self.ax.grid(axis="y", linestyle="--", alpha=0.4)

        self.canvas.draw()
