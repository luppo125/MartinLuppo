import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3



def mostrar_Notapedido(parent):
    ventana = tk.Toplevel(parent)
    ventana.title("Nota de pedido")
    ventana.state("zoomed")  # ← Maximizamos la ventana
    # ventana.geometry("800x600")  # ← Ya no es necesario si la ventana es maximizada