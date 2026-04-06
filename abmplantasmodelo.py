def insertar_planta(conexion, nombre):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO plantas (nombre) VALUES (?)", (nombre,))
    conexion.commit()

def modificar_planta(conexion, planta_id, nombre):
    cursor = conexion.cursor()
    cursor.execute("UPDATE plantas SET nombre = ? WHERE id = ?", (nombre, planta_id))
    conexion.commit()

def obtener_nombres_plantas(conexion):
    """Esta función la usaremos luego en el ABM de Sectores"""
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre FROM plantas ORDER BY nombre")
    return [fila[0] for fila in cursor.fetchall()]