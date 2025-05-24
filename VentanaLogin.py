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

class VentanaUsuario(ct.CTkToplevel):
    def __init__(self, menu, colorFondo="#1256E8"):
        super().__init__(menu)
        self.title("Iniciar sesión")
        self.menu=menu

        self.transient(menu)
        self.deiconify()
        self.lift()
        self.focus_force()
        self.update()

        ancho_v = 500
        alto_v = 500
        x = (self.winfo_screenwidth() - ancho_v) // 2
        y = (self.winfo_screenheight() - alto_v) // 2
        self.geometry(f"{ancho_v}x{alto_v}+{x}+{y}")

        self.grab_set()

        print("VentanaUsuario creada Vol.4")
        
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
        ct.set_default_color_theme("green")

        self.CREDENTIALS_BD = "credentials.db"
        self.usuario = ""
        self.contrasenia = ""

        self.container1 = ct.CTkFrame(self, fg_color=colorFondo)
        self.container2 = ct.CTkFrame(self, fg_color="#D9D9D9", corner_radius=10)
        self.container3 = ct.CTkFrame(self, fg_color=colorFondo)
        self.container4 = ct.CTkFrame(self, fg_color=colorFondo)
        self.container5 = ct.CTkFrame(self, fg_color=colorFondo)

        self.container1.pack(padx=10, pady=10)
        self.container2.pack(padx=30, pady=10, expand=True, fill="both")
        self.container3.pack(padx=10, pady=10)
        self.container4.pack(padx=10, pady=10)
        self.container5.pack(padx=10, pady=10)

        self.lbTitulo = ct.CTkLabel(self.container1, text="JOIN UP", text_color="#F27171", font=("Eras Bold ITC", 70))
        self.lbTitulo.pack(expand=True, anchor="center")

        self.lbSI = ct.CTkLabel(self.container1, text="Inicio de sesión", text_color="white", font=("Arial", 30))
        self.lbSI.pack(expand=True, anchor="center")

        self.lbUser = ct.CTkLabel(self.container2, text="Usuario", text_color="black", font=("Arial", 20))
        self.lbUser.grid(row=0, column=0, padx=10, pady=10)

        self.entrada1 = ct.CTkEntry(self.container2, font=("Arial", 20), fg_color="white", border_color="black", border_width=2)
        self.entrada1.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky="nsew")

        #self.entrada1.bind("<FocusIn>", lambda event: self.lbUser.configure(text="Usuario"))
        #self.entrada1.bind("<FocusOut>", lambda event: self.lbUser.configure(text=""))

        self.lbPW = ct.CTkLabel(self.container2, text="Contraseña", text_color="black", font=("Arial", 20))
        self.lbPW.grid(row=1, column=0, padx=10, pady=10)

        self.entrada2 = ct.CTkEntry(self.container2, font=("Arial", 20), show="*", fg_color="white", border_color="black", border_width=2)
        self.entrada2.grid(row=1, column=1, columnspan=3,  padx=10, pady=10, sticky="nsew")
        #self.entrada2.bind("<FocusIn>", lambda event: self.lbPW.configure(text="Contraseña"))
        #self.entrada2.bind("<FocusOut>", lambda event: self.lbPW.configure(text=""))

        self.opcion = ct.BooleanVar()
        self.checkbox = ct.CTkCheckBox(self.container2, text="Recordar usuario", text_color="black", variable=self.opcion)
        self.checkbox.grid(row=2, column=0, padx=10, pady=10)

        self.boton1 = ct.CTkButton(self.container3, font=("Arial", 20), text="Iniciar sesión", fg_color="#F27171", hover_color="red", command=self.login)
        self.boton1.pack(padx=5, pady=5, expand=True)

        self.lbRegistro = ct.CTkLabel(self.container4, text="Registro", text_color="white", font=("Arial", 20, "underline"), cursor="hand2")
        self.lbRegistro.pack(padx=5, pady=5, expand=True, side="right", anchor="e")

        self.lbRegistro.bind("<Button-1>", lambda event: self.registro())
        self.lbRegistro.bind("<Enter>", lambda event: self.lbRegistro.configure(text_color="blue"))
        self.lbRegistro.bind("<Leave>", lambda event: self.lbRegistro.configure(text_color="white"))

        self.label = ct.CTkLabel(self.container5, text="", font=("Arial", 15), text_color="red")
        self.label.pack(expand=True, anchor="center")

        self.crearTablaBD()
        self.obtenerCredenciales()

    def on_enter(self, event):
        self.close_button.configure(text_color="red")  # O fg_color si solo cambia el texto

    def on_leave(self, event):
        self.close_button.configure(text_color="SystemButtonFace")  # O el color que usabas antes

    """
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
        """
    def registro(self):
        self.destroy()
        VentanaRegistro(self.menu)

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

    def cerrar(self):
        self.grab_release()
        self.destroy()
class VentanaRegistro(ct.CTkToplevel):
    def __init__(self, menu, textlb = "Registro de usuarios", textE1 = "Nombre", textE2 = "Apellidos", textE3 = "E-mail", textE4 = "Usuario", textE5 = "Contraseña", textE6 = "Confirmar Contraseña", textB1 = "Registrar", textB2 = "Volver", colorFondo="black"):
        super().__init__(menu)
        self.title("Registro")
        self.menu=menu

        self.transient(menu)
        self.deiconify()
        self.lift()
        self.focus_force()
        self.update()

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

        self.REGISTRO_BD = "credentials.db"
        self.seleccion = ct.StringVar(value="")

        self.frame_principal = self.crear_scrollable_frame()

        self.frame_titulo = self.crear_frame_titulo(self.frame_principal)

        self.datos_personales = self.crear_frame_datos(self.frame_principal, "Datos personales")
        self.crear_datos_personales(self.datos_personales)

        self.datos_usuario = self.crear_frame_datos(self.frame_principal, "Datos de usuario")
        self.crear_datos_usuario(self.datos_usuario)

        self.frme_botones = self.crear_frame_botones(self.frame_principal)

        #self.labelError = ct.CTkLabel(self.container9, text="", font=("Arial", 15), text_color="red")
        #self.labelError.pack(expand=True, anchor="center")

        self.crearTablaBD()

    def crear_scrollable_frame(self):
        container1 = ct.CTkScrollableFrame(self, fg_color="transparent")
        container1.pack(padx=10, pady=10, fill="both", expand=True)

        return container1

    def crear_frame_titulo(self, scrollable_frame):
        frame = ct.CTkFrame(scrollable_frame, fg_color="transparent")
        frame.pack(padx=10, pady=10, fill="both")

        lbTitulo = ct.CTkLabel(frame, text="JOIN UP", text_color="#F27171", font=("Eras Bold ITC", 70))
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
        self.crear_entry_arriba(frame_datos, 0, "Nombre")
        self.crear_entry_arriba(frame_datos, 2, "Apellido Paterno")
        self.crear_entry_arriba(frame_datos, 4, "Apellido Materno")
        self.crear_frame_radios(frame_datos)
        self.crear_frame_fecha(frame_datos)
        self.crear_frame_municipio(frame_datos)

    def crear_entry_arriba(self, frame_datos, columna, texto):
        entrada = ct.CTkEntry(frame_datos, text_color="black", font=("Arial", 20), fg_color="white")
        entrada.grid(row=0, column=columna, columnspan=2, pady=10, padx=10)

        label = ct.CTkLabel(frame_datos, text=texto, text_color="black", font=("Arial", 20))
        label.grid(row=1, column=columna, columnspan=4, pady=10, padx=10, sticky="w")

    def crear_frame_radios(self, frame_datos):
        frameRadios = ct.CTkFrame(frame_datos, fg_color="white")
        frameRadios.grid(row=2, column=0, columnspan=4, pady=10, padx=10)

        label = ct.CTkLabel(frameRadios, text="Género", text_color="black", font=("Arial", 20))
        label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        radio_hombre = self.crear_radios(frameRadios, 0, "Hombre")
        radio_mujer = self.crear_radios(frameRadios, 1, "Mujer")
        radio_otro = self.crear_radios(frameRadios, 2, "Otro")
        
    def crear_radios(self, frame_radios, columna, texto):
        radio = ct.CTkRadioButton(frame_radios, text=texto, text_color="black", variable=self.seleccion, value=1)
        radio.grid(row=1, column=columna, pady=10, padx=10)

    def crear_frame_fecha(self, frame_datos):
        frameFecha = ct.CTkFrame(frame_datos, fg_color="white")
        frameFecha.grid(row=2,column=4, columnspan=4, pady=10, padx=10, sticky="nsew")

        label = ct.CTkLabel(frameFecha, text="Fecha de nacimiento", text_color="black", font=("Arial", 20))
        label.grid(row=0, column=0, pady=10, padx=10)

        date_entry = DateEntry(frameFecha, width=16, background='#D9D9D9',
                       date_pattern='y-mm-dd', mindate=date(1900, 1, 1), maxdate=date.today())
        date_entry.grid(row=1, column=0, pady=10, padx=10)

    def crear_frame_municipio(self, frame_datos):
        frame = ct.CTkFrame(frame_datos, fg_color="transparent")
        frame.grid(row=3, column=0, columnspan=8, pady=10, padx=10)

        self.crear_entry(frame, 0, "Estado")
        self.crear_entry(frame, 4, "Municipio")

    def crear_entry(self, frame_municipio, columna, texto):
        label = ct.CTkLabel(frame_municipio, text=texto, text_color="black", font=("Arial", 20))
        label.grid(row=0, column=columna, pady=10, padx=10, sticky="w")

        entrada = ct.CTkEntry(frame_municipio, text_color="black", font=("Arial", 20), fg_color="white")
        entrada.grid(row=0, column=columna+1, columnspan=3, pady=10, padx=10)

    # Todos los campos de datos de usuario
    def crear_datos_usuario(self, frame_datos):
        self.crear_entry_derecha(frame_datos, 0, 1, "Nombre de usuario")
        self.crear_entry_derecha(frame_datos, 1, 1, "Contraseña")
        self.crear_entry_derecha(frame_datos, 2, 1, "Confirmar contraseña")
        self.crear_entry_derecha(frame_datos, 3, 1, "Teléfono")
        self.crear_entry_derecha(frame_datos, 4, 1, "Correo electrónico")

    def crear_entry_derecha(self, frame_datos, fila, columna, texto):
        label = ct.CTkLabel(frame_datos, text=texto, text_color="black", font=("Arial", 20))
        label.grid(row=fila, column=columna, columnspan=2, pady=10, padx=10, sticky="w")

        entrada = ct.CTkEntry(frame_datos, text_color="black", font=("Arial", 20), fg_color="white")
        entrada.grid(row=fila, column=columna+2, columnspan=4, pady=10, padx=10, sticky="nsew")

    # Creación de botones
    def crear_frame_botones(self, scrollable_frame):
        frame = ct.CTkFrame(scrollable_frame, fg_color="transparent")
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.crear_boton(frame, "Volver", "left", self.volver)
        self.crear_boton(frame, "Registrar", "right", self.registrar)

        return frame
        
    def crear_boton(self, frame_botones, texto, lado, comando):
        boton = ct.CTkButton(frame_botones, font=("Arial", 20), text=texto, command=comando)
        boton.pack(pady=10, side=lado, expand=True)


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
        self.cerrar()
        VentanaUsuario(self.menu)

    def cerrar(self):
        self.grab_release()
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


#if __name__ == "__main__":
#    root = ct.CTk()
#    root.withdraw()  # Oculta la ventana principal
#    app = VentanaUsuario(root)
#    app.mainloop()
