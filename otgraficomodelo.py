class OTGraficosModelo:

    def __init__(self, repositorio_ot):
        self.repo = repositorio_ot
        self.conexion = repositorio_ot.conexion

    # =====================================================
    # OBTENER TODAS LAS OT
    # =====================================================
    def obtener_todas(self):

        cursor = self.conexion.cursor()

        cursor.execute("""
            SELECT Fecha, Realizada, Planta, Sector
            FROM OT
        """)

        filas = cursor.fetchall()

        resultado = []

        for fila in filas:

            fecha_raw, realizada, planta, linea = fila

            fecha_dt = self.repo.fecha_segura(fecha_raw)

            if not fecha_dt:
                continue

            resultado.append({
                "fecha": fecha_dt,
                "cerrada": self.repo.texto_seguro(realizada),
                "planta": self.repo.texto_seguro(planta),
                "linea": self.repo.texto_seguro(linea)
            })

        return resultado

    # =====================================================
    # FILTRAR
    # =====================================================
    def filtrar(self, planta=None, linea=None, mes=None, anio=None):

        datos = self.obtener_todas()

        return self.repo.filtrar_lista(
            datos,
            planta,
            linea,
            mes,
            anio
        )

    # =====================================================
    # RESUMEN MENSUAL
    # =====================================================
    def resumen(self, planta=None, linea=None, mes=None, anio=None):

        ot_filtradas = self.filtrar(planta, linea, mes, anio)

        generadas = len(ot_filtradas)

        cerradas = sum(
            1 for x in ot_filtradas
            if self.repo.es_cerrada(x["cerrada"])
        )

        pendientes = generadas - cerradas

        porcentaje_cierre = (cerradas / generadas * 100) if generadas else 0

        return {
            "generadas": generadas,
            "cerradas": cerradas,
            "pendientes": pendientes,
            "porcentaje_cierre": round(porcentaje_cierre, 2)
        }

    # =====================================================
    # RESUMEN ANUAL
    # =====================================================
    def resumen_anual(self, planta=None, linea=None, anio=None):

        # Importante → SIN filtro mes
        datos = self.filtrar(planta, linea, None, anio)

        meses_nombre = [
            "Ene", "Feb", "Mar", "Abr", "May", "Jun",
            "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"
        ]

        generadas = [0] * 12
        cerradas = [0] * 12

        for ot in datos:

            mes_index = ot["fecha"].month - 1

            generadas[mes_index] += 1

            if self.repo.es_cerrada(ot["cerrada"]):
                cerradas[mes_index] += 1

        pendientes = [
            generadas[i] - cerradas[i]
            for i in range(12)
        ]

        return {
            "meses": meses_nombre,
            "generadas": generadas,
            "cerradas": cerradas,
            "pendientes": pendientes
        }
