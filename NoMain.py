# no main
import customtkinter as ctk
from gui.ventana_usuarios import abrir_ventana_usuarios
from gui.ventana_eventos import abrir_ventana_eventos
from gui.ventana_asistencias import abrir_ventana_asistencias
from utils.orm_utils import crear_base_de_datos

def main():
    crear_base_de_datos()
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("JOIN UP")
    root.geometry("400x400")

    ctk.CTkLabel(root, text="Sistema de Eventos", font=("Arial", 24)).pack(pady=20)

    ctk.CTkButton(root, text="Usuarios", command=abrir_ventana_usuarios).pack(pady=10)
    ctk.CTkButton(root, text="Eventos", command=abrir_ventana_eventos).pack(pady=10)
    ctk.CTkButton(root, text="Asistencias", command=abrir_ventana_asistencias).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
