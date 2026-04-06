import os
import sys

def obtener_ruta_base():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def obtener_ruta_db(): # <--- Asegurate que NO tenga (planta) aquí
    base_path = obtener_ruta_base()
    return os.path.join(base_path, "MANTENIMIENTO.db")