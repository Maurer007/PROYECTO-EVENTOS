import customtkinter as ctk
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import bcrypt
from models.evento import Evento
import Sesion

class DatosEventos(ctk.CTkFrame):
    def __init__(self, parent, colorFondo="#1256E8"):
        super().__init__(parent)
        self.anfitrion = None
        self.imagen = None
        self.tipo = None
        self.fecha = None
        self.hora = None
        self.direccion = None
        self.num_invitados = None
        self.privacidad = None
        self.privacidad_codigo = None
        self.cupo_limitado = None
        self.vestimenta_tipo = None

        self.descripcion = None

        self.cumpleañero = None
        self.edad = None
        self.mesa_regalos = None
        self.txt_mesa_regalos = None

        self.escuela = None
        self.nivel_educativo = None
        self.generacion = None
        self.invitados_por_alumno = None
        
        self.cumpleañero_xv = None
        self.padre = None
        self.madre = None
        self.padrino = None
        self.madrina = None
        self.mesa_regalos_xv = None
        self.txt_mesa_regalos_xv = None
        self.misa_xv = None
        self.iglesia_xv = None

        self.novia = None
        self.novio = None
        self.padrino_boda = None
        self.madrina_boda = None
        self.mesa_regalos_boda = None
        self.txt_mesa_regalos_boda = None
        self.misa = None
        self.iglesia = None
        self.menores_permitidos = None

        self.configure(fg_color=colorFondo)
        self.obtener_credenciales()        

        self.crear_titulo()
        self.obtener_datos_eventos()
        self.crear_frame_datos()
        self.crear_frame_imagen()

        self.crear_boton_cerrar_sesion()
        

    def crear_titulo(self):
        self.titulo = ctk.CTkLabel(self, text="Información del evento", font=("Eras Demi ITC", 75), text_color="#0A1A43")
        self.titulo.pack(pady=10)

    def obtener_datos_eventos(self):
        from sqlalchemy.exc import SQLAlchemyError
        import Sesion  # Asegúrate de importar el módulo completo, no la variable directa

        engine = create_engine("sqlite:///db/app.db")
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            self.evento = session.query(Evento).filter_by(id_evento=evento_seleccionado).first()

            if self.evento is None:
                raise ValueError(f"No se encontró el eventi '{evento_seleccionado}' en la base de datos.")

            self.anfitrion = self.evento.anfitrion
            self.imagen = self.evento.imagen_bytes
            self.tipo = self.evento.tipo_evento
            self.fecha = self.evento.fecha
            self.hora = self.evento.hora
            self.direccion = self.evento.direccion
            self.num_invitados = self.evento.num_invitados
            self.privacidad = self.evento.privacidad
            self.privacidad_codigo = self.evento.privacidad_codigo
            self.cupo_limitado = self.evento.cupo_limitado
            self.vestimenta_tipo = self.evento.vestimenta_tipo

            if self.tipo == "Fiesta":
                from models.evento import Fiesta
                self.fiesta = session.query(Fiesta).filter_by(id_evento=evento_seleccionado).first()
                self.descripcion = self.fiesta.descripcion
            elif self.tipo == "Cumpleaños":
                from models.evento import Cumpleaños
                self.cumpleaños = session.query(Cumpleaños).filter_by(id_evento=evento_seleccionado).first()
                self.cumpleañero = self.cumpleaños.cumpleañero
                self.edad = self.cumpleaños.edad
                self.mesa_regalos = self.cumpleaños.mesa_regalos
                self.txt_mesa_regalos = self.cumpleaños.txt_mesa_regalos
            elif self.tipo == "Graduación":
                from models.evento import Graduación
                self.graduacion = session.query(Graduación).filter_by(id_evento=evento_seleccionado).first()
                self.escuela = self.graduacion.escuela
                self.nivel_educativo = self.nivel_educativo
                self.generacion = self.graduacion.generacion
                self.invitados_por_alumno = self.graduacion.invitados_por_alumno
            elif self.tipo == "XV_años":
                from models.evento import XV_años
                self.xv_años = session.query(XV_años).filter_by(id_evento=evento_seleccionado).first()
                self.cumpleañero_xv = self.xv_años.cumpleañero_xv
                self.padre = self.xv_años.padre
                self.madre = self.xv_años.madre
                self.padrino = self.xv_años.padrino
                self.madrina = self.xv_años.madrina
                self.mesa_regalos_xv = self.xv_años.mesa_regalos_xv
                self.txt_mesa_regalos_xv = self.xv_años.txt_mesa_regalos_xv
                self.misa_xv = self.xv_años.misa_xv
                self.iglesia_xv = self.xv_años.iglesia_xv
            elif self.tipo == "Boda":
                from models.evento import Boda
                self.boda = session.query(Boda).filter_by(id_evento=evento_seleccionado).first()
                self.novia = self.boda.novia
                self.novio = self.boda.novio
                self.padrino_boda = self.boda.padrino_boda
                self.madrina_boda = self.boda.madrina_boda
                self.mesa_regalos_boda = self.boda.mesa_regalos_boda
                self.txt_mesa_regalos_boda = self.boda.txt_mesa_regalos_boda
                self.misa = self.boda.misa
                self.iglesia = self.boda.iglesia
                self.menores_permitidos = self.boda.menores_permitidos
                        

        except (SQLAlchemyError, ValueError) as e:
            print("Error al obtener credenciales:", e)
            # Puedes mostrar un mensaje en la interfaz si quieres
            self.anfitrion = ""
            self.imagen = ""
            self.tipo = ""
            self.fecha = ""
            self.hora = ""
            self.direccion = ""
            self.num_invitados = ""
            self.privacidad = ""
            self.privacidad_codigo = ""
            self.cupo_limitado = ""
            self.vestimenta_tipo = ""

    def crear_frame_datos(self):
        frame = ctk.CTkFrame(self, fg_color="#FFFFFF")
        frame.pack(padx=10, pady=10, fill='both', expand=True, side="left")

        self.crear_label(frame, f"Anfitrión: {self.anfitrion}")
        self.crear_label(frame, f"Tipo de evento: {self.tipo}")
        self.crear_label(frame, f"Fecha: {self.fecha}")
        self.crear_label(frame, f"Hora: {self.hora}")
        self.crear_label(frame, f"Dirección: {self.direccion}")
        self.crear_label(frame, f"Número de invitados: {self.num_invitados}")
        self.crear_label_checkbox(frame, self.privacidad, "Privacidad")
        if self.privacidad == "1":
            self.crear_label(frame, f"Código de privacidad: {self.privacidad_codigo}")
        self.crear_label(frame, f"Cupo: {self.cupo_limitado}")

    def crear_frame_imagen(self):
        frame = ctk.CTkFrame(self, fg_color="#FFFFFF")
        frame.pack(padx=10, pady=10, fill='both', expand=True, side="right")

        if self.imagen:
            from PIL import Image, ImageTk
            imagen = Image.open(self.imagen)
            imagen = imagen.resize((300, 300), Image.ANTIALIAS)
            self.imagen_tk = ImageTk.PhotoImage(imagen)
            label_imagen = ctk.CTkLabel(frame, image=self.imagen_tk)
            label_imagen.pack(pady=20)
        else:
            label_imagen = ctk.CTkLabel(frame, text="No hay imagen disponible", font=("Arial", 20), text_color="black")
            label_imagen.pack(pady=20)

    def crear_label(self, container, texto):
        label = ctk.CTkLabel(self, text=texto, font=("Arial", 30), text_color="black")
        label.pack(pady=10, anchor='w', padx=20)

    def crear_label_checkbox(self, container, checkbox, texto):
        if checkbox=="1":
            texto = f"{texto}: ✅"
        else:
            texto = f"{texto}: ❌"
        label = ctk.CTkLabel(container, text=texto, font=("Arial", 30), text_color="black")
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
