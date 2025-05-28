import tkinter as tk
from tkinter import ttk

# Importamos los módulos de cada integrante del equipo
import longitud


def main():
    root = tk.Tk()
    root.title("Conversor de Unidades")
    root.geometry("400x300")
    
    ttk.Label(root, text="Conversor de Unidades", font=("Arial", 16)).pack(pady=20)

    # Botones para abrir cada submódulo
    ttk.Button(root, text="Conversión de Longitud", command=longitud.abrir_ventana).pack(pady=5)
    


    ttk.Label(root, text="© Proyecto de Informatorio", font=("Arial", 10)).pack(side="bottom", pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()