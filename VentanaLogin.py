import os
import sqlite3
#from tkinter import filedialog
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import bcrypt
import customtkinter as ct
from PIL import Image
#import tkinter as tk
from datetime import date
from models.usuario import Usuario
import Sesion
import json
from pathlib import Path

engine = create_engine("sqlite:///join_up.db", echo=True)

class VentanaUsuario(ct.CTkToplevel):
    def __init__(self, menu, colorFondo="#1256E8"):
        super().__init__(menu)
        self.title("Iniciar sesión")
        self.menu=menu

        ancho_v = 500
        alto_v = 500
        x = (self.winfo_screenwidth() - ancho_v) // 2
        y = (self.winfo_screenheight() - alto_v) // 2
        self.geometry(f"{ancho_v}x{alto_v}+{x}+{y}")

        self.grab_set()
        
        self.overrideredirect(True)
        frame_top = ct.CTkFrame(self, height=30, corner_radius=0, fg_color=colorFondo)
        frame_top.pack(fill="x")
        self.close_button = ct.CTkButton(frame_top, text="X", width=30, font=("Arial", 30), command=self.cerrar,
                                    fg_color="black", hover_color="black", text_color_disabled="gray")
        self.close_button.pack(side="right", padx=5, pady=2)
        self.close_button.bind("<Enter>", self.on_enter)
        self.close_button.bind("<Leave>", self.on_leave)
        self.attributes("-topmost", True)
        self.after(1000, lambda: self.attributes("-topmost", False))

        self.configure(fg_color=  colorFondo)
        self._set_appearance_mode("dark")
        ct.set_default_color_theme("blue")

        self.json = "credenciales.json"
        self.entrada1 = None
        self.entrada2 = None
        self.label = None
        self.ver_contraseña = None
        self.usuario = ""
        self.contrasenia = ""

        self.opcion = ct.BooleanVar()
        self.vista = ct.BooleanVar()

        self.crear_frame_titulo()
        self.crear_frame_datos()
        self.crear_frame_boton()
        self.crear_frame_registro()
        self.crear_frame_error()

        self.withdraw()
        self.deiconify()

        self.cargar_credenciales_json()


    def crear_frame_titulo(self):
        frame = ct.CTkFrame(self, fg_color="transparent")
        frame.pack(padx=10, pady=10, fill="both")

        lbTitulo = ct.CTkLabel(frame, text="JOIN UP", text_color="#df0f69", font=("Eras Bold ITC", 70))
        lbTitulo.pack(expand=True, anchor="center")

        lbSubtitulo = ct.CTkLabel(frame, text="Iniciar Sesión", text_color="white", font=("Arial", 30))
        lbSubtitulo.pack(expand=True, anchor="center")

        return frame

    def crear_frame_datos(self):
        frame = ct.CTkFrame(self, fg_color="#D9D9D9", corner_radius=10)
        frame.pack(padx=30, pady=10, fill="both")

        self.entrada1 = self.crear_entry_derecha(frame, "Usuario", 0, "")
        self.entrada2 = self.crear_entry_derecha(frame, "Contraseña", 1, "*")

        self.ver_contraseña = ct.CTkCheckBox(frame, text="🔒", text_color="black", font=("Arial",25), variable=self.vista)
        self.ver_contraseña.grid(row=1, column=4, padx=10, pady=10)
        self.ver_contraseña.bind("<Button-1>", lambda event: self.cambiar_show())

        checkbox = ct.CTkCheckBox(frame, text="Recordar usuario", text_color="black", variable=self.opcion)
        checkbox.grid(row=2, column=0, padx=10, pady=10)

        return frame

    def cambiar_show(self):
        if self.vista.get():
            self.entrada2.configure(show="")
            self.ver_contraseña.configure(text="🔓")
        else:
            self.entrada2.configure(show="*")
            self.ver_contraseña.configure(text="🔒")
    def guardar_id_usuario_json(self, id_usuario):
        datos = {
            "id_usuario": id_usuario
        }
        try:
            with open("usuario_sesion.json", "w") as f:
                json.dump(datos, f)
            print("Archivo usuario_sesion.json creado correctamente.")
        except Exception as e:
            print("Error al crear usuario_sesion.json:", e)

    def cargar_id_usuario_json(ruta="usuario_sesion.json"):
        if not Path(ruta).exists():
            return None
        with open(ruta, "r") as f:
            data = json.load(f)
            return data.get("id_usuario")

    
    def guardar_credenciales_json(self):
        datos = {
            "usuario": self.entrada1.get().strip(),
            "contraseña": self.entrada2.get().strip(),
        }
        
        try:
            with open(self.json, "w") as f:
                json.dump(datos, f)
            print("Archivo credenciales.json creado correctamente.")
        except Exception as e:
            print("Error al crear credenciales.json:", e)

    def cargar_credenciales_json(self):
        if os.path.exists(self.json):
            with open(self.json, "r") as f:
                datos = json.load(f)
                self.entrada1.insert(0, datos.get("usuario", ""))
                self.entrada2.insert(0, datos.get("contraseña", ""))
                self.opcion.set(True)

    def borrar_credenciales_json(self):
        if os.path.exists(self.json):
            os.remove(self.json)

            
    def crear_entry_derecha(self, frame, texto, fila, show):
        label = ct.CTkLabel(frame, text=texto, text_color="black", font=("Arial", 20))
        label.grid(row=fila, column=0, padx=10, pady=10)

        entrada = ct.CTkEntry(frame, font=("Arial", 20), text_color="dark grey", fg_color="white", border_color="black", border_width=2, show=show)
        entrada.grid(row=fila, column=1, columnspan=3, padx=10, pady=10, sticky="nsew")

        return entrada

    def crear_frame_boton(self):
        frame = ct.CTkFrame(self, fg_color="transparent")
        frame.pack(padx=10, pady=10, fill="both")

        self.crear_boton(frame, "Iniciar Sesión", self.login)

        return frame

    def crear_boton(self, frame, texto, funcion):
        boton = ct.CTkButton(frame, font=("Arial", 20), text=texto, fg_color="#F27171", hover_color="red", command=funcion)
        boton.pack(padx=5, pady=5)

    def crear_frame_registro(self):
        frame = ct.CTkFrame(self, fg_color="transparent")
        frame.pack(padx=10, pady=10)

        label = ct.CTkLabel(frame, text="Aún no tienes cuenta? Regístrate", text_color="#030D24", font=("Arial", 20, "underline"), cursor="hand2")
        label.pack(padx=5, pady=5, side="right")

        label.bind("<Button-1>", lambda event: self.registro())
        label.bind("<Enter>", lambda event: label.configure(text_color="#B9FFF1"))
        label.bind("<Leave>", lambda event: label.configure(text_color="#030D24"))

        return frame

    def crear_frame_error(self):
        frame = ct.CTkFrame(self, fg_color="transparent")
        frame.pack(padx=10, pady=10)

        self.label = ct.CTkLabel(frame, text="", font=("Arial", 15), text_color="red")
        self.label.pack(padx=5, pady=5, anchor="e")


        return frame


    def on_enter(self, event):
        self.close_button.configure(text_color="red")  # O fg_color si solo cambia el texto

    def on_leave(self, event):
        self.close_button.configure(text_color="SystemButtonFace")  # O el color que usabas antes

    def registro(self):
        from VentanaRegistro import VentanaRegistro
        self.destroy()
        VentanaRegistro(self.menu)
    
    def login(self):        
        username = self.entrada1.get().strip()
        password = self.entrada2.get().strip()

        engine = create_engine("sqlite:///db/app.db")
        Session = sessionmaker(bind=engine)
        session = Session()

        if not username:
            self.label.configure(text="Ingrese un usuario por favor")
            return
        if not password:
            self.label.configure(text="Ingrese una contraseña por favor")
            return

        user = session.query(Usuario).filter_by(nom_usuario=username).first()

        if user:
            if bcrypt.checkpw(password.encode("utf-8"), user.contraseña.encode("utf-8")):
                print("Login correcto con:", username)
                import Sesion
                Sesion.usuario_actual = username

                self.guardar_id_usuario_json(user.id_usuario)

                if self.opcion.get():
                    self.guardar_credenciales_json()
                else:
                    self.borrar_credenciales_json()

                self.cerrar()
                print(f"Usuario: {Sesion.usuario_actual}")


            else:
                self.label.configure(text="Contraseña incorrecta")
        else:
            self.label.configure(text="Usuario no encontrado")
    
    def crearTablaBD(self):
        sqlinstruction = "CREATE TABLE IF NOT EXISTS " \
                         "credenciales(id INTEGER PRIMARY KEY AUTOINCREMENT," \
                         "usuario varchar(20)," \
                         "contraseña varchar(20))"
        conexion = sqlite3.connect(self.CREDENTIALS_BD)
        conexion.execute(sqlinstruction)
        conexion.close()

    def insertarDatos(self, user, psw, img):
        registro = "INSERT INTO credenciales(usuario, contraseña, imagen) VALUES(?,?,?)"
        conexion = sqlite3.connect(self.CREDENTIALS_BD)
        try:
            conexion.execute(registro, (user, psw, img))
            conexion.commit()
        except Exception as e:
            if type(e).__name__ == "IntegrityError":
                print("Posible llave duplicada")
            else:
                print(type(e).__name__)
        conexion.close()

    def obtenerCredenciales(self):
        instruccion = "SELECT * FROM credenciales ORDER BY id DESC LIMIT 1"
        conexion = sqlite3.connect(self.CREDENTIALS_BD)
        cursor = conexion.cursor()
        resultado = cursor.execute(instruccion).fetchone()
        conexion.close()

        if resultado:
            self.entrada1.insert(0, resultado[1])
            self.entrada2.insert(0, resultado[2])
            self.checkbox.select()

    def borrarCredenciales(self):
        conexion = sqlite3.connect(self.CREDENTIALS_BD)
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM credenciales")
        conexion.commit()
        conexion.close()

    def cerrar(self):
        self.grab_release()
        self.destroy()

