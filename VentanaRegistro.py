import os
import sqlite3
from tkinter import filedialog
import bcrypt
import customtkinter as ct
from PIL import Image
import tkinter as tk
from tkcalendar import DateEntry
from datetime import date
from sqlalchemy.exc import SQLAlchemyError
from utils.orm_utils import Session
from models.usuario import Usuario 
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import bcrypt

class UsuarioManager:

    @staticmethod
    def registrar_usuario(nombre, apellido_paterno, apellido_materno, género, ciudad, estado, fecha_nacimiento, nom_usuario, contraseña, teléfono, correo):
        session = Session()
        try:

            hashed_password = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            nuevo_usuario = Usuario(
                nombre=nombre,
                apellido_paterno=apellido_paterno,
                apellido_materno=apellido_materno,
                ciudad=ciudad,
                estado=estado,
                género=género,
                fecha_nacimiento=fecha_nacimiento,
                nom_usuario=nom_usuario,
                contraseña=hashed_password,
                teléfono=teléfono,
                correo=correo
            )

            session.add(nuevo_usuario)
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error al registrar usuario: {e}")
        finally:
            session.close()

class VentanaRegistro(ct.CTkToplevel):
    def __init__(self, menu, textlb = "Registro de usuarios", textE1 = "Nombre", textE2 = "Apellidos", textE3 = "E-mail", textE4 = "Usuario", textE5 = "Contraseña", textE6 = "Confirmar Contraseña", textB1 = "Registrar", textB2 = "Volver", colorFondo="black"):
        super().__init__(menu)
        self.title("Registro")
        self.menu=menu

        ancho_v = 800
        alto_v = 600
        x = (self.winfo_screenwidth() - ancho_v) // 2
        y = (self.winfo_screenheight() - alto_v) // 2
        self.geometry(f"{ancho_v}x{alto_v}+{x}+{y}")

        self.grab_set()

        #self.resizable(False, False)
        self.overrideredirect(True)
        frame_top = ct.CTkFrame(self, height=30, corner_radius=0, fg_color=colorFondo)
        frame_top.pack(fill="x")
        self.close_button = ct.CTkButton(frame_top, text="X", width=30, font=("Arial", 30), command=self.cerrar,
                                         fg_color="black", hover_color="black", text_color_disabled="gray")
        self.close_button.pack(side="right", padx=5, pady=2)
        self.close_button.bind("<Enter>", self.on_enter)
        self.close_button.bind("<Leave>", self.on_leave)
        self.attributes("-topmost", True)

        self.configure(fg_color=  colorFondo)
        self._set_appearance_mode("dark")
        self.rowconfigure(1, weight=1)

        self.nombre=""
        self.apellido_paterno=""
        self.apellido_materno=""
        self.estado=""
        self.municipio=""
        self.seleccion = ct.StringVar(value="")
        self.nom_usuario=""
        self.contrasena=""
        self.telefono=""
        self.correo=""
        self.frame_principal = self.crear_scrollable_frame()

        self.frame_titulo = self.crear_frame_titulo(self.frame_principal)

        self.datos_personales = self.crear_frame_datos(self.frame_principal, "Datos personales")
        self.crear_datos_personales(self.datos_personales)

        self.datos_usuario = self.crear_frame_datos(self.frame_principal, "Datos de usuario")
        self.crear_datos_usuario(self.datos_usuario)

        self.frme_botones = self.crear_frame_botones(self.frame_principal)

        self.withdraw()
        self.deiconify()

        #self.labelError = ct.CTkLabel(self.container9, text="", font=("Arial", 15), text_color="red")
        #self.labelError.pack(expand=True, anchor="center")

        #self.crearTablaBD()

    def crear_scrollable_frame(self):
        container1 = ct.CTkScrollableFrame(self, fg_color="transparent")
        container1.pack(padx=10, pady=10, fill="both", expand=True)

        return container1

    def crear_frame_titulo(self, scrollable_frame):
        frame = ct.CTkFrame(scrollable_frame, fg_color="transparent")
        frame.pack(padx=10, pady=10, fill="both")

        lbTitulo = ct.CTkLabel(frame, text="JOIN UP", text_color="#df0f69", font=("Eras Bold ITC", 70))
        lbTitulo.pack(expand=True, anchor="center")

        lbSubtitulo = ct.CTkLabel(frame, text="Registro de usuario", text_color="white", font=("Arial", 30))
        lbSubtitulo.pack(expand=True, anchor="center")

        return frame

    def crear_frame_datos(self, scrollable_frame, tipo_datos):
        frame = ct.CTkFrame(scrollable_frame, fg_color="#D9D9D9", corner_radius=16)
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        lbDatos = ct.CTkLabel(frame, text=tipo_datos, text_color="black", font=("Arial", 24))
        lbDatos.pack(padx=10, pady=10, anchor="w")

        frame_datos = ct.CTkFrame(frame, fg_color="#B5B2CA", border_color="white", border_width=3, corner_radius=16)
        frame_datos.pack(pady=10, padx=10, anchor="center", fill="both", expand=True)
        frame_datos.grid_columnconfigure((0,1,2,3,4,5,6,7), weight=1)

        return frame_datos
    
    #Todos los campos de datos personales
    def crear_datos_personales(self, frame_datos):
        self.nombre=self.crear_entry_arriba(frame_datos, 0, "Nombre")
        self.apellido_paterno=self.crear_entry_arriba(frame_datos, 2, "Apellido Paterno")
        self.apellido_materno=self.crear_entry_arriba(frame_datos, 4, "Apellido Materno")
        self.crear_frame_radios(frame_datos)
        self.crear_frame_fecha(frame_datos)
        self.crear_frame_municipio(frame_datos)

    def crear_entry_arriba(self, frame_datos, columna, texto):
        entrada = ct.CTkEntry(frame_datos, text_color="black", font=("Arial", 20), fg_color="white")
        entrada.grid(row=0, column=columna, columnspan=2, pady=10, padx=10)

        label = ct.CTkLabel(frame_datos, text=texto, text_color="black", font=("Arial", 20))
        label.grid(row=1, column=columna, columnspan=4, pady=10, padx=10, sticky="w")

        return entrada
    def crear_radios(self, frame_radios, columna, texto, valor):
        print("DEBUG seleccion:", self.seleccion)
        radio = ct.CTkRadioButton(frame_radios, text=texto, text_color="black", variable=self.seleccion, value=valor)
        radio.grid(row=1, column=columna, pady=10, padx=10)
        return radio
    
    def crear_frame_radios(self, frame_datos):
        frameRadios = ct.CTkFrame(frame_datos, fg_color="white")
        frameRadios.grid(row=2, column=0, columnspan=4, pady=10, padx=10)

        label = ct.CTkLabel(frameRadios, text="Género", text_color="black", font=("Arial", 20))
        label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        radio_hombre = self.crear_radios(frameRadios, 0, "Hombre", "Hombre")
        radio_mujer = self.crear_radios(frameRadios, 1, "Mujer", "Mujer")
        radio_otro = self.crear_radios(frameRadios, 2, "Otro", "Otro")
    

    def crear_frame_fecha(self, frame_datos):
        frameFecha = ct.CTkFrame(frame_datos, fg_color="white")
        frameFecha.grid(row=2,column=4, columnspan=4, pady=10, padx=10, sticky="nsew")

        label = ct.CTkLabel(frameFecha, text="Fecha de nacimiento", text_color="black", font=("Arial", 20))
        label.grid(row=0, column=0, pady=10, padx=10)

        self.date_entry = DateEntry(frameFecha, width=16, background='#D9D9D9',
                       date_pattern='y-mm-dd', mindate=date(1900, 1, 1), maxdate=date.today())
        self.date_entry.grid(row=1, column=0, pady=10, padx=10)

    def crear_frame_municipio(self, frame_datos):
        frame = ct.CTkFrame(frame_datos, fg_color="transparent")
        frame.grid(row=3, column=0, columnspan=8, pady=10, padx=10)

        self.estado=self.crear_entry(frame, 0, "Estado")
        self.municipio=self.crear_entry(frame, 4, "Municipio")

    def crear_entry(self, frame_municipio, columna, texto):
        label = ct.CTkLabel(frame_municipio, text=texto, text_color="black", font=("Arial", 20))
        label.grid(row=0, column=columna, pady=10, padx=10, sticky="w")

        entrada = ct.CTkEntry(frame_municipio, text_color="black", font=("Arial", 20), fg_color="white")
        entrada.grid(row=0, column=columna+1, columnspan=3, pady=10, padx=10)

        return entrada

    # Todos los campos de datos de usuario
    def crear_datos_usuario(self, frame_datos):
        self.nom_usuario=self.crear_entry_derecha(frame_datos, 0, 0, "Nombre de usuario")
        self.nom_usuario_var = tk.StringVar()
        self.nom_usuario.configure(textvariable=self.nom_usuario_var)
        self.nom_usuario_var.trace_add("write", self.verificar_usuario_en_tiempo_real)
        self.labelError_usuario = self.crear_label_error(frame_datos, 0)

        self.contrasena=self.crear_entry_derecha(frame_datos, 1, 0, "Contraseña")
        self.crear_entry_derecha(frame_datos, 2, 0, "Confirmar contraseña")
        self.labelError_contraseña = self.crear_label_error(frame_datos, 2)
        self.telefono=self.crear_entry_derecha(frame_datos, 3, 0, "Teléfono")
        self.correo=self.crear_entry_derecha(frame_datos, 4, 0, "Correo electrónico")

    def crear_entry_derecha(self, frame_datos, fila, columna, texto):
        label = ct.CTkLabel(frame_datos, text=texto, text_color="black", font=("Arial", 20))
        label.grid(row=fila, column=columna, columnspan=2, pady=10, padx=10, sticky="w")

        entrada = ct.CTkEntry(frame_datos, text_color="black", font=("Arial", 20), fg_color="white")
        entrada.grid(row=fila, column=columna+2, columnspan=2, pady=10, padx=10, sticky="nsew")

        return entrada
    
    def crear_label_error(self, frame_datos, fila):
        labelError = ct.CTkLabel(frame_datos, text="", font=("Arial", 15), text_color="red")
        labelError.grid(row=fila, column=4, columnspan=2, pady=10, padx=10, sticky="w")

        return labelError

    def verificar_usuario_en_tiempo_real(self, *args):
        engine = create_engine("sqlite:///db/app.db")  # Usa la ruta correcta de tu base
        Session = sessionmaker(bind=engine)
        session = Session()

        username = self.nom_usuario_var.get().strip()
        user = session.query(Usuario).filter_by(nom_usuario=username).first()

        if username and user:
            self.labelError_usuario.configure(text="El nombre de usuario ya existe")
        else:
            self.labelError_usuario.configure(text="")

        session.close()



    # Creación de botones
    def crear_frame_botones(self, scrollable_frame):
        frame = ct.CTkFrame(scrollable_frame, fg_color="transparent")
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.crear_boton(frame, "Volver", "left", self.volver)
        self.crear_boton(frame, "Registrar", "right", self.on_registrar)

        return frame
        
    def crear_boton(self, frame_botones, texto, lado, comando):
        self.boton = ct.CTkButton(frame_botones, font=("Arial", 20), text=texto, command=comando)
        self.boton.pack(pady=10, side=lado, expand=True)


    def on_enter(self, event):
        self.close_button.configure(text_color="red")  # O fg_color si solo cambia el texto

    def on_leave(self, event):
        self.close_button.configure(text_color="SystemButtonFace")  # O el color que usabas antes

    def on_registrar(self):

        print("on_registrar seleccion:", self.seleccion)
        if self.seleccion is None:
            print("ERROR: self.seleccion es None antes de get()")
        else:
            genero = self.seleccion.get()
            print("Genero seleccionado:", genero)

        nombre = self.nombre.get()
        apellido_paterno = self.apellido_paterno.get()
        apellido_materno = self.apellido_materno.get()
        género = self.seleccion.get()
        ciudad = self.municipio.get()
        estado = self.estado.get()
        fecha_nacimiento = self.date_entry.get_date()
        nom_usuario = self.nom_usuario.get()
        contraseña = self.contrasena.get()
        teléfono = self.telefono.get()
        correo = self.correo.get()
        

        exito = UsuarioManager.registrar_usuario(
            nombre, apellido_paterno, apellido_materno,
            género, ciudad, estado, fecha_nacimiento,
            nom_usuario, contraseña, teléfono, correo)
        
        self.volver()

    def volver(self):
        from VentanaLogin import VentanaUsuario
        self.cerrar()
        VentanaUsuario(self.menu)

    def cerrar(self):
        self.grab_release()
        self.destroy() 
