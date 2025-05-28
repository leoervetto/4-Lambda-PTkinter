import tkinter as tk
from tkinter import ttk, messagebox

conversiones_longitud = {
    "metros": 1.0,
    "kilómetros": 1000.0,
    "centímetros": 0.01,
    "milímetros": 0.001,
    "pies": 0.3048,
    "yardas": 0.9144,
    "millas": 1609.34,
    "pulgadas": 0.0254
}




def abrir_ventana():
    ventana = tk.Toplevel()
    ventana.title("Conversión de Longitud")
    ventana.geometry("300x250")

