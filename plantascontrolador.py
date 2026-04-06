from tkinter import messagebox
import plantasmodelo as modelo
import plantasvista as vista
import abmplantas  # Importamos el puente para abrir el formulario

def iniciar_plantas(parent, conexion):
    # 1. Preparar la interfaz (Vista)
    ventana = vista.crear_ventana(parent)
    botones = vista.crear_toolstrip(ventana)
    tree = vista.crear_tabla(ventana)

    # 2. Lógica de carga de datos
    def cargar_datos():
        # Limpiamos el Treeview antes de cargar
        tree.delete(*tree.get_children())
        # Traemos los datos desde el modelo de plantas
        for fila in modelo.obtener_plantas(conexion):
            tree.insert("", "end", values=fila)

    # 3. Funciones de acción conectadas al ABM
    def agregar():
        # Llamamos al puente en modo agregar
        abmplantas.abrir_abm_planta(
            parent=ventana,
            conexion=conexion,
            modo="agregar",
            on_guardar=cargar_datos  # Refresca la tabla al guardar
        )

    def modificar():
        # Obtenemos la selección actual
        seleccionado = tree.focus()
        if not seleccionado:
            messagebox.showwarning("Atención", "Seleccione una planta para modificar", parent=ventana)
            return

        # Sacamos los datos de la fila (id, nombre)
        datos = tree.item(seleccionado)["values"]
        
        # Llamamos al puente en modo modificar
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

        # Obtenemos ID y Nombre para la confirmación
        item = tree.item(seleccionado)["values"]
        planta_id = item[0]
        nombre = item[1]

        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar la planta '{nombre}'?\nEsto no borrará los sectores, pero quedarán sin referencia.", parent=ventana):
            try:
                modelo.eliminar_planta(conexion, planta_id)
                cargar_datos()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar: {e}", parent=ventana)

    # 4. Asignación de comandos a los botones
    botones["agregar"].config(command=agregar)
    botones["modificar"].config(command=modificar)
    botones["eliminar"].config(command=eliminar)
    botones["atras"].config(command=ventana.destroy)

    # Carga inicial
    cargar_datos()