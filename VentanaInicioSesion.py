import customtkinter as ctk

class InicioSesion(ctk.CTkFrame):
    def __init__(self, parent, colorFondo="#1256E8"):
        super().__init__(parent)
        self.parent = parent

        self.configure(fg_color=colorFondo)
        

        self.crear_titulo()

    def crear_titulo(self):
        self.titulo = ctk.CTkLabel(self, text="Ventana de Usuario", font=("Eras Demi ITC", 75), text_color="#0A1A43")
        self.titulo.pack(pady=10)

    