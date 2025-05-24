import customtkinter as ctk
from sqlalchemy.exc import SQLAlchemyError
from utils.orm_utils import Session
from models.evento import Evento

def registrar_evento(anfitrion, tipo, fecha, hora):
    session = Session()
    try:
        nuevo_evento = Evento(
            anfitrion=anfitrion,
            tipo_evento=tipo,
            fecha=fecha,
            hora=hora
        )
        session.add(nuevo_evento)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error al registrar evento: {e}")
    finally:
        session.close()

def abrir_ventana_eventos():
    ventana = ctk.CTkToplevel()
    ventana.title("Registro de Evento")
    ventana.geometry("400x400")

    ctk.CTkLabel(ventana, text="Anfitrión").pack()
    entry_anfitrion = ctk.CTkEntry(ventana)
    entry_anfitrion.pack()

    ctk.CTkLabel(ventana, text="Tipo de evento").pack()
    entry_tipo = ctk.CTkEntry(ventana)
    entry_tipo.pack()

    ctk.CTkLabel(ventana, text="Fecha (YYYY-MM-DD)").pack()
    entry_fecha = ctk.CTkEntry(ventana)
    entry_fecha.pack()

    ctk.CTkLabel(ventana, text="Hora (HH:MM)").pack()
    entry_hora = ctk.CTkEntry(ventana)
    entry_hora.pack()

    def on_registrar():
        registrar_evento(
            entry_anfitrion.get(),
            entry_tipo.get(),
            entry_fecha.get(),
            entry_hora.get()
        )

    ctk.CTkButton(ventana, text="Registrar Evento", command=on_registrar).pack(pady=10)
