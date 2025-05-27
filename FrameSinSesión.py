import customtkinter as ctk
from tkinter import *
from tkinter.ttk import Treeview, Style
from Sesion import usuario_actual
from VentanaLogin import VentanaUsuario

class SinSesión(ctk.CTkFrame):
    def __init__(self, parent, titulo):
        super().__init__(parent)
        self.parent = parent
        self.titulo = titulo
        
        self.configure(fg_color="#C4DF62")

        self.crear_titulo()
        self.crear_mensaje_login()    
        self.crear_boton_login()
        
    def crear_titulo(self):
        self.titulo = ctk.CTkLabel(self, text=self.titulo, font=("Eras Demi ITC", 75), text_color="#0A1A43")
        self.titulo.pack(pady=10)    

    def crear_mensaje_login(self):
        label = ctk.CTkLabel(
            self,
            text="Ups, necesitas iniciar sesión \npara continuar",
            font=("Arial", 80),  # Ajusta tamaño si era demasiado grande
            text_color="red",
            justify="center"
        )            
        label.pack(expand=True, fill="both")

    def crear_boton_login(self):
        boton = ctk.CTkButton(
            self,
            text="Iniciar Sesión",
            font=("Arial", 20),
            fg_color="#F27171",
            hover_color="red",
            command=self.abrir_login
        )
        boton.pack(pady=20)    

    def abrir_login(self):
        print("Creando VentanaUsuario...")
        if hasattr(self, "ventana_usuario") and self.ventana_usuario.winfo_exists():
            print("Ya hay una ventana de usuario abierta.")
            return
        try:
            VentanaUsuario(self)
        except Exception as e:
            print("ERROR al crear VentanaUsuario:", e)