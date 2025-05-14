import random
from PIL import Image
import customtkinter as ctk
from database import DatabaseManager

class SplashScreen(ctk.CTkToplevel):  # Ventana emergente temporal
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry("300x200+800+400")
        self.title("Cargando...")
        self.overrideredirect(True)  # Oculta barra de título

        label = ctk.CTkLabel(self, text="Cargando...", font=("Arial", 18))
        label.pack(expand=True)

        self.after(500, self.close_splash)

    def close_splash(self):
        self.destroy()
        self.master.deiconify()

class Main(ctk.CTk):
    def __init__(self, color_fondo="#2b2b2b", color_texto="black", color_placeholder="gray", color_texto_botones="white"):
        super().__init__()
        self.title("JoinUp")
        self.geometry("900x750+250+150")
        self.minsize(900, 750)
        self._set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.configure(fg_color=color_fondo)

        # Inicializar la base de datos dabid hola (prueba para ver si funciona)
        self.db_manager = DatabaseManager()
        self.db_manager.insertar_eventos_ejemplo()  # Insertar datos de ejemplo si la tabla está vacía

        # Crear el frame principal
        self.frame_principal = ctk.CTkScrollableFrame(self)
        self.frame_principal.grid(row=1, column=1, sticky="nsew", padx=(0, 10), pady=(0, 4))
        self.frame_principal.columnconfigure(0, weight=1)

        # Cargar eventos desde la base de datos
        #self.cargar_eventos()

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        self.icon_user = ctk.CTkImage(Image.open("user.png"), size=(40, 40))
        self.icon_lupa = ctk.CTkImage(Image.open("lupa.png"), size=(40, 40))
        self.icon_home = ctk.CTkImage(Image.open("home.png"), size=(40, 40))
        self.icon_calendario = ctk.CTkImage(Image.open("calendario.png"), size=(40, 40))
        self.icon_mis_eventos = ctk.CTkImage(Image.open("mis_eventos.png"), size=(40, 40))
        self.icon_notificaciones = ctk.CTkImage(Image.open("notificaciones.png"), size=(40, 40))
        self.icon_ajustes = ctk.CTkImage(Image.open("ajustes.png"), size=(40, 40))
        self.icon_logout = ctk.CTkImage(Image.open("logout.png"), size=(40, 40))
        self.text_color = color_texto
        self.placeholder_color = color_placeholder
        self.color_texto_botones = color_texto_botones

        self.create_widgets()
        self.desordenar_categorias()
        
    def create_widgets(self):
        evento_height = 300
        evento_width = 400
        frame_superior = ctk.CTkFrame(self)
        frame_lupa = ctk.CTkFrame(self)
        frame_barra = ctk.CTkFrame(self)
        frame_principal = ctk.CTkScrollableFrame(self)
        frame_principal._scrollbar.grid_forget()

        frame_superior.columnconfigure(0,weight=1)
        frame_superior.columnconfigure(1,weight=0)

        frame_barra.rowconfigure(0, weight=1)
        frame_barra.rowconfigure(1, weight=4)
        frame_barra.rowconfigure(2, weight=0)

        frame_principal.columnconfigure(0, weight=1)
        frame_principal.columnconfigure(1, weight=1)
        frame_principal.columnconfigure(2, weight=1)
        frame_principal.columnconfigure(3, weight=1)
        frame_principal.columnconfigure(4, weight=1)
        frame_principal.columnconfigure(5, weight=1)
        frame_principal.rowconfigure(0, weight=1)
        frame_principal.rowconfigure(1, weight=1)
        frame_principal.rowconfigure(2, weight=1)

        subframe_barra_1 =ctk.CTkFrame(frame_barra, fg_color="transparent", width=0, height=0)
        subframe_barra_2 =ctk.CTkFrame(frame_barra, fg_color="transparent", width=0, height=0)
        subframe_barra_3 =ctk.CTkFrame(frame_barra, fg_color="transparent", width=0, height=0)
        subframe_barra_1.grid()
        subframe_barra_2.grid(sticky="nsew")
        subframe_barra_3.grid()

        subframe_barra_2.rowconfigure(0, weight=0)
        subframe_barra_2.rowconfigure(1, weight=0)
        subframe_barra_2.rowconfigure(2, weight=0)
        subframe_barra_2.rowconfigure(3, weight=0)

        principal_main = ctk.CTkFrame(frame_principal)
        principal_fila2 = ctk.CTkFrame(frame_principal)
        principal_fila3 = ctk.CTkFrame(frame_principal)
        principal_fila4 = ctk.CTkFrame(frame_principal)
        principal_fila5 = ctk.CTkFrame(frame_principal)
        principal_fila6 = ctk.CTkFrame(frame_principal)

        principal_main.grid(row=0, column=0, sticky="nsew", columnspan=6)
        principal_fila2.grid(row=1, column=0, sticky="nsew", columnspan=6)
        principal_fila3.grid(row=2, column=0, sticky="nsew", columnspan=6)
        principal_fila4.grid(row=3, column=0, sticky="nsew", columnspan=6)
        principal_fila5.grid(row=4, column=0, sticky="nsew", columnspan=6)
        principal_fila6.grid(row=5, column=0, sticky="nsew", columnspan=6)
        principal_main.columnconfigure(0, weight=1)
        principal_main.rowconfigure(0, weight=1)
        principal_fila2.columnconfigure(0, weight=1)
        principal_fila2.rowconfigure(0, weight=1)
        principal_fila2.rowconfigure(1, weight=4)
        principal_fila3.columnconfigure(0, weight=1)
        principal_fila3.rowconfigure(0, weight=1)
        principal_fila3.rowconfigure(1, weight=4)
        principal_fila4.columnconfigure(0, weight=1)
        principal_fila4.rowconfigure(0, weight=1)
        principal_fila4.rowconfigure(1, weight=4)
        principal_fila5.columnconfigure(0, weight=1)
        principal_fila5.rowconfigure(0, weight=1)
        principal_fila5.rowconfigure(1, weight=4)
        principal_fila6.columnconfigure(0, weight=1)
        principal_fila6.rowconfigure(0, weight=1)
        principal_fila6.rowconfigure(1, weight=4)

        fila2_frame_titulo = ctk.CTkFrame(principal_fila2, fg_color="transparent")
        fila2_frame_titulo.grid(row=0, column=0, sticky="nsew")
        fila2_frame_contenido = ctk.CTkScrollableFrame(principal_fila2, fg_color="transparent", orientation="horizontal", height=evento_height)
        fila2_frame_contenido._scrollbar.grid_forget()
        fila2_frame_contenido.grid(row=1, column=0, sticky="nsew", padx=0)

        fila3_frame_titulo = ctk.CTkFrame(principal_fila3, fg_color="transparent")
        fila3_frame_titulo.grid(row=0, column=0, sticky="nsew")
        fila3_frame_contenido = ctk.CTkScrollableFrame(principal_fila3, fg_color="transparent", orientation="horizontal", height=evento_height)
        fila3_frame_contenido._scrollbar.grid_forget()
        fila3_frame_contenido.grid(row=1, column=0, sticky="nsew")

        fila4_frame_titulo = ctk.CTkFrame(principal_fila4, fg_color="transparent")
        fila4_frame_titulo.grid(row=0, column=0, sticky="nsew")
        fila4_frame_contenido = ctk.CTkScrollableFrame(principal_fila4, fg_color="transparent", orientation="horizontal", height=evento_height)
        fila4_frame_contenido._scrollbar.grid_forget()
        fila4_frame_contenido.grid(row=1, column=0, sticky="nsew")

        fila5_frame_titulo = ctk.CTkFrame(principal_fila5, fg_color="transparent")
        fila5_frame_titulo.grid(row=0, column=0, sticky="nsew")
        fila5_frame_contenido = ctk.CTkScrollableFrame(principal_fila5, fg_color="transparent", orientation="horizontal", height=evento_height)
        fila5_frame_contenido._scrollbar.grid_forget()
        fila5_frame_contenido.grid(row=1, column=0, sticky="nsew")

        fila6_frame_titulo = ctk.CTkFrame(principal_fila6, fg_color="transparent")
        fila6_frame_titulo.grid(row=0, column=0, sticky="nsew")
        fila6_frame_contenido = ctk.CTkScrollableFrame(principal_fila6, fg_color="transparent", orientation="horizontal", height=evento_height)
        fila6_frame_contenido._scrollbar.grid_forget()
        fila6_frame_contenido.grid(row=1, column=0, sticky="nsew")

        frame_lupa.grid(row=0, column=0, sticky="nsew", padx=(10, 5), pady=(10, 5))
        frame_superior.grid(row=0, column=1, sticky="nsew", padx=(5, 10), pady=(10, 5))
        frame_barra.grid(row=1, column=0, sticky="nsew", padx=(10, 5), pady=(5, 10))
        frame_principal.grid(row=1, column=1, sticky="nsew", padx=(0, 10), pady=(0, 4))

        frame_superpuesto = ctk.CTkFrame(self, fg_color="white", bg_color="white")
        frame_superpuesto.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10, relwidth=0.4, relheight=0.35, )
        frame_superpuesto.columnconfigure(0, weight=1)
        frame_superpuesto.rowconfigure(0, weight=1)
        frame_superpuesto.rowconfigure(1, weight=9)

        self.horarios_titulo = ctk.CTkButton(frame_superpuesto, text="HORARIOS", text_color="black", fg_color="yellow", border_width=3, border_color="black", corner_radius=0, command=self.minimizar)
        self.horarios_titulo.grid(row=0, column=0, sticky="nsew")
        self.horarios = ctk.CTkScrollableFrame(frame_superpuesto, fg_color="yellow", corner_radius=0)
        self.horarios.grid(row=1, column=0, sticky="nsew")
        self.horarios._scrollbar.grid_forget()

        lupa = ctk.CTkButton(frame_superior, text="", image=self.icon_lupa, fg_color="purple", corner_radius=8, width=60, height=60)
        barra = ctk.CTkLabel(frame_superior, text="Barra de búsqueda", fg_color="lightgreen", corner_radius=8, text_color=self.text_color, height=60)

        user = ctk.CTkButton(frame_lupa, text="", image=self.icon_user, fg_color="lightblue", corner_radius=8, width=60, height=60)

        home = ctk.CTkButton(subframe_barra_2, text="", image=self.icon_home, fg_color="lightcoral", corner_radius=8, width=60, height=60)
        calendario = ctk.CTkButton(subframe_barra_2, text="", image=self.icon_calendario, fg_color="red", corner_radius=8, width=60, height=60)
        mis_eventos = ctk.CTkButton(subframe_barra_2, text="", image=self.icon_mis_eventos, fg_color="cyan", corner_radius=8, width=60, height=60)
        notificaciones = ctk.CTkButton(subframe_barra_2, text="", image=self.icon_notificaciones, fg_color="green", corner_radius=8, width=60, height=60)
        ajustes = ctk.CTkButton(subframe_barra_2, text="", image=self.icon_ajustes, fg_color="yellow", corner_radius=8, width=60, height=60)
        logout = ctk.CTkButton(subframe_barra_3, text="", fg_color="transparent", image=self.icon_logout, corner_radius=8, width=60, height=60)

        evento_grande = ctk.CTkLabel(principal_main, text="Evento 1", fg_color="royalblue", corner_radius=8, text_color=self.text_color, height=evento_height)
        evento_grande.grid(sticky="nsew", pady=(0,3))
        fila2_titulo = ctk.CTkLabel(fila2_frame_titulo, text="Cumpleaños", font=("Arial", 20, "bold"), fg_color="transparent", text_color="white")
        fila2_titulo.grid(sticky="w", padx=10, pady=(5,0))
        evento_mediano1= ctk.CTkLabel(fila2_frame_contenido, text="Evento 2", fg_color="maroon", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_mediano1.grid(row= 0, column=0,sticky="nsew", padx=(0,3))
        evento_mediano2 = ctk.CTkLabel(fila2_frame_contenido, text="Evento 3", fg_color="pink", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_mediano2.grid(row=0, column=1, sticky="nsew", padx=(3,3))
        evento_mediano3 = ctk.CTkLabel(fila2_frame_contenido, text="Evento 4", fg_color="magenta", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_mediano3.grid(row=0, column=2, sticky="nsew", padx=(3,3))
        evento_mediano4 = ctk.CTkLabel(fila2_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_mediano4.grid(row=0, column=3, sticky="nsew", padx=(3,3))
        evento_mediano5 = ctk.CTkLabel(fila2_frame_contenido, text="Evento 6", fg_color="brown", corner_radius=8,text_color=self.text_color, height=evento_height, width=evento_width)
        evento_mediano5.grid(row=0, column=4, sticky="nsew", padx=(3,3))
        evento_mediano6 = ctk.CTkLabel(fila2_frame_contenido, text="Evento 7", fg_color="pink", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_mediano6.grid(row=0, column=5, sticky="nsew", padx=(3,3))

        fila3_titulo = ctk.CTkLabel(fila3_frame_titulo, text="XV años", font=("Arial", 20, "bold"), fg_color="transparent", text_color="white")
        fila3_titulo.grid(sticky="w", padx=10, pady=(5,0))
        evento_chico1 = ctk.CTkLabel(fila3_frame_contenido, text="Evento 4", fg_color="magenta", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico1.grid(row= 0, column=1, sticky="nsew", pady=(3, 0), padx=(0,3))
        evento_chico2 = ctk.CTkLabel(fila3_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico2.grid(row= 0, column=2, sticky="nsew", pady=(3, 0), padx=(3,3))
        evento_chico3 = ctk.CTkLabel(fila3_frame_contenido, text="Evento 6", fg_color="brown", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico3.grid(row= 0, column=3, sticky="nsew", pady=(3, 0), padx=(3,3))
        evento_chico4 = ctk.CTkLabel(fila3_frame_contenido, text="Evento 5", fg_color="green", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico4.grid(row=0, column=4, sticky="nsew", pady=(3, 0), padx=(3,3))
        evento_chico5 = ctk.CTkLabel(fila3_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico5.grid(row=0, column=5, sticky="nsew", pady=(3, 0), padx=(3,3))
        evento_chico6 = ctk.CTkLabel(fila3_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico6.grid(row=0, column=6, sticky="nsew", pady=(3, 0), padx=(3,3))

        fila4_titulo = ctk.CTkLabel(fila4_frame_titulo, text="Graduación", font=("Arial", 20, "bold"), fg_color="transparent", text_color="white")
        fila4_titulo.grid(sticky="w", padx=10, pady=(5, 0))
        evento_chico1 = ctk.CTkLabel(fila4_frame_contenido, text="Evento 4", fg_color="magenta", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico1.grid(row=0, column=1, sticky="nsew", pady=(3, 0), padx=(0, 3))
        evento_chico2 = ctk.CTkLabel(fila4_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8,  text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico2.grid(row=0, column=2, sticky="nsew", pady=(3, 0), padx=(3, 3))
        evento_chico3 = ctk.CTkLabel(fila4_frame_contenido, text="Evento 6", fg_color="brown", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico3.grid(row=0, column=3, sticky="nsew", pady=(3, 0), padx=(3, 3))
        evento_chico4 = ctk.CTkLabel(fila4_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico4.grid(row=0, column=4, sticky="nsew", pady=(3, 0), padx=(3, 3))
        evento_chico5 = ctk.CTkLabel(fila4_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8,  text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico5.grid(row=0, column=5, sticky="nsew", pady=(3, 0), padx=(3, 3))
        evento_chico6 = ctk.CTkLabel(fila4_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico6.grid(row=0, column=6, sticky="nsew", pady=(3, 0), padx=(3, 3))

        fila5_titulo = ctk.CTkLabel(fila5_frame_titulo, text="Boda", font=("Arial", 20, "bold"), fg_color="transparent", text_color="white")
        fila5_titulo.grid(sticky="w", padx=10, pady=(5, 0))
        evento_chico1 = ctk.CTkLabel(fila5_frame_contenido, text="Evento 4", fg_color="magenta", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico1.grid(row=0, column=1, sticky="nsew", pady=(3, 0), padx=(0, 3))
        evento_chico2 = ctk.CTkLabel(fila5_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8,  text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico2.grid(row=0, column=2, sticky="nsew", pady=(3, 0), padx=(3, 3))
        evento_chico3 = ctk.CTkLabel(fila5_frame_contenido, text="Evento 6", fg_color="brown", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico3.grid(row=0, column=3, sticky="nsew", pady=(3, 0), padx=(3, 3))
        evento_chico4 = ctk.CTkLabel(fila5_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico4.grid(row=0, column=4, sticky="nsew", pady=(3, 0), padx=(3, 3))
        evento_chico5 = ctk.CTkLabel(fila5_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8,  text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico5.grid(row=0, column=5, sticky="nsew", pady=(3, 0), padx=(3, 3))
        evento_chico6 = ctk.CTkLabel(fila5_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico6.grid(row=0, column=6, sticky="nsew", pady=(3, 0), padx=(3, 3))

        fila6_titulo = ctk.CTkLabel(fila6_frame_titulo, text="Fiesta", font=("Arial", 20, "bold"), fg_color="transparent", text_color="white")
        fila6_titulo.grid(sticky="w", padx=10, pady=(5, 0))
        evento_chico1 = ctk.CTkLabel(fila6_frame_contenido, text="Evento 4", fg_color="magenta", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico1.grid(row=0, column=1, sticky="nsew", pady=(3, 0), padx=(0, 3))
        evento_chico2 = ctk.CTkLabel(fila6_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8,  text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico2.grid(row=0, column=2, sticky="nsew", pady=(3, 0), padx=(3, 3))
        evento_chico3 = ctk.CTkLabel(fila6_frame_contenido, text="Evento 6", fg_color="brown", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico3.grid(row=0, column=3, sticky="nsew", pady=(3, 0), padx=(3, 3))
        evento_chico4 = ctk.CTkLabel(fila6_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico4.grid(row=0, column=4, sticky="nsew", pady=(3, 0), padx=(3, 3))
        evento_chico5 = ctk.CTkLabel(fila6_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8,  text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico5.grid(row=0, column=5, sticky="nsew", pady=(3, 0), padx=(3, 3))
        evento_chico6 = ctk.CTkLabel(fila6_frame_contenido, text="Evento 5", fg_color="violet", corner_radius=8, text_color=self.text_color, height=evento_height, width=evento_width)
        evento_chico6.grid(row=0, column=6, sticky="nsew", pady=(3, 0), padx=(3, 3))

        barra.grid(row=0, column=0, sticky="nsew", padx=(0,5))
        lupa.grid(row=0, column=1, sticky="nsew", padx=(5,0))
        user.grid()
        home.grid(row=0, column=0, pady=(0,3))
        calendario.grid(row=1, column=0, pady=(3,3))
        mis_eventos.grid(row=2, column=0, pady=(3,3))
        notificaciones.grid(row=3, column=0, pady=(3,3))
        ajustes.grid(row=4, column=0, pady=(3,0))
        logout.grid()

        self.categoria_frames = [
            principal_fila2,
            principal_fila3,
            principal_fila4,
            principal_fila5,
            principal_fila6,
        ]

    def minimizar(self):
        if self.horarios.winfo_ismapped():
            # Hide the horarios widget
            self.horarios.grid_forget()
            self.horarios_titulo.configure(text="MOSTRAR HORARIOS")
            # Resize the parent frame to be smaller
            frame_superpuesto = self.horarios_titulo.master
            frame_superpuesto.place_configure(relheight=0.028)  # Only show title bar height
        else:
            # Show the horarios widget
            self.horarios.grid(row=1, column=0, sticky="nsew")
            self.horarios_titulo.configure(text="HORARIOS")
            # Restore the parent frame's original size
            frame_superpuesto = self.horarios_titulo.master
            frame_superpuesto.place_configure(relheight=0.35)  # Restore original height

    def desordenar_categorias(self):
        random.shuffle(self.categoria_frames)
        for i, frame in enumerate(self.categoria_frames):
            frame.grid(row=i+1, column=0, sticky="nsew", columnspan=6)

    def reorganizar_categorias(self):
        random.shuffle(self.categoria_frames_dinamicos)
        for i, frame in enumerate(self.categoria_frames_dinamicos):
            frame.grid_forget()
            frame.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)

if __name__ == "__main__":
    app = Main()
    app.withdraw()
    splash = SplashScreen(app)
    app.mainloop() 