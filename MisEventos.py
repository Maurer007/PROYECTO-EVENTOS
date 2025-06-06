import customtkinter as ctk
from tkinter import *
from tkinter.ttk import Treeview, Style
import Sesion
from models.evento import Evento 
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
import bcrypt
import json
from pathlib import Path

class MisEventos(ctk.CTkFrame):
    def __init__(self, parent, funcion_invitaciones):
        super().__init__(parent)
        self.parent = parent
        self.funcion_invitaciones = funcion_invitaciones
        self.eventos = {}

        self.configure(fg_color="#C4DF62")
        self.crear_titulo()
        self.crear_boton_evento(self.funcion_invitaciones)
        self.recuperar_eventos()
        self.crear_treeview()

    def crear_titulo(self):
        self.titulo = ctk.CTkLabel(self, text="Mis Eventos", font=("Eras Demi ITC", 75), text_color="#0A1A43")
        self.titulo.pack(pady=10)    

    def crear_boton_evento(self, funcion):
        self.boton = ctk.CTkButton(self, text="Crear Evento", command=funcion)
        self.boton.pack(pady=10)    

    def cargar_id_usuario_json(self, ruta="usuario_sesion.json"):
        if not Path(ruta).exists():
            return None
        with open(ruta, "r") as f:
            data = json.load(f)
            return data.get("id_usuario")
    
    def recuperar_eventos(self):
        engine = create_engine("sqlite:///db/app.db")  # Usa la ruta correcta de tu base
        Session = sessionmaker(bind=engine)
        session = Session()
        anfitrion_id = self.cargar_id_usuario_json()

        for evento in session.query(Evento).filter_by(anfitrion_id=anfitrion_id).all():
            self.eventos[evento.id_evento] = (
                evento.tipo_evento,
                evento.fecha,
                evento.hora,
                evento.num_invitados
                )
            

    def crear_treeview(self):
        style = Style()
        tv = Treeview(self, columns=("Columna1", "Columna2", "Columna3", "Columna4"))
        style.configure("Treeview", rowheight=40)
        tv.heading("#0", text="No.")
        tv.heading("Columna1", text="Tipo de evento")
        tv.heading("Columna2", text="Fecha")
        tv.heading("Columna3", text="Hora")
        tv.heading("Columna4", text="Numero de invitados")
        tv.column("#0", width=50, minwidth=50, stretch=True)
        tv.configure()
        tv.tag_configure('par', background='#274687', font=("Arial", 15))
        tv.tag_configure('impar', background='#6086d6', font=("Arial", 15), foreground='blue')
        tv.pack(side="top", fill="x", padx=5, pady=5)

        resultado = {
            ('Cumpleaños', '28/12/2025', '18:00', 'Invitación'),
            ('Boda', '14/9/2026', '18:00', 'Invitación'),
            ('Cumpleaños', '02/04/2026', '14:00', 'Invitación'),
            ('Graduación', '06/08/2025', '20:00', 'Invitación')
        }

        for item in tv.get_children():
            tv.delete(item)

        contador = 0
        for datos in self.eventos.values():
            contador += 1
            if contador % 2 == 0:
                tv.insert("", "end", text=contador, values=datos, tags=("par",))
            else:
                tv.insert("", "end", text=contador, values=datos, tags=("impar",))
                