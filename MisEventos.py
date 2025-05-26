import customtkinter as ctk
from tkinter import *
from tkinter.ttk import Treeview, Style

class MisEventos(ctk.CTkFrame):
    def __init__(self, parent, funcion_invitaciones):
        super().__init__(parent)
        self.parent = parent
        self.funcion_invitaciones = funcion_invitaciones

        self.configure(fg_color="#C4DF62")
        self.crear_titulo()
        self.crear_boton_evento(self.funcion_invitaciones)
        self.crear_treeview()

    def crear_titulo(self):
        self.titulo = ctk.CTkLabel(self, text="Mis Eventos", font=("Eras Demi ITC", 75), text_color="#0A1A43")
        self.titulo.pack(pady=10)    

    def crear_boton_evento(self, funcion):
        self.boton = ctk.CTkButton(self, text="Crear Evento", command=funcion)
        self.boton.pack(pady=10)    

    def crear_treeview(self):
        style = Style()
        tv = Treeview(self, columns=("Columna1", "Columna2", "Columna3", "Columna4"))
        style.configure("Treeview", rowheight=40)
        tv.heading("#0", text="No.")
        tv.heading("Columna1", text="Tipo de evento")
        tv.heading("Columna2", text="Fecha")
        tv.heading("Columna3", text="Hora")
        tv.heading("Columna4", text="Invitación")
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
        for item in resultado:
            contador += 1
            if contador % 2 == 0:
                tv.insert("", "end", text=contador, values=(item[0], item[1], item[2], item[3]), tags=("par",))
            else:
                tv.insert("", "end", text=contador, values=(item[0], item[1], item[2], item[3]), tags=("impar",))
        