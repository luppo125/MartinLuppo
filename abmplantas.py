import abmplantascontrolador

def abrir_abm_planta(parent, conexion, modo, datos=None, on_guardar=None):
    """
    Función puente que invoca el controlador del formulario de Plantas.
    modo: 'agregar' | 'modificar'
    datos: (id, nombre) -> Solo se usa en modo modificar
    on_guardar: función callback para refrescar la tabla del listado
    """
    abmplantascontrolador.iniciar_abm_planta(
        parent=parent, 
        conexion=conexion, 
        modo=modo, 
        datos=datos, 
        on_guardar=on_guardar
    )