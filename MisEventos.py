import customtkinter as ctk
from tkinter import *
from tkinter.ttk import Treeview, Style

class MisEventos(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        self.configure(fg_color="#C4DF62")
        self.crear_titulo()
        self.crear_boton_evento()
        #self.crear_treeview()
        
    def crear_titulo(self):
        self.titulo = ctk.CTkLabel(self, text="Mis Eventos", font=("Eras Demi ITC", 75), text_color="#0A1A43")
        self.titulo.pack(pady=10)    

    def crear_boton_evento(self):
        self.boton = ctk.CTkButton(self, text="Crear Evento")
        self.boton.pack(pady=10)    

    def crear_treeview(self):
        self.treeview = ctk.CTkTreeview(self, columns=("Evento", "Fecha", "Hora"), show="headings")
        self.treeview.heading("Evento", text="Evento")
        self.treeview.heading("Fecha", text="Fecha")
        self.treeview.heading("Hora", text="Hora")
        self.treeview.pack(pady=10, fill="both", expand=True)    