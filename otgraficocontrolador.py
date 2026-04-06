from otgraficomodelo import OTGraficosModelo
from otgraficovista import OTGraficosVista
from datetime import datetime


class OTGraficosControlador:

    def __init__(self, parent, repositorio_ot):

        self.repositorio = repositorio_ot
        self.modelo = OTGraficosModelo(self.repositorio)
        self.vista = OTGraficosVista(parent)

        # Conectar vista con controlador
        self.vista.set_controlador(self)

        # Modo inicial
        self.modo = "mensual"

        self.mes_actual = datetime.now().month
        self.anio_actual = datetime.now().year

        self._cargar_combos()
        self._conectar_eventos()
        self.cargar_datos()

    # ---------------------------------
    # CARGA DE COMBOS
    # ---------------------------------
    def _cargar_combos(self):

        todas = self.modelo.obtener_todas()

        if not todas:
            return

        # ---------------- MES ----------------
        self.vista.combo_mes["values"] = [""] + list(range(1, 13))
        self.vista.combo_mes.set("")

        # ---------------- AÑO ----------------
        anios = sorted({ot["fecha"].year for ot in todas if ot.get("fecha")})

        if anios:
            self.vista.combo_anio["values"] = anios
            self.vista.combo_anio.set(
                self.anio_actual if self.anio_actual in anios else anios[0]
            )

        # ---------------- PLANTA ----------------
        plantas = sorted({ot["planta"] for ot in todas if ot.get("planta")})
        self.vista.combo_planta["values"] = [""] + plantas
        self.vista.combo_planta.set("")

        # ---------------- LINEA ----------------
        lineas = sorted({ot["linea"] for ot in todas if ot.get("linea")})
        self.vista.combo_linea["values"] = [""] + lineas
        self.vista.combo_linea.set("")

    # ---------------------------------
    # EVENTOS
    # ---------------------------------
    def _conectar_eventos(self):

        self.vista.combo_mes.bind(
            "<<ComboboxSelected>>",
            lambda e: self.cargar_datos()
        )

        self.vista.combo_anio.bind(
            "<<ComboboxSelected>>",
            lambda e: self.cargar_datos()
        )

        self.vista.combo_planta.bind(
            "<<ComboboxSelected>>",
            lambda e: self.cargar_datos()
        )

        self.vista.combo_linea.bind(
            "<<ComboboxSelected>>",
            lambda e: self.cargar_datos()
        )

    # ---------------------------------
    # CAMBIAR MODO
    # ---------------------------------
    def cambiar_modo(self, modo):

        self.modo = modo

        # Deshabilitar mes si es anual
        if modo == "anual":
            self.vista.combo_mes.set("")
            self.vista.combo_mes.configure(state="disabled")
        else:
            self.vista.combo_mes.configure(state="readonly")

        self.cargar_datos()

    # ---------------------------------
    # OBTENER FILTROS
    # ---------------------------------
    def _obtener_filtros(self):

        # MES
        mes_valor = self.vista.combo_mes.get()
        mes = int(mes_valor) if mes_valor else None

        # AÑO
        anio_valor = self.vista.combo_anio.get()
        anio = int(anio_valor) if anio_valor else self.anio_actual

        # PLANTA
        planta = self.vista.combo_planta.get() or None

        # LINEA
        linea = self.vista.combo_linea.get() or None

        return planta, linea, mes, anio

    # ---------------------------------
    # CARGA DE DATOS
    # ---------------------------------
    def cargar_datos(self):

        try:

            planta, linea, mes, anio = self._obtener_filtros()

            # ==========================
            # MODO MENSUAL
            # ==========================
            if self.modo == "mensual":

                resumen = self.modelo.resumen(
                    planta=planta,
                    linea=linea,
                    mes=mes,
                    anio=anio
                )

                self.vista.mostrar_grafico_resumen(resumen)

            # ==========================
            # MODO ANUAL
            # ==========================
            elif self.modo == "anual":

                resumen = self.modelo.resumen_anual(
                    planta=planta,
                    linea=linea,
                    anio=anio
                )

                self.vista.mostrar_grafico_anual(resumen)

        except Exception as e:
            print("Error cargando gráficos:", e)
