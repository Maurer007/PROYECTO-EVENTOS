import customtkinter as ctk
from VentanaLogin import VentanaUsuario

class AlertaLogin(ctk.CTkToplevel):
    def __init__(self, parent, colorFondo="#1256E8"):
        super().__init__(parent)
        self.title("Alerta de Inicio de Sesión")
        self.parent = parent

        ancho_v = 400
        alto_v = 200
        x = (self.winfo_screenwidth() - ancho_v) // 2
        y = (self.winfo_screenheight() - alto_v) // 2
        self.geometry(f"{ancho_v}x{alto_v}+{x}+{y}")

        self.grab_set()
        
        self.configure(fg_color=colorFondo)
        self._set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.crear_frame_mensaje()
        self.crear_boton_cerrar()

    def crear_frame_mensaje(self, mensaje):
        frame_mensaje = ctk.CTkFrame(self, fg_color="transparent")
        frame_mensaje.pack(pady=20)

        label_mensaje = ctk.CTkLabel(frame_mensaje, text="Ups, necesitas iniciar sesión \npara continuar", font=("Arial", 16), text_color="white")
        label_mensaje.pack(pady=10)

    def crear_frame_boton(self):
        frame_boton = ctk.CTkFrame(self, fg_color="transparent")
        frame_boton.pack(pady=10)

        self.crear_boton(frame_boton, "Iniciar Sesión", self.abrir_login)
        self.crear_boton(frame_boton, "Cerrar", self.cerrar)
        
    def crear_boton(self, frame, texto, funcion):
        boton_cerrar = ctk.CTkButton(frame, text=texto, command=funcion)
        boton_cerrar.pack(pady=10)

    def abrir_login(self):
        print("Creando VentanaUsuario...")
        if hasattr(self, "ventana_usuario") and self.ventana_usuario.winfo_exists():
            print("Ya hay una ventana de usuario abierta.")
            return
        try:
            VentanaUsuario(self)
        except Exception as e:
            print("ERROR al crear VentanaUsuario:", e)

    def cerrar(self):
        self.destroy()