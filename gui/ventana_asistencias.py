import customtkinter as ctk
from sqlalchemy.exc import SQLAlchemyError
from utils.orm_utils import Session
from models.asistencia import Asiste

def registrar_asistencia(id_usuario, id_evento):
    session = Session()
    try:
        nueva_asistencia = Asiste(
            id_usuario=id_usuario,
            id_evento=id_evento
        )
        session.add(nueva_asistencia)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error al registrar asistencia: {e}")
    finally:
        session.close()

def abrir_ventana_asistencias():
    ventana = ctk.CTkToplevel()
    ventana.title("Registrar Asistencia")
    ventana.geometry("400x300")

    ctk.CTkLabel(ventana, text="ID Usuario").pack()
    entry_usuario = ctk.CTkEntry(ventana)
    entry_usuario.pack()

    ctk.CTkLabel(ventana, text="ID Evento").pack()
    entry_evento = ctk.CTkEntry(ventana)
    entry_evento.pack()

    def on_registrar():
        registrar_asistencia(entry_usuario.get(), entry_evento.get())

    ctk.CTkButton(ventana, text="Registrar Asistencia", command=on_registrar).pack(pady=10)
