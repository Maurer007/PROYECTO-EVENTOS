import customtkinter as ctk
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import bcrypt
from models.usuario import Usuario
import Sesion

class InicioSesion(ctk.CTkFrame):
    def __init__(self, parent, colorFondo="#1256E8"):
        super().__init__(parent)
        self.parent = parent
        self.user = ""
        self.nombre=""
        self.apellido_p = ""
        self.apellido_m = ""

        self.configure(fg_color=colorFondo)
        self.obtener_credenciales()        

        self.crear_titulo()
        self.crear_label_usuario()
        self.crear_label_nombre()
        self.crear_label(
            f"Género: {self.genero}"
        )
        self.crear_label(    
            f"Fecha de nacimiento: {self.fecha_nacimiento}"
        )
        self.crear_label(
            f"Estado: {self.estado}"
        )
        self.crear_label(
            f"Ciudad: {self.ciudad}"
        )
        self.crear_label(
            f"Teléfono: {self.telefono}"
        )
        self.crear_label(
            f"Correo eléctrico: {self.correo}"
        )

        self.crear_boton_cerrar_sesion()
        

    def crear_titulo(self):
        self.titulo = ctk.CTkLabel(self, text="Ventana de Usuario", font=("Eras Demi ITC", 75), text_color="#0A1A43")
        self.titulo.pack(pady=10)

    def obtener_credenciales(self):
        from sqlalchemy.exc import SQLAlchemyError
        import Sesion  # Asegúrate de importar el módulo completo, no la variable directa

        engine = create_engine("sqlite:///db/app.db")
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            if not Sesion.usuario_actual:
                raise ValueError("No hay usuario en sesión.")

            # Recuperar el objeto completo del usuario
            self.user = session.query(Usuario).filter_by(nom_usuario=Sesion.usuario_actual).first()

            if self.user is None:
                raise ValueError(f"No se encontró el usuario '{Sesion.usuario_actual}' en la base de datos.")

            # Aquí puedes acceder a TODOS los campos del usuario
            self.nombre = self.user.nombre
            self.apellido_p = self.user.apellido_paterno
            self.apellido_m = self.user.apellido_materno
            self.genero = self.user.género
            self.fecha_nacimiento = self.user.fecha_nacimiento
            self.estado = self.user.estado
            self.ciudad = self.user.ciudad
            self.telefono = self.user.teléfono
            self.correo = self.user.correo

            # Puedes agregar más campos si tu modelo los tiene
            # self.email = self.user.email
            # self.telefono = self.user.telefono

        except (SQLAlchemyError, ValueError) as e:
            print("Error al obtener credenciales:", e)
            # Puedes mostrar un mensaje en la interfaz si quieres
            self.nombre = "No disponible"
            self.apellido_p = ""
            self.apellido_m = ""
            self.genero = ""
            self.fecha_nacimiento = ""
            self.estado = ""
            self.ciudad = ""
            self.telefono = ""
            self.correo = ""


    def crear_label_usuario(self):
        self.usuario = ctk.CTkLabel(self, text=f"Usuario: {self.user.nom_usuario}", font=("Arial", 40), text_color="black")
        self.usuario.pack(pady=10, anchor='w', padx=20)

    def crear_label_nombre(self):
        self.nombre_label = ctk.CTkLabel(self, text=f"Nombre completo: {self.nombre} {self.apellido_p} {self.apellido_m}", font=("Arial", 30), text_color="black")
        self.nombre_label.pack(pady=10, anchor='w', padx=20)

    def crear_label(self, texto):
        label = ctk.CTkLabel(self, text=texto, font=("Arial", 30), text_color="black")
        label.pack(pady=10, anchor='w', padx=20)

    def crear_boton_cerrar_sesion(self):
        self.boton_cerrar_sesion = ctk.CTkButton(self, text="Cerrar Sesión", command=self.cerrar_sesion, font=("Arial", 20), fg_color="#FF0000")
        self.boton_cerrar_sesion.pack(pady=20)

    def cerrar_sesion(self):
        Sesion.usuario_actual = None
        root = self.winfo_toplevel()
        
        # Restaurar el icono de usuario a su estado original
        if hasattr(root, "user") and hasattr(root, "iconos"):
            root.user.configure(image=root.iconos["user"])
        
        # Restaurar la vista anterior en lugar de ir siempre al main
        if hasattr(root, "restaurar_vista_anterior"):
            root.restaurar_vista_anterior()
        elif hasattr(root, "abrir_main"):
            root.abrir_main()
        
        print("Sesión cerrada.")
