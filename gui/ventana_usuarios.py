import customtkinter as ctk
from sqlalchemy.exc import SQLAlchemyError
from utils.orm_utils import Session
from models.usuario import Usuario 

def registrar_usuario(nombre, apellido_paterno, apellido_materno, genero, ciudad, estado, fecha_nacimiento, nom_usuario, contrasena, telefono, correo):
    session = Session()
    try:
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            genero=genero,
            ciudad=ciudad,
            estado=estado,
            fecha_nacimiento=fecha_nacimiento,
            nom_usuario=nom_usuario,
            contraseña=contrasena,
            telefono=telefono,
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

def abrir_ventana_usuarios():
    ventana = ctk.CTkToplevel()
    ventana.title("Registro de Usuario")
    ventana.geometry("400x400")

    ctk.CTkLabel(ventana, text="Nombre").pack()
    entry_nombre = ctk.CTkEntry(ventana)
    entry_nombre.pack()

    ctk.CTkLabel(ventana, text="Apellido Paterno").pack()
    entry_apellido = ctk.CTkEntry(ventana)
    entry_apellido.pack()

    ctk.CTkLabel(ventana, text="Correo").pack()
    entry_correo = ctk.CTkEntry(ventana)
    entry_correo.pack()

    ctk.CTkLabel(ventana, text="Contraseña").pack()
    entry_contrasena = ctk.CTkEntry(ventana, show="*")
    entry_contrasena.pack()
    
    label_estado = ctk.CTkLabel(ventana, text="")
    label_estado.pack(pady=10)

    def on_registrar():
        exito = registrar_usuario(
            entry_nombre.get(),
            entry_apellido.get(),
            entry_correo.get(),
            entry_contrasena.get()
        )
        if exito:
            label_estado.configure(text="¡Usuario registrado con éxito!", text_color="green")
        else:
            label_estado.configure(text="Error al registrar usuario.", text_color="red")

    ctk.CTkButton(ventana, text="Registrar", command=on_registrar).pack(pady=10)
