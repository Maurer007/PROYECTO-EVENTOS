import random, threading
from PIL import Image
import customtkinter as ctk
from database import DatabaseManager
from carrusel_deslizante import CarruselDeslizante
from invitaciones import Ventana
from MisEventos import MisEventos

class SplashScreen(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        ancho_ventana = 300
        alto_ventana = 200
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

        self.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
        self.overrideredirect(True)  # Oculta barra de título

        label = ctk.CTkLabel(self, text="Cargando...", font=("Arial", 18))
        label.pack(expand=True)

    def close_splash(self):
        self.destroy()

class Main(ctk.CTk):
    def __init__(self, color_fondo="#2b2b2b", color_texto="black", color_placeholder="gray", color_texto_botones="white", carga_event=None):
        super().__init__()
        self.title("JoinUp")
        self.minsize(900, 750)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.configure(fg_color=color_fondo)

        # Inicializar la base de datos
        self.db_manager = DatabaseManager()
        self.db_manager.insertar_eventos_ejemplo()  # Insertar datos de ejemplo si la tabla está vacía

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        self.text_color = color_texto
        self.placeholder_color = color_placeholder
        self.color_texto_botones = color_texto_botones
        self.carga_event=carga_event
        self.filas_eventos = []

        self.cargar_iconos()
        self.cargar_imagenes_eventos()
        self.create_widgets()
        #self.desordenar_filas() # Descomentar para desordenar filas
        #self.cargar_eventos()

    def create_widgets(self):
        self.create_barra_superior()
        self.create_menu_lateral()
        self.create_principal()
        self.create_user()
        self.create_frame_superpuesto()

    def cargar_iconos(self):
        iconos_info = {
            "user": "user.png",
            "lupa": "lupa.png",
            "home": "home.png",
            "calendario": "calendario.png",
            "mis_eventos": "mis_eventos.png",
            "notificaciones": "notificaciones.png",
            "ajustes": "ajustes.png",
            "logout": "logout.png"
        }

        self.iconos = {}  # Diccionario donde se almacenarán los CTkImage
        for nombre, archivo in iconos_info.items():
            ruta = f"assets/iconos/{archivo}"
            self.iconos[nombre] = ctk.CTkImage(Image.open(ruta), size=(40, 40))

    def create_barra_superior(self):
        frame_superior = ctk.CTkFrame(self)
        frame_superior.columnconfigure(0, weight=1)
        frame_superior.columnconfigure(1, weight=0)
        frame_superior.grid(row=0, column=1, sticky="nsew", padx=(5, 10), pady=(10, 5))
        lupa = ctk.CTkButton(frame_superior, text="", image=self.iconos["lupa"], fg_color="purple", corner_radius=8, width=60, height=60)
        barra = ctk.CTkLabel(frame_superior, text="Barra de búsqueda", fg_color="lightgreen", corner_radius=8, text_color=self.text_color, height=60)
        barra.grid(row=0, column=0, sticky="nsew", padx=(0,5))
        lupa.grid(row=0, column=1, sticky="nsew", padx=(5,0))

    def create_menu_lateral(self):
        frame_barra = ctk.CTkFrame(self)
        frame_barra.rowconfigure(0, weight=1)
        frame_barra.rowconfigure(1, weight=4)
        frame_barra.rowconfigure(2, weight=0)
        frame_barra.grid(row=1, column=0, sticky="nsew", padx=(10, 5), pady=(5, 10))

        subframe_barra_1 = ctk.CTkFrame(frame_barra, fg_color="transparent", width=0, height=0)
        subframe_barra_2 = ctk.CTkFrame(frame_barra, fg_color="transparent", width=0, height=0)
        subframe_barra_3 = ctk.CTkFrame(frame_barra, fg_color="transparent", width=0, height=0)

        subframe_barra_1.grid()
        subframe_barra_2.grid(sticky="nsew")
        subframe_barra_3.grid()

        for i in range(4):
            subframe_barra_1.rowconfigure(i, weight=0)

        # Lista para agregar botones dinámicamente
        botones_config = [
            {"icon": self.iconos["home"],   "color": "lightcoral", "command": self.abrir_main},
            {"icon": self.iconos["calendario"],   "color": "red", "command": self.abrir_mis_eventos},
            {"icon": self.iconos["mis_eventos"],   "color": "cyan", "command": self.abrir_invitacion},
            {"icon": self.iconos["notificaciones"],   "color": "green", "command": None},
            {"icon": self.iconos["ajustes"],   "color": "yellow", "command": None},
        ]

        # Crear y colocar los botones
        for index, config in enumerate(botones_config):
            boton = ctk.CTkButton(
                subframe_barra_2,
                text="",
                image=config["icon"],
                fg_color=config["color"],
                corner_radius=8,
                width=60,
                height=60, 
                command=config["command"]
            )
            pady_top = 0 if index == 0 else 3
            pady_bottom = 0 if index == len(botones_config) - 1 else 3
            boton.grid(row=index, column=0, pady=(pady_top, pady_bottom))

    def crear_fila_eventos(self, contenedor, fila, titulo):
        frame_fila = ctk.CTkFrame(contenedor)
        frame_fila.grid(row=fila, column=0, columnspan=6, sticky="nsew")
        frame_fila.columnconfigure(0, weight=1)
        frame_fila.rowconfigure(0, weight=1)
        frame_fila.rowconfigure(1, weight=4)

        frame_titulo = ctk.CTkFrame(frame_fila, fg_color="transparent")
        frame_titulo.grid(row=0, column=0, sticky="nsew")

        # Crear el título de la fila
        label_titulo = ctk.CTkLabel(frame_titulo, text=titulo, font=("Arial", 25, "bold"), fg_color="transparent", text_color="white")
        label_titulo.pack(anchor="w", padx=10)

        frame_contenido = ctk.CTkScrollableFrame(frame_fila, fg_color="transparent", orientation="horizontal", height=300)
        frame_contenido.grid(row=1, column=0, sticky="nsew", padx=0)
        frame_contenido._scrollbar.grid_forget()  # Oculta scroll por estética

        self.filas_eventos.append(frame_fila)

        return frame_contenido

    def create_principal(self):
        evento_height = 300

        self.frame_principal = ctk.CTkScrollableFrame(self)
        self.frame_principal.grid(row=1, column=1, sticky="nsew", padx=(0, 10), pady=(0, 4))
        self.frame_principal._scrollbar.grid_forget()
        for i in range(6):
            self.frame_principal.rowconfigure(i, weight=1)
        for i in range(3):
            self.frame_principal.columnconfigure(i, weight=1)

        #Evento grande en la parte superior
        principal_main = ctk.CTkFrame(self.frame_principal)
        principal_main.grid(row=0, column=0, sticky="nsew", columnspan=6)
        principal_main.columnconfigure(0, weight=1)
        principal_main.rowconfigure(0, weight=1)

        #contenido = self.obtener_imagenes_eventos()
        contenido = [
            {"type": "text", "text": "¡Bienvenido a JoinUp!"},
            {"type": "image", "path": "assets/grandes/grande1.png"},
            {"type": "text", "text": "¡Organiza tus eventos con nosotros!"},
            {"type": "image", "path": "assets/grandes/grande2.png"},
            {"type": "text", "text": "¡Haz tu evento inolvidable!"},
            {"type": "image", "path": "assets/grandes/grande3.png"},
            {"type": "text", "text": "¡Celebra con nosotros!"},
            {"type": "image", "path": "assets/grandes/grande4.png"},
        ]
        evento_grande = CarruselDeslizante(principal_main, contenido, duracion=3000, velocidad=8, height=evento_height)
        evento_grande.grid(sticky="nsew", pady=(0,3))

        # Filas de eventos (copia una fila para poner una nueva categoría de eventos)
        self.fila_cumple = self.crear_fila_eventos(self.frame_principal, fila=1, titulo="Cumpleaños")
        self.fila_fiestas = self.crear_fila_eventos(self.frame_principal, fila=2, titulo="Fiestas")
        self.fila_bodas = self.crear_fila_eventos(self.frame_principal, fila=3, titulo="Bodas")
        self.fila_xvs = self.crear_fila_eventos(self.frame_principal, fila=4, titulo="XV años")
        self.fila_graduaciones = self.crear_fila_eventos(self.frame_principal, fila=5, titulo="Graduaciones")
        self.fila_eventos = self.crear_fila_eventos(self.frame_principal, fila=6, titulo="Eventos")

    def create_user(self):
        frame_user = ctk.CTkFrame(self)
        frame_user.grid(row=0, column=0, sticky="nsew", padx=(10, 5), pady=(10, 5))
        user = ctk.CTkButton(frame_user, text="", image=self.iconos["user"], fg_color="lightblue", corner_radius=8, width=60, height=60, command=self.abrir_login)
        user.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

    def cargar_imagenes_eventos(self):
        self.imagenes_eventos = {}

        def cargar():
            imagenes_info = {
            "cumple":{
                "cumple1": "assets/cumples/cumple1.png",
                "cumple2": "assets/cumples/cumple2.png",
                "cumple3": "assets/cumples/cumple3.png",
                "cumple4": "assets/cumples/cumple4.png",
                "cumple5": "assets/cumples/cumple5.png",
                "cumple6": "assets/cumples/cumple6.png",
                "cumple7": "assets/cumples/cumple7.png",
                "cumple8": "assets/cumples/cumple8.png",
                "cumple9": "assets/cumples/cumple9.png",
                "cumple10": "assets/cumples/cumple10.png",
            },            
            "boda": {
                "boda1": "assets/bodas/boda1.png",
                "boda2": "assets/bodas/boda2.png",
                "boda3": "assets/bodas/boda3.png",
                "boda4": "assets/bodas/boda4.png",
                "boda5": "assets/bodas/boda5.png",
                "boda6": "assets/bodas/boda6.png",
                "boda7": "assets/bodas/boda7.png",
                "boda8": "assets/bodas/boda8.png",
                "boda9": "assets/bodas/boda9.png",
                "boda10": "assets/bodas/boda10.png",        
            },
            "fiesta": {
                "fiesta1": "assets/fiestas/fiesta1.png",
                "fiesta2": "assets/fiestas/fiesta2.png",
                "fiesta3": "assets/fiestas/fiesta3.png",
                "fiesta4": "assets/fiestas/fiesta4.png",
                "fiesta5": "assets/fiestas/fiesta5.png",
                "fiesta6": "assets/fiestas/fiesta6.png",
                "fiesta7": "assets/fiestas/fiesta7.png",
                "fiesta8": "assets/fiestas/fiesta8.png",
                "fiesta9": "assets/fiestas/fiesta9.png",
                "fiesta10": "assets/fiestas/fiesta10.png",        
            },
            "xv" : {
                "xv1": "assets/xvs/xv1.png",
                "xv2": "assets/xvs/xv2.png",
                "xv3": "assets/xvs/xv3.png",
                "xv4": "assets/xvs/xv4.png",
                "xv5": "assets/xvs/xv5.png",
                "xv6": "assets/xvs/xv6.png",
                "xv7": "assets/xvs/xv7.png",
                "xv8": "assets/xvs/xv8.png",
                "xv9": "assets/xvs/xv9.png",
                "xv10": "assets/xvs/xv10.png",        
            },
            "graduacion" : {
                "grad1": "assets/graduaciones/grad1.png",
                "grad2": "assets/graduaciones/grad2.png",
                "grad3": "assets/graduaciones/grad3.png",
                "grad4": "assets/graduaciones/grad4.png",
                "grad5": "assets/graduaciones/grad5.png",
                "grad6": "assets/graduaciones/grad6.png",
                "grad7": "assets/graduaciones/grad7.png",
                "grad8": "assets/graduaciones/grad8.png",
                "grad9": "assets/graduaciones/grad9.png",
                "grad10": "assets/graduaciones/grad10.png",        
            },
            "eventos" : {
                "evento1": "assets/eventos/evento1.png",
                "evento2": "assets/eventos/evento2.png",
                "evento3": "assets/eventos/evento3.png",
                "evento4": "assets/eventos/evento4.png",
                "evento5": "assets/eventos/evento5.png",
                "evento6": "assets/eventos/evento6.png",
                "evento7": "assets/eventos/evento7.png",
                "evento8": "assets/eventos/evento8.png",
                "evento9": "assets/eventos/evento9.png",
                "evento10": "assets/eventos/evento10.png",        
            },
        }
            for categoria, imagenes in imagenes_info.items():
                for clave, ruta in imagenes.items():
                    try:
                        imagen = ctk.CTkImage(Image.open(ruta), size=(400, 300))
                        self.imagenes_eventos[clave] = imagen
                    except Exception as e:
                        print(f"Error al cargar {ruta}: {e}")
            # Cuando termina, llama a la función para poblar las filas (en el hilo principal)
            self.after(0, self.cargar_imagenes_en_filas)
            if self.carga_event:
                self.carga_event.set()

        threading.Thread(target=cargar, daemon=True).start()

    def cargar_imagenes_en_filas(self):
        evento_height = 300
        evento_width = 400

        # Diccionario que mapea categorías a sus atributos de fila y prefijos de clave
        categorias = {
            "cumple":   (self.fila_cumple, "cumple"),
            "fiesta":   (self.fila_fiestas, "fiesta"),
            "boda":     (self.fila_bodas, "boda"),
            "xv":       (self.fila_xvs, "xv"),
            "graduacion": (self.fila_graduaciones, "grad"),
            "eventos":  (self.fila_eventos, "evento"),
        }

        # Diccionario para definir cuántas imágenes mostrar por categoría
        """k_por_categoria = {
            "cumple": 7,
            "fiesta": 5,
            "boda": 10,
            "xv": 3,
            "graduacion": 8,
            "eventos": 6,
        }"""

        for categoria, (fila_widget, clave_prefijo) in categorias.items():
            #k = k_por_categoria.get(categoria, 10)  # Valor por defecto 10 si no está definido
            claves = [f"{clave_prefijo}{i}" for i in range(1, 11)]
            claves_random = random.sample(claves, k=10)
            for clave in claves_random:
                imagen = self.imagenes_eventos.get(clave)
                if imagen:
                    label = ctk.CTkLabel(fila_widget, image=imagen, text="", width=evento_width, height=evento_height)
                    label.pack(side="left", padx=5, pady=5)

    def ajustar_frame_superpuesto(self, event=None):
        # Obtén el tamaño actual de la ventana principal
        ancho = self.winfo_width()
        alto = self.winfo_height()
        # Define el tamaño mínimo y máximo del frame superpuesto
        relwidth = min(0.4, max(0.25, 350 / max(ancho, 1)))
        # Ajusta relheight según el estado minimizado
        if getattr(self, "frame_superpuesto_minimizado", False):
            relheight = 0.028  # Altura minimizada
        else:
            relheight = min(0.35, max(0.15, 250 / max(alto, 1)))
        # Reposiciona el frame superpuesto
        self.frame_superpuesto.place_configure(
            relwidth=relwidth,
            relheight=relheight,
            relx=1.0,
            rely=1.0,
            anchor="se",
            x=-10,
            y=-10
        )

    def create_frame_superpuesto(self):
        self.frame_superpuesto = ctk.CTkFrame(self, fg_color="white", bg_color="white")
        self.frame_superpuesto.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10, relwidth=0.4, relheight=0.35)

        
        self.frame_superpuesto.columnconfigure(0, weight=1)
        self.frame_superpuesto.rowconfigure(0, weight=0, minsize=28)
        self.frame_superpuesto.rowconfigure(1, weight=1)

        self.horarios_titulo = ctk.CTkButton(self.frame_superpuesto, text="HORARIOS", text_color="black", fg_color="yellow", border_width=3, border_color="black", corner_radius=0, command=self.minimizar, height=28)
        self.horarios_titulo.grid(row=0, column=0, sticky="nsew")
        self.horarios = ctk.CTkScrollableFrame(self.frame_superpuesto, fg_color="yellow", corner_radius=0)
        self.horarios.grid(row=1, column=0, sticky="nsew")
        self.horarios._scrollbar.grid_forget()

        self.frame_superpuesto_minimizado = False
        self.bind("<Configure>", self.ajustar_frame_superpuesto)
        self.minimizar() 

    def abrir_login(self):
        from VentanaLogin import VentanaUsuario
        print("Creando VentanaUsuario...")
        if hasattr(self, "ventana_usuario") and self.ventana_usuario.winfo_exists():
            print("Ya hay una ventana de usuario abierta.")
            return
        try:
            VentanaUsuario(self)
        except Exception as e:
            print("ERROR al crear VentanaUsuario:", e)

    def abrir_main(self):
        # Limpia el frame_principal
        for widget in self.frame_principal.winfo_children():
            widget.destroy()
        # Vuelve a crear el contenido principal
        self.create_principal()
        self.cargar_imagenes_en_filas()

    def abrir_mis_eventos(self):
        # Limpia el frame_principal
        for widget in self.frame_principal.winfo_children():
            widget.destroy()
        # Inserta la Ventana de mis eventos dentro de frame_principal
        try:
            mis_eventos = MisEventos(self.frame_principal)
            mis_eventos.pack(fill="both", expand=True)
        except Exception as e:
            print("ERROR al crear Ventana de Mis Eventos:", e)

    
    def abrir_invitacion(self):
        # Limpia el frame_principal
        for widget in self.frame_principal.winfo_children():
            widget.destroy()
        self.frame_principal.rowconfigure(0, weight=1)
        self.frame_principal.columnconfigure(0, weight=1)
        # Inserta la Ventana de invitaciones dentro de frame_principal
        try:
            invitacion = Ventana(self.frame_principal)
            invitacion.grid(row=0, column=0, sticky="nsew")
        except Exception as e:
            print("ERROR al crear Ventana de Invitación:", e)

    def minimizar(self):
        if not self.frame_superpuesto_minimizado:
            # Minimizar: ocultar horarios y reducir tamaño
            self.horarios.grid_forget()
            self.horarios_titulo.configure(text="MOSTRAR HORARIOS")
            self.frame_superpuesto_minimizado = True
        else:
            # Maximizar: mostrar horarios y restaurar tamaño
            self.horarios.grid(row=1, column=0, sticky="nsew")
            self.horarios_titulo.configure(text="HORARIOS")
            self.frame_superpuesto_minimizado = False

    def desordenar_filas(self):
        random.shuffle(self.filas_eventos)
        for i, fila in enumerate(self.filas_eventos):
            fila.grid_forget()
            fila.grid(row=i+1, column=0, columnspan=6, sticky="nsew")  # i+1 porque la fila 0 es el evento principal

if __name__ == "__main__":
    carga_event = threading.Event()
    app = Main(carga_event=carga_event)
    app.withdraw()
    splash = SplashScreen(app)

    def iniciar_app():
        carga_event.wait()  # Espera a que termine la carga
        splash.close_splash()
        app.deiconify()
        app.wm_state("zoomed")  # Maximiza la ventana principal

    threading.Thread(target=iniciar_app, daemon=True).start()
    app.mainloop()