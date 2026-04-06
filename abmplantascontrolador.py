from tkinter import messagebox
import plantasmodelo as modelo
import plantasvista as vista
import abmplantas  # El controlador del formulario de carga

def iniciar_abm_plantas(parent, conexion):
    # 1. Inicializar la interfaz (Vista)
    ventana = vista.crear_ventana(parent)
    botones = vista.crear_toolstrip(ventana)
    tree = vista.crear_tabla(ventana)

    # 2. Lógica para refrescar la tabla
    def cargar_datos():
        # Limpiamos la tabla antes de recargar
        tree.delete(*tree.get_children())
        # Traemos los datos desde el modelo
        for fila in modelo.obtener_plantas(conexion):
            tree.insert("", "end", values=fila)

    # 3. Funciones de Acción
    def agregar():
        # Llamamos al ABM en modo agregar
        abmplantas.abrir_abm_planta(
            parent=ventana,
            conexion=conexion,
            modo="agregar",
            on_guardar=cargar_datos  # Callback para refrescar la lista al terminar
        )

    def modificar():
        seleccionado = tree.focus()
        if not seleccionado:
            messagebox.showwarning("Atención", "Seleccione una planta para modificar", parent=ventana)
            return

        # Obtenemos los datos de la fila seleccionada (id, nombre)
        datos = tree.item(seleccionado)["values"]
        
        abmplantas.abrir_abm_planta(
            parent=ventana,
            conexion=conexion,
            modo="modificar",
            datos=datos,
            on_guardar=cargar_datos
        )

    def eliminar():
        seleccionado = tree.focus()
        if not seleccionado:
            messagebox.showwarning("Atención", "Seleccione una planta para eliminar", parent=ventana)
            return

        planta_id = tree.item(seleccionado)["values"][0]
        nombre = tree.item(seleccionado)["values"][1]

        # Confirmación de seguridad
        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar la planta '{nombre}'?\nLos sectores existentes no se borrarán pero quedarán sin referencia actualizada.", parent=ventana):
            try:
                modelo.eliminar_planta(conexion, planta_id)
                cargar_datos()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar: {e}", parent=ventana)

    # 4. Asignar los comandos a los botones de la vista
    botones["agregar"].config(command=agregar)
    botones["modificar"].config(command=modificar)
    botones["eliminar"].config(command=eliminar)
    botones["atras"].config(command=ventana.destroy)

    # 5. Carga inicial de datos al abrir
    cargar_datos()