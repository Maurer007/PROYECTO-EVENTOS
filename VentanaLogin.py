import os
os.chdir(os.path.dirname(__file__))
import sqlite3
from tkinter import filedialog
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import bcrypt
import customtkinter as ct
from PIL import Image
import tkinter as tk
from tkcalendar import DateEntry
from datetime import date

engine = create_engine("sqlite:///join_up.db", echo=True)

class VentanaUsuario(ct.CTk):
    def __init__(self, textBImg="Seleccionar Imagen", textE1 = "Username", textE2 = "Password", textB1 = "Login",textCB = "Renember me", textB3 = "Register me", colorFondo="black"):
        super().__init__()
        self.title("Log In")

        ancho_v = 500
        alto_v = 500
        ancho_p = self.winfo_screenwidth()
        alto_p = self.winfo_screenheight()
        x = (ancho_p-ancho_v)//2
        y = (alto_p-alto_v)//2
        self.geometry(f"{ancho_v}x{alto_v}+{x}+{y}")

        self.resizable(False, False)
        self.overrideredirect(True)
        frame_top = ct.CTkFrame(self, height=30, corner_radius=0, fg_color=colorFondo)
        frame_top.pack(fill="x")
        self.close_button = ct.CTkButton(frame_top, text="X", width=30, font=("Arial", 30), command=self.destroy,
                                    fg_color="black", hover_color="black", text_color_disabled="gray")
        self.close_button.pack(side="right", padx=5, pady=2)
        self.close_button.bind("<Enter>", self.on_enter)
        self.close_button.bind("<Leave>", self.on_leave)
        self.attributes("-topmost", True)
        self.after(1000, lambda: self.attributes("-topmost", False))

        self.configure(fg_color=  colorFondo)
        self._set_appearance_mode("dark")
        ct.set_default_color_theme("green")

        self.CREDENTIALS_BD = "credentials.db"
        self.usuario = ""
        self.contrasenia = ""
        self.profile_image_path = ""

        self.container1 = ct.CTkFrame(self, fg_color=colorFondo)
        self.container2 = ct.CTkFrame(self, fg_color=colorFondo)
        self.container3 = ct.CTkFrame(self, fg_color=colorFondo)
        self.container4 = ct.CTkFrame(self, fg_color=colorFondo)
        self.container5 = ct.CTkFrame(self, fg_color=colorFondo)
        self.container6 = ct.CTkFrame(self, fg_color=colorFondo)
        self.container7 = ct.CTkFrame(self, fg_color=colorFondo)

        self.container1.pack(padx=10, pady=10)
        self.container2.pack(padx=90, pady=10, expand=True, fill="both")
        self.container3.pack(padx=90, pady=10, expand=True, fill="both")
        self.container4.pack(padx=10, pady=10)
        self.container5.pack(padx=10, pady=10)
        self.container6.pack(padx=10, pady=10)
        self.container7.pack(padx=10, pady=10)

        self.img = ct.CTkImage(light_image=Image.open('logo.png'),
                               dark_image=Image.open('logo.png'),
                               size=(250, 150))
        self.lbImg = ct.CTkLabel(self.container1, text="", image=self.img)
        self.lbImg.pack(expand=True, anchor="center")

        self.lbUser = ct.CTkLabel(self.container2, text=textE1, text_color="white", font=("Arial", 20))
        self.lbUser.pack(expand=True, side="left")

        self.entrada1 = ct.CTkEntry(self.container2, font=("Arial", 20))
        self.entrada1.pack(expand=True, fill="both", side="right", padx=10)

        #self.entrada1.bind("<FocusIn>", lambda event: self.lbUser.configure(text="Usuario"))
        #self.entrada1.bind("<FocusOut>", lambda event: self.lbUser.configure(text=""))

        self.lbPW = ct.CTkLabel(self.container3, text=textE2, text_color="white", font=("Arial", 20))
        self.lbPW.pack(expand=True, side="left")

        self.entrada2 = ct.CTkEntry(self.container3, font=("Arial", 20), show="*")
        self.entrada2.pack(expand=True, fill="both", side="right", padx=10)

        #self.entrada2.bind("<FocusIn>", lambda event: self.lbPW.configure(text="Contraseña"))
        #self.entrada2.bind("<FocusOut>", lambda event: self.lbPW.configure(text=""))

        self.opcion = ct.BooleanVar()
        self.checkbox = ct.CTkCheckBox(self.container4, text=textCB, text_color="white", variable=self.opcion)
        self.checkbox.pack(padx=5, pady=5, expand=True, side="left", anchor="w")

        self.boton1 = ct.CTkButton(self.container5, font=("Arial", 20), text=textB1, command=self.login)
        self.boton1.pack(padx=5, pady=5, expand=True)

        self.lbRegistro = ct.CTkLabel(self.container6, text=textB3, text_color="white", font=("Arial", 20, "underline"), cursor="hand2")
        self.lbRegistro.pack(padx=5, pady=5, expand=True, side="right", anchor="e")

        self.lbRegistro.bind("<Button-1>", lambda event: self.registro())
        self.lbRegistro.bind("<Enter>", lambda event: self.lbRegistro.configure(text_color="blue"))
        self.lbRegistro.bind("<Leave>", lambda event: self.lbRegistro.configure(text_color="white"))

        self.label = ct.CTkLabel(self.container7, text="", font=("Arial", 15), text_color="red")
        self.label.pack(expand=True, anchor="center")

        self.crearTablaBD()
        self.obtenerCredenciales()

    def on_enter(self, event):
        self.close_button.configure(text_color="red")  # O fg_color si solo cambia el texto

    def on_leave(self, event):
        self.close_button.configure(text_color="SystemButtonFace")  # O el color que usabas antes

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.gif;*.webp;*.jfif")])
        if file_path:
            try:
                new_image = ct.CTkImage(light_image=Image.open(file_path), dark_image=Image.open(file_path), size=(100, 100))
                self.lbImg.configure(image=new_image)
                self.lbImg.image = new_image
                self.profile_image_path = file_path
            except Exception as e:
                print(f"Error al cargar la imagen: {e}")

    def registro(self):
        self.destroy()
        ventana_registro = VentanaRegistro(self)
        ventana_registro.mainloop()

    def login(self):
        username = self.entrada1.get()
        password = self.entrada2.get()

        conexion = sqlite3.connect(self.CREDENTIALS_BD)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM registro WHERE usuario=?", (username,))
        user = cursor.fetchone()

        if not username:
            self.label.configure(text="Ingrese un usuario por favor")
        elif not password:
            self.label.configure(text="Ingrese una contraseña por favor")
        else:
            if user:
                hashed_password = user[5].encode('utf-8')
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    ventana_datos = VentanaDatos(self, username).mainloop()

                    if self.checkbox.get():
                        self.insertarDatos(username, password, self.profile_image_path)
                    else:
                        self.borrarCredenciales()
            else:
                self.label.configure(text="Usuario o contraseña incorrectos")
        conexion.close()

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

    def cancel(self):
        self.destroy()

class VentanaRegistro(ct.CTk):
    def __init__(self, parent, textlb = "Registro de usuarios", textE1 = "Nombre", textE2 = "Apellidos", textE3 = "E-mail", textE4 = "Usuario", textE5 = "Contraseña", textE6 = "Confirmar Contraseña", textB1 = "Registrar", textB2 = "Volver", colorFondo="black"):
        super().__init__()
        self.parent = parent
        self.title("Registro")

        ancho_v = 800
        alto_v = 650
        ancho_p = self.winfo_screenwidth()
        alto_p = self.winfo_screenheight()
        x = (ancho_p - ancho_v) // 2
        y = (alto_p - alto_v) // 2
        self.geometry(f"{ancho_v}x{alto_v}+{x}+{y}")

        self.resizable(False, False)
        self.overrideredirect(True)
        frame_top = ct.CTkFrame(self, height=30, corner_radius=0, fg_color=colorFondo)
        frame_top.pack(fill="x")
        self.close_button = ct.CTkButton(frame_top, text="X", width=30, font=("Arial", 30), command=self.destroy,
                                         fg_color="black", hover_color="black", text_color_disabled="gray")
        self.close_button.pack(side="right", padx=5, pady=2)
        self.close_button.bind("<Enter>", self.on_enter)
        self.close_button.bind("<Leave>", self.on_leave)
        self.attributes("-topmost", True)

        self.configure(fg_color=  colorFondo)
        self._set_appearance_mode("dark")
        self.rowconfigure(1, weight=1)

        self.REGISTRO_BD = "credentials.db"
        self.seleccion = ct.StringVar(value="")

        self.container1 = ct.CTkFrame(self, fg_color="transparent")
        self.container2 = ct.CTkScrollableFrame(self, fg_color="transparent")

        self.container1.pack(padx=10, pady=10, fill="both")
        self.container2.pack(padx=10, pady=10, fill="both", expand=True)
        self.container2.grid_columnconfigure((0,1,2,3,4,5), weight=1)

        self.lbTitulo = ct.CTkLabel(self.container1, text=textlb, text_color="red", font=("Arial", 40))
        self.lbTitulo.pack(expand=True, anchor="center")

        self.lbDatos1 = ct.CTkLabel(self.container2, text="Datos personales", text_color="white", font=("Arial", 30))
        self.lbDatos1.grid(row=0, column=0, pady=10, padx=10)

        self.entrada1 = ct.CTkEntry(self.container2, font=("Arial", 20))
        self.entrada1.grid(row=1,column=0, columnspan=2, pady=10, padx=10)

        self.entrada2 = ct.CTkEntry(self.container2, font=("Arial", 20))
        self.entrada2.grid(row=1,column=2, columnspan=2, pady=10, padx=10)

        self.entrada3 = ct.CTkEntry(self.container2, font=("Arial", 20))
        self.entrada3.grid(row=1,column=4, columnspan=2, pady=10, padx=10)

        self.label1 = ct.CTkLabel(self.container2, text="Nombre(s)", text_color="white", font=("Arial", 20))
        self.label1.grid(row=2,column=0, columnspan=2, pady=10, padx=10)

        self.label2 = ct.CTkLabel(self.container2, text="Apellido Paterno", text_color="white", font=("Arial", 20))
        self.label2.grid(row=2,column=2, columnspan=2, pady=10, padx=10)

        self.label3 = ct.CTkLabel(self.container2, text="Apellido Materno", text_color="white", font=("Arial", 20))
        self.label3.grid(row=2,column=4, columnspan=2, pady=10, padx=10)

        self.label4 = ct.CTkLabel(self.container2, text="Género", text_color="white", font=("Arial", 20))
        self.label4.grid(row=3,column=0, columnspan=3, pady=10, padx=10)

        self.radio_hombre = ct.CTkRadioButton(self.container2, text="Hombre", text_color="white", variable=self.seleccion, value=1)
        self.radio_hombre.grid(row=4,column=0, pady=10, padx=10)

        self.radio_mujer = ct.CTkRadioButton(self.container2, text="Mujer", text_color="white", variable=self.seleccion, value=2)
        self.radio_mujer.grid(row=4,column=1, pady=10, padx=10)

        self.radio_otro = ct.CTkRadioButton(self.container2, text="Otro", text_color="white", variable=self.seleccion, value=3)
        self.radio_otro.grid(row=4,column=2, pady=10, padx=10)

        self.label5 = ct.CTkLabel(self.container2, text="Fecha de nacimiento", text_color="white", font=("Arial", 20))
        self.label5.grid(row=3,column=3, columnspan=3, pady=10, padx=10)

        self.date_entry = DateEntry(self.container2, width=16, background='darkblue',
                       foreground='white', borderwidth=2, date_pattern='y-mm-dd', mindate=date(1900, 1, 1), maxdate=date.today())
        self.date_entry.grid(row=4,column=3, columnspan=3, pady=10, padx=10)

        #self.label6 = ct.CTkLabel(self.container7, text=textE6, font=("Arial", 20))
        #self.label6.pack(expand=True, anchor="w", side="left")

        #self.entrada6 = ct.CTkEntry(self.container7, font=("Arial", 20))
        #self.entrada6.pack(expand=True, anchor="w", side="right", fill="both")

        #self.boton1 = ct.CTkButton(self.container8, font=("Arial", 20), text=textB1, command=lambda:self.registrar())
        #self.boton1.pack(padx=5, pady=5, expand=True, side="left")

        #self.boton2 = ct.CTkButton(self.container8, font=("Arial", 20), text=textB2, command=lambda:self.volver())
        #self.boton2.pack(padx=5, pady=5, expand=True, side="right")

        #self.labelError = ct.CTkLabel(self.container9, text="", font=("Arial", 15), text_color="red")
        #self.labelError.pack(expand=True, anchor="center")

        self.crearTablaBD()

    def on_enter(self, event):
        self.close_button.configure(text_color="red")  # O fg_color si solo cambia el texto

    def on_leave(self, event):
        self.close_button.configure(text_color="SystemButtonFace")  # O el color que usabas antes

    def registrar(self):
        nombre = self.entrada1.get()
        apellido = self.entrada2.get()
        email = self.entrada3.get()
        usuario = self.entrada4.get()
        password = self.entrada5.get()
        confirm_password = self.entrada6.get()

        if not nombre or not apellido or not usuario or not email or not password:
            self.labelError.configure(text="Ingrese todos los datos por favor")
        else:
            if confirm_password == "":
                self.labelError.configure(text="Confirme su contraseña por favor")
            elif password != confirm_password:
                self.labelError.configure(text="Las contraseñas no coinciden")
            else:
                usuarios = self.obtenerUsuario()
                #for item in usuarios:
                 #   if item[5] == usuario:
                  #      self.labelError.configure(text="El usuario ingresado ya existe")
                   # else:
                self.insertarDatos(nombre, apellido, email, usuario, password)
                self.labelError.configure(text="Datos guardados correctamente", text_color="green")

    def crearTablaBD(self):
        sqlinstruction = "CREATE TABLE IF NOT EXISTS " \
                         "registro(id INTEGER PRIMARY KEY AUTOINCREMENT," \
                         "nombre varchar(30)," \
                         "apellidos varchar(45)," \
                         "email varchar(60)," \
                         "usuario varchar(20)," \
                         "contraseña varchar(20))"
        conexion = sqlite3.connect(self.REGISTRO_BD)
        conexion.execute(sqlinstruction)
        conexion.close()

    def insertarDatos(self, nom, aps, email, user, psw):
        hashed_password = bcrypt.hashpw(psw.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        registro = "INSERT INTO registro(nombre, apellidos, email, usuario, contraseña) VALUES(?,?,?,?,?)"
        conexion = sqlite3.connect(self.REGISTRO_BD)
        try:
            conexion.execute(registro, (nom, aps, email, user, hashed_password))
            conexion.commit()
        except Exception as e:
            if type(e).__name__ == "IntegrityError":
                print("Posible llave duplicada")
            else:
                print(type(e).__name__)
        conexion.close()

    def obtenerUsuario(self):
        instruccion = "SELECT * FROM registro"
        conexion = sqlite3.connect(self.REGISTRO_BD)
        cursor = conexion.cursor()
        resultado = cursor.execute(instruccion).fetchall()
        conexion.close()
        return resultado

    def volver(self):
        self.destroy()

class VentanaDatos(ct.CTk):
    def __init__(self, parent, usuario):
        super().__init__()
        self.parent = parent
        self.title("Datos")
        self.geometry("500x500")
        self.rowconfigure(1, weight=1)

        self.REGISTRO_DB = "credentials.db"
        self.usuario = usuario
        self.nombre = ""
        self.apellidos = ""
        self.email = ""
        self.contrasenia = ""

        self.cargar_datos()

        self.container1 = ct.CTkFrame(self)
        self.container2 = ct.CTkFrame(self)
        self.container3 = ct.CTkFrame(self)
        self.container4 = ct.CTkFrame(self)
        self.container5 = ct.CTkFrame(self)
        self.container6 = ct.CTkFrame(self)
        self.container7 = ct.CTkFrame(self)

        self.container1.pack(padx=10, pady=10)
        self.container2.pack(padx=10, pady=10)
        self.container3.pack(padx=10, pady=10)
        self.container4.pack(padx=10, pady=10)
        self.container5.pack(padx=10, pady=10)
        self.container6.pack(padx=10, pady=10)
        self.container7.pack(padx=10, pady=10)

        self.lbTitulo = ct.CTkLabel(self.container1, text="DATOS", font=("Arial", 35))
        self.lbTitulo.pack(expand=True, anchor="center")

        self.label1 = ct.CTkLabel(self.container2, text=f"Usuario: {self.usuario}", font=("Arial", 20))
        self.label1.pack(expand=True, side="left")

        self.label2 = ct.CTkLabel(self.container3, text=f"Nombre: {self.nombre}", font=("Arial", 20))
        self.label2.pack(expand=True, side="left")

        self.label3 = ct.CTkLabel(self.container4, text=f"Apellidos: {self.apellidos}", font=("Arial", 20))
        self.label3.pack(expand=True, side="left")

        self.label4 = ct.CTkLabel(self.container5, text=f"E-mail: {self.email}", font=("Arial", 20))
        self.label4.pack(expand=True, side="left")

        self.label5 = ct.CTkLabel(self.container6, text=f"Contraseña: {self.contrasenia}", font=("Arial", 20))
        self.label5.pack(expand=True, side="left")

        self.boton1 = ct.CTkButton(self.container7, font=("Arial", 20), text="Cerrar Sesión", command=self.cerrar_sesion)
        self.boton1.pack(padx=5, pady=5, expand=True, anchor="center")

    def cargar_datos(self):
        conexion = sqlite3.connect(self.REGISTRO_DB)
        cursor = conexion.cursor()
        resultado = cursor.execute("SELECT * FROM registro WHERE usuario=?", (self.usuario,)).fetchone()
        conexion.close()

        self.nombre = resultado[1]
        self.apellidos = resultado[2]
        self.email = resultado[3]
        self.contrasenia = resultado[5]

    def cerrar_sesion(self):
        self.destroy()
        self.parent.deiconify()


if __name__ == "__main__":
    app = VentanaUsuario()
    app.mainloop()
