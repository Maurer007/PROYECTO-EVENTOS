import random, threading, concurrent.futures, sys, io
sys.dont_write_bytecode = True
from PIL import Image
import customtkinter as ctk
from carrusel_deslizante import CarruselDeslizante
from invitaciones import Ventana
from MisEventos import MisEventos
from Alerta_login import AlertaLogin
from VentanaLogin import VentanaUsuario
from FrameSinSesión import SinSesión
from Calendario import Calendario
from InfoEventos import DatosEventos
from VentanaInicioSesion import InicioSesion
from utils.orm_utils import crear_base_de_datos
from utils.carga_imagenes import cargar_imagenes_desde_carpeta
from config import ASSETS, ICONOS, THEME, CATEGORIAS_EVENTOS, TEXTOS, ANIMACION
import Sesion
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.evento import Evento, Fiesta, Cumpleaños, Graduacion, XVAnos, Boda
from models.usuario import Usuario
from utils.orm_utils import engine

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
        from config import cargar_config
        cargar_config()
        self.title("JoinUp")
        self.minsize(900, 750)
        ctk.set_appearance_mode("dark")
        self.configure(fg_color=color_fondo)
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=30)
        self.eventos = {}


        crear_base_de_datos()

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        self.text_color = color_texto
        self.placeholder_color = color_placeholder
        self.color_texto_botones = color_texto_botones
        self.carga_event=carga_event
        self.filas_eventos = []

        self.vista_anterior = None
        self.estado_anterior = None

        self.calendario = Calendario(self)
        self.cargar_iconos()
        self.cargar_imagenes_eventos()
        self.create_widgets()
        #self.desordenar_filas() #Descomentar para desordenar filas
        #self.cargar_eventos()}
        if self.calendario is not None:
            self.calendario.actualizar_contenido()

    def create_widgets(self):
        self.create_barra_superior()
        self.create_menu_lateral()
        self.create_principal()
        self.create_user()

    def cargar_iconos(self):
        self.iconos = {}  
        for nombre, archivo in ICONOS.items():
            ruta = ASSETS["iconos"] + archivo
            self.iconos[nombre] = ctk.CTkImage(Image.open(ruta), size=(40, 40))

    def create_barra_superior(self):
        self.frame_superior = ctk.CTkFrame(self)
        self.frame_superior.columnconfigure(0, weight=1)
        self.frame_superior.columnconfigure(1, weight=0)
        self.frame_superior.grid(row=0, column=1, sticky="nsew", padx=(0, 5), pady=(10, 5))
        self.lupa = ctk.CTkButton(self.frame_superior, text="", image=self.iconos["lupa"], fg_color=THEME["button_fg"], corner_radius=8, width=60, height=60)
        self.barra = ctk.CTkEntry(self.frame_superior, placeholder_text="Barra de búsqueda", fg_color=THEME["background"], font=THEME["font_title"], corner_radius=8, height=60)
        self.barra.grid(row=0, column=0, sticky="nsew", padx=(0,2.5))
        self.lupa.grid(row=0, column=1, sticky="nsew", padx=(2.5,0))

        self.barra.bind("<Return>", lambda event: self.realizar_busqueda())

    def create_menu_lateral(self):
        self.frame_barra = ctk.CTkFrame(self, width=60, fg_color=THEME["background"], corner_radius=6)
        self.frame_barra.grid(row=1, column=0, sticky="nsew", padx=(10, 5), pady=(0, 2.5))
        self.frame_barra.rowconfigure(0, weight=1)
        self.frame_barra.rowconfigure(1, weight=4)
        self.frame_barra.rowconfigure(2, weight=0)
        
        self.subframe_barra_1 = ctk.CTkFrame(self.frame_barra, fg_color=THEME["background"], width=60, height=60, corner_radius=6)
        self.subframe_barra_2 = ctk.CTkFrame(self.frame_barra, fg_color=THEME["background"], corner_radius=0)
        self.subframe_barra_3 = ctk.CTkFrame(self.frame_barra, fg_color=THEME["background"], width=60, corner_radius=6)

        self.subframe_barra_1.grid(row=0, sticky="nsew", pady=(6,0))
        self.subframe_barra_2.grid(row=1, sticky="nsew")
        self.subframe_barra_3.grid(row=2, sticky="nsew", pady=(0,6))

        for i in range(4):
            self.subframe_barra_1.rowconfigure(i, weight=0)

        # Lista para agregar botones dinámicamente
        botones_config = [
            {"icon": self.iconos["home"],   "color": THEME["button_fg"], "command": self.abrir_main},
            {"icon": self.iconos["calendario"],   "color": THEME["button_fg"], "command": self.abrir_calendario},
            {"icon": self.iconos["mis_eventos"],   "color": THEME["button_fg"], "command": self.abrir_mis_eventos},
            #{"icon": self.iconos["notificaciones"],   "color": "green", "command": None},
            {"icon": self.iconos["ajustes"],   "color": THEME["button_fg"], "command": self.abrir_ajustes},
        ]

        # Crear y colocar los botones
        for index, config in enumerate(botones_config):
            boton = ctk.CTkButton(
                self.subframe_barra_2,
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
        self.frame_fila = ctk.CTkFrame(contenedor, corner_radius=6)
        self.frame_fila.grid(row=fila, column=0, columnspan=6, sticky="nsew")
        self.frame_fila.columnconfigure(0, weight=1)
        self.frame_fila.rowconfigure(0, weight=1)
        self.frame_fila.rowconfigure(1, weight=4)

        self.frame_titulo = ctk.CTkFrame(self.frame_fila, fg_color=THEME["background"], corner_radius=0)
        self.frame_titulo.grid(row=0, column=0, sticky="nsew")

        # Crear el título de la fila
        self.label_titulo = ctk.CTkLabel(self.frame_titulo, text=titulo, font=("Arial", 25, "bold"), fg_color=THEME["background"], text_color="white")
        self.label_titulo.pack(anchor="w", padx=10)

        self.frame_contenido = ctk.CTkScrollableFrame(self.frame_fila, fg_color=THEME["background"], orientation="horizontal", height=300, corner_radius=0)
        self.frame_contenido.grid(row=1, column=0, sticky="nsew", padx=0)
        self.frame_contenido._scrollbar.grid_forget()  # Oculta scroll por estética

        self.filas_eventos.append(self.frame_fila)

        return self.frame_contenido

    def create_principal(self):
        self.frame_principal = ctk.CTkScrollableFrame(self, fg_color=THEME["background"])
        self.frame_principal.grid(row=1, column=1, sticky="nsew", padx=(0, 5), pady=(0, 5))
        self.frame_principal._scrollbar.grid_forget()
        for i in range(6):
            self.frame_principal.rowconfigure(i, weight=1)
        for i in range(3):
            self.frame_principal.columnconfigure(i, weight=1)

        #Evento grande en la parte superior
        self.principal_main = ctk.CTkFrame(self.frame_principal)
        self.principal_main.grid(row=0, column=0, sticky="nsew", columnspan=6)
        self.principal_main.columnconfigure(0, weight=1)
        self.principal_main.rowconfigure(0, weight=1)

        #contenido = self.obtener_imagenes_eventos()
        contenido = [
            {"type": "text", "text": TEXTOS["bienvenida"]},
            {"type": "image", "path": ASSETS["categorias"]["grande"] + "/grande1.png"},
            {"type": "text", "text": TEXTOS["organiza"]},
            {"type": "image", "path": ASSETS["categorias"]["grande"] + "/grande2.png"},
            {"type": "text", "text": TEXTOS["inolvidable"]},
            {"type": "image", "path": ASSETS["categorias"]["grande"] + "/grande3.png"},
            {"type": "text", "text": TEXTOS["celebra"]},
            {"type": "image", "path": ASSETS["categorias"]["grande"] + "/grande4.png"},
        ]
        self.evento_grande = CarruselDeslizante(self.principal_main, contenido, duracion=ANIMACION["duracion"], velocidad=ANIMACION["velocidad"], height=THEME["evento_height"])
        self.evento_grande.grid(sticky="nsew", pady=(0,3), padx=(0))

        # Filas de eventos (copia una fila para poner una nueva categoría de eventos)
        self.fila_cumple = self.crear_fila_eventos(self.frame_principal, fila=1, titulo="Cumpleaños")
        self.fila_fiestas = self.crear_fila_eventos(self.frame_principal, fila=2, titulo="Fiestas")
        self.fila_bodas = self.crear_fila_eventos(self.frame_principal, fila=3, titulo="Bodas")
        self.fila_xvs = self.crear_fila_eventos(self.frame_principal, fila=4, titulo="XV años")
        self.fila_graduaciones = self.crear_fila_eventos(self.frame_principal, fila=5, titulo="Graduaciones")
        #self.fila_eventos = self.crear_fila_eventos(self.frame_principal, fila=6, titulo="Eventos")

    def create_user(self):
        self.frame_user = ctk.CTkFrame(self)
        self.frame_user.grid(row=0, column=0, sticky="nsew", padx=(10, 5), pady=(10, 5))
        self.user = ctk.CTkButton(self.frame_user, text="", image=self.iconos["user"], fg_color="lightblue", corner_radius=8, width=60, height=60, command=self.verificar_sesion)
        self.user.grid(row=0, column=0, sticky="nsew")

    def cargar_imagenes_eventos(self):
        self.imagenes_eventos = {}

        def cargar():
            placeholder = ASSETS["placeholder"]
            for cat in CATEGORIAS_EVENTOS:
                carpeta = ASSETS["categorias"][cat["clave"]]
                prefijo = cat["clave"]
                cantidad = cat["cantidad"]
                imagenes = cargar_imagenes_desde_carpeta(
                    carpeta, prefijo, cantidad, size=(THEME["evento_width"], THEME["evento_height"]), placeholder_path=placeholder
                )
                self.imagenes_eventos.update(imagenes)
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
            #"eventos":  (self.fila_eventos, "evento"),
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

    def verificar_sesion(self):
        if Sesion.usuario_actual:
            print("Sesión activa con:", Sesion.usuario_actual)
            self.abrir_VentanaInicioSesion()
        else:
            print("No hay sesión activa.")
            self.abrir_login()
            
    def abrir_alerta_login(self):
        if Sesion.usuario_actual:
            print("Sesión activa con:", Sesion.usuario_actual)
        else:
            print("No hay sesión activa.")
            self.abrir_login()
        
    def abrir_login(self):
        print("Creando VentanaUsuario...")
        if hasattr(self, "ventana_usuario") and self.ventana_usuario.winfo_exists():
            print("Ya hay una ventana de usuario abierta.")
            return
        try:
            # Guardar la vista actual antes de abrir el login
            vista_actual = self.detectar_vista_actual()
            
            ventana = VentanaUsuario(self)
            # Esperar a que se cierre la ventana y luego reverificar
            self.wait_window(ventana)
            
            # Después de que se cierra, verificar sesión nuevamente
            if Sesion.usuario_actual:
                # Actualizar el icono del usuario
                self.user.configure(image=self.iconos["user2"])
                
                # Actualizar la vista actual según el contexto
                if vista_actual == "main":
                    self.abrir_main()
                elif vista_actual == "calendario" or vista_actual == "sin_sesion_calendario":
                    self.abrir_calendario()
                elif vista_actual == "mis_eventos" or vista_actual == "sin_sesion_mis_eventos":
                    self.abrir_mis_eventos()
                elif vista_actual == "ajustes":
                    self.abrir_ajustes()
                elif vista_actual == "invitacion":
                    self.abrir_invitacion()
                else:
                    # Por defecto ir a main
                    self.abrir_main()
            else:
                # Si no se inició sesión y estamos en main, cargar las imágenes
                if vista_actual == "main":
                    self.cargar_imagenes_en_filas()
                    
        except Exception as e:
            print("ERROR al crear VentanaUsuario:", e)

    def abrir_main(self):
        # Destruir frame_principal actual
        self.frame_principal.destroy()
        
        # Recrear frame_principal como scrolleable
        self.frame_principal = ctk.CTkScrollableFrame(self)
        self.frame_principal.grid(row=1, column=1, sticky="nsew", padx=(0, 5), pady=(0, 4))
        self.frame_principal._scrollbar.grid_forget()
        
        # Configurar grid
        for i in range(6):
            self.frame_principal.rowconfigure(i, weight=1)
        for i in range(3):
            self.frame_principal.columnconfigure(i, weight=1)
        
        # Vuelve a crear el contenido principal
        self.create_principal()
        if Sesion.usuario_actual:
            self.cargar_eventos()  # Cargar de BD
        else:
            self.cargar_imagenes_en_filas()

    def abrir_VentanaInicioSesion(self):
        try:
            # Guardar información sobre la vista actual antes de cambiarla
            self.guardar_estado_actual()
            
            # Destruir el frame principal actual
            self.frame_principal.destroy()
            
            # Crear nuevo frame_principal (normal)
            self.frame_principal = ctk.CTkFrame(self)
            self.frame_principal.grid(row=1, column=1, sticky="nsew", padx=(0, 5), pady=(0, 4))
            
            # Configurar grid del nuevo frame
            self.frame_principal.grid_columnconfigure(0, weight=1)
            self.frame_principal.grid_rowconfigure(0, weight=1)
            
            # Crear la ventana de inicio de sesión
            ventana_usuario = InicioSesion(self.frame_principal)
            ventana_usuario.pack(fill="both", expand=True)
        except Exception as e:
            print("ERROR al crear ventana inicio sesion:", e)
            import traceback
            traceback.print_exc()

    def abrir_info_eventos(self, evento_id):
        try:
            # Guardar información sobre la vista actual antes de cambiarla
            self.guardar_estado_actual()
            
            # Destruir el frame principal actual
            self.frame_principal.destroy()
            
            # Crear nuevo frame_principal (normal)
            self.frame_principal = ctk.CTkFrame(self)
            self.frame_principal.grid(row=1, column=1, sticky="nsew", padx=(0, 5), pady=(0, 4))
            
            # Configurar grid del nuevo frame
            self.frame_principal.grid_columnconfigure(0, weight=1)
            self.frame_principal.grid_rowconfigure(0, weight=1)
            
            # Crear la ventana de inicio de sesión
            info_eventos = DatosEventos(self.frame_principal, evento_id)
            info_eventos.pack(fill="both", expand=True)
        except Exception as e:
            print("ERROR al crear ventana de datos de eventos:", e)
            import traceback
            traceback.print_exc()        

    def abrir_calendario(self):
        # Limpia el frame_principal
        self.frame_principal.destroy()
        
        # Crear nuevo frame_principal (normal)
        self.frame_principal = ctk.CTkFrame(self)
        self.frame_principal.grid(row=1, column=1, sticky="nsew", padx=(0, 5), pady=(0, 4))
        
        # Configurar grid del nuevo frame
        self.frame_principal.grid_columnconfigure(0, weight=1)
        self.frame_principal.grid_rowconfigure(0, weight=1)
        # Inserta la Ventana de mis eventos dentro de frame_principal
        try:
            if Sesion.usuario_actual:
                calendario_actual = Calendario(self.frame_principal)
                calendario_actual.pack(fill="both", expand=True)
            else:
                frame_sin_sesion = SinSesión(self.frame_principal, titulo="Calendario")
                frame_sin_sesion.pack(fill="both", expand=True)    

        except Exception as e:
            print("ERROR al crear Ventana de Calendario:", e)

    def guardar_estado_actual(self):
        """Guarda el estado de la vista actual para poder restaurarla después"""
        self.vista_anterior = self.detectar_vista_actual()
        print(f"Guardando estado actual: {self.vista_anterior}")

    def detectar_vista_actual(self):
        """Detecta qué vista está actualmente activa"""
        if not hasattr(self, 'frame_principal') or not self.frame_principal.winfo_exists():
            return "main"
        
        # Verificar por widgets específicos o clases
        for widget in self.frame_principal.winfo_children():
            # Importar las clases para poder hacer isinstance
            try:
                if widget.__class__.__name__ == "MisEventos":
                    return "mis_eventos"
                elif widget.__class__.__name__ == "Calendario":
                    return "calendario"
                elif widget.__class__.__name__ == "SinSesión":
                    titulo = getattr(widget, 'titulo', '')
                    if "Calendario" in titulo:
                        return "sin_sesion_calendario"
                    elif "Mis Eventos" in titulo:
                        return "sin_sesion_mis_eventos"
                    return "sin_sesion"
                elif hasattr(widget, 'cget'):
                    try:
                        if widget.cget("text") == "Cambiar tema":
                            return "ajustes"
                    except:
                        pass
                elif widget.__class__.__name__ == "Ventana":  # Invitaciones
                    return "invitacion"
            except:
                continue
        
        # Verificar si es la vista principal buscando el carrusel o filas de eventos
        if hasattr(self, 'evento_grande'):
            try:
                if self.evento_grande.winfo_exists():
                    return "main"
            except:
                pass
        
        # Si hay filas de eventos visibles, probablemente es main
        try:
            for fila in self.filas_eventos:
                if fila.winfo_exists():
                    return "main"
        except:
            pass
        
        return "main"  # Por defecto

    def restaurar_vista_anterior(self):
        """Restaura la vista que estaba activa antes de abrir InicioSesion"""
        if not self.vista_anterior:
            self.abrir_main()
            return
            
        print(f"Restaurando vista anterior: {self.vista_anterior}")
        
        if self.vista_anterior == "main":
            self.abrir_main()
        elif self.vista_anterior == "calendario":
            self.abrir_calendario()
        elif self.vista_anterior == "mis_eventos":
            self.abrir_mis_eventos()
        elif self.vista_anterior == "ajustes":
            self.abrir_ajustes()
        elif self.vista_anterior == "invitacion":
            self.abrir_invitacion()
        elif self.vista_anterior == "sin_sesion_calendario":
            self.abrir_calendario()  # Esto mostrará SinSesión automáticamente si no hay sesión
        elif self.vista_anterior == "sin_sesion_mis_eventos":
            self.abrir_mis_eventos()  # Esto mostrará SinSesión automáticamente si no hay sesión
        else:
            # Por defecto, ir al main
            self.abrir_main()
        
        # Limpiar el estado guardado
        self.vista_anterior = None

    def abrir_mis_eventos(self):
        # Limpia el frame_principal
        self.frame_principal.destroy()
        
        # Crear nuevo frame_principal (normal)
        self.frame_principal = ctk.CTkFrame(self)
        self.frame_principal.grid(row=1, column=1, sticky="nsew", padx=(0, 10), pady=(0, 4))
        
        # Configurar grid del nuevo frame
        self.frame_principal.grid_columnconfigure(0, weight=1)
        self.frame_principal.grid_rowconfigure(0, weight=1)
        # Inserta la Ventana de mis eventos dentro de frame_principal
        try:
            if Sesion.usuario_actual:
                mis_eventos = MisEventos(self.frame_principal, self.abrir_invitacion)
                mis_eventos.pack(fill="both", expand=True)
            else:
                frame_sin_sesion = SinSesión(self.frame_principal, titulo="Mis Eventos")
                frame_sin_sesion.pack(fill="both", expand=True)    
        except Exception as e:
            print("ERROR al crear Ventana de Mis Eventos:", e)

    def abrir_invitacion(self):
        # Destruir frame_principal actual (scrolleable)
        self.frame_principal.destroy()
        
        # Crear nuevo frame_principal (normal)
        self.frame_principal = ctk.CTkFrame(self)
        self.frame_principal.grid(row=1, column=1, sticky="nsew", padx=(0, 10), pady=(0, 4))
        
        # Configurar grid del nuevo frame
        self.frame_principal.grid_columnconfigure(0, weight=1)
        self.frame_principal.grid_rowconfigure(0, weight=1)
        
        # Crear la invitación en el nuevo frame
        invitacion = Ventana(master=self.frame_principal)
        invitacion.grid(row=0, column=0, sticky="nsew")    

    def abrir_ajustes(self):
        self.frame_principal.destroy()
        
        # Crear nuevo frame_principal (normal)
        self.frame_principal = ctk.CTkFrame(self, fg_color="#C4DF62")
        self.frame_principal.grid(row=1, column=1, sticky="nsew", padx=(0, 5), pady=(0, 4))
        
        # Configurar grid del nuevo frame
        self.frame_principal.grid_columnconfigure(0, weight=1)
        self.frame_principal.grid_rowconfigure(0, weight=1)

        self.titulo = ctk.CTkLabel(self.frame_principal, text="Cambiar tema", font=("Eras Demi ITC", 75), text_color="#0A1A43")
        self.titulo.pack(pady=10)

        opcion = ctk.StringVar(value="")
        tema_actual = THEME["background"]
        valor_actual = ""
        if tema_actual == "#053d57":
            valor_actual = "opcion1"
        elif tema_actual == "#E4BE42":
            valor_actual = "opcion2"
        elif tema_actual == "#42A9E4":
            valor_actual = "opcion3"
        elif tema_actual == "#C4DF62":
            valor_actual = "opcion4"
        elif tema_actual == "#E44242":
            valor_actual = "opcion5"
        
        opcion.set(valor_actual)
        self.radio1 = ctk.CTkRadioButton(self.frame_principal, text="Default", variable=opcion, value="opcion1", font=("Arial", 40), text_color="#2b2b2b", command=lambda: self.actualizar_tema("background", "#053d57"))
        self.radio2 = ctk.CTkRadioButton(self.frame_principal, text="NARANJA", variable=opcion, value="opcion2", font=("Arial", 40), text_color="#2b2b2b", command=lambda: self.actualizar_tema("background", "#E4BE42"))
        self.radio3 = ctk.CTkRadioButton(self.frame_principal, text="CELESTE", variable=opcion, value="opcion3", font=("Arial", 40), text_color="#2b2b2b", command=lambda: self.actualizar_tema("background", "#42A9E4"))
        self.radio4 = ctk.CTkRadioButton(self.frame_principal, text="VERDE", variable=opcion, value="opcion4", font=("Arial", 40), text_color="#2b2b2b", command=lambda: self.actualizar_tema("background", "#C4DF62"))
        self.radio5 = ctk.CTkRadioButton(self.frame_principal, text="ROJO", variable=opcion, value="opcion5", font=("Arial", 40), text_color="#2b2b2b", command=lambda: self.actualizar_tema("background", "#E44242"))

        # Posicionarlos
        self.radio1.pack(pady=10, anchor='w', padx=20)
        self.radio2.pack(pady=10, anchor='w', padx=20)
        self.radio3.pack(pady=10, anchor='w', padx=20)
        self.radio4.pack(pady=10, anchor='w', padx=20)
        self.radio5.pack(pady=10, anchor='w', padx=20)

    def desordenar_filas(self):
        random.shuffle(self.filas_eventos)
        for i, fila in enumerate(self.filas_eventos):
            fila.grid_forget()
            fila.grid(row=i+1, column=0, columnspan=6, sticky="nsew")  # i+1 porque la fila 0 es el evento principal

    def limpiar_filas_eventos(self):
        """Limpia todas las imágenes de las filas de eventos"""
        categorias = {
            "cumple": self.fila_cumple,
            "fiesta": self.fila_fiestas,
            "boda": self.fila_bodas,
            "xv": self.fila_xvs,
            "graduacion": self.fila_graduaciones,
        }
        
        for _, fila_widget in categorias.items():
            for widget in fila_widget.winfo_children():
                widget.destroy()

    def actualizar_tema(self, clave, nuevo_valor):
        if clave in THEME:
            THEME[clave] = nuevo_valor
            print(f"Tema actualizado: {clave} = {nuevo_valor}")
            
            # AGREGAR ESTAS LÍNEAS:
            from config import guardar_config
            guardar_config()  # Guardar la configuración
            
            # Aplicar los cambios a la interfaz
            self.aplicar_cambios_tema()
        else:
            print(f"Error: '{clave}' no es una clave válida en THEME.")
        
    def aplicar_cambios_tema(self):
        """Actualiza todos los elementos que usan configuraciones del tema"""
        # Actualizar el fondo principal
        #self.configure(fg_color=THEME["background"])
        
        # Verificar si estamos en la sección de ajustes
        en_ajustes = False
        if hasattr(self, 'frame_principal'):
            for widget in self.frame_principal.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "Cambiar tema":
                    en_ajustes = True
                    break
        
        # Actualizar frame principal solo si no estamos en ajustes
        if hasattr(self, 'frame_principal') and not en_ajustes:
            self.frame_principal.configure(fg_color=THEME["background"])
        
        # Actualizar todos los frames con fondo del tema
        frames_con_tema = [
            self.frame_barra,
            self.barra,
            self.frame_fila,
            self.frame_contenido,
            self.fila_bodas,
            self.fila_cumple,
            self.fila_fiestas,
            self.fila_xvs,
            self.fila_graduaciones
        ]
        
        for frame in frames_con_tema:
            if frame and frame.winfo_exists():
                frame.configure(fg_color=THEME["background"])
        
        # Actualizar los subframes de la barra lateral
        if hasattr(self, 'frame_barra'):
            for widget in self.frame_barra.winfo_children():
                if isinstance(widget, ctk.CTkFrame):
                    widget.configure(fg_color=THEME["background"])
        
        # Actualizar botones del menú lateral
        botones = []
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkFrame):
                for subwidget in widget.winfo_children():
                    if isinstance(subwidget, ctk.CTkButton) and subwidget != self.user:
                        subwidget.configure(fg_color=THEME["button_fg"])
        
        # Actualizar etiquetas de títulos
        for fila in self.filas_eventos:
            for widget in fila.winfo_children():
                if isinstance(widget, ctk.CTkFrame):  # Frame de título
                    widget.configure(fg_color=THEME["background"])
                    for subwidget in widget.winfo_children():
                        if isinstance(subwidget, ctk.CTkLabel):
                            subwidget.configure(fg_color=THEME["background"])

    def realizar_busqueda(self):
        """Busca eventos según el texto en la barra de búsqueda y muestra los resultados"""
        termino_busqueda = self.barra.get().lower().strip()
        if not termino_busqueda:
            # Si la búsqueda está vacía, vuelve a la pantalla principal
            self.abrir_main()
            return
            
        # Limpiar el frame principal para mostrar resultados
        self.frame_principal.destroy()
        
        # Recrear frame_principal como scrolleable
        self.frame_principal = ctk.CTkScrollableFrame(self)
        self.frame_principal.grid(row=1, column=1, sticky="nsew", padx=(0, 10), pady=(0, 4))
        self.frame_principal._scrollbar.grid_forget()
        
        # Configurar grid
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(0, weight=0)
        self.frame_principal.rowconfigure(1, weight=1)
        
        # Título de resultados de búsqueda
        titulo_frame = ctk.CTkFrame(self.frame_principal, fg_color=THEME["background"], corner_radius=0)
        titulo_frame.grid(row=0, column=0, sticky="ew", pady=(5, 10))
        
        titulo_label = ctk.CTkLabel(titulo_frame, text=f"Resultados de búsqueda: '{termino_busqueda}'", 
                                font=("Arial", 25, "bold"), text_color="white", 
                                fg_color=THEME["background"])
        titulo_label.pack(anchor="w", padx=10, pady=5)
        
        # Contenedor para los resultados
        resultados_frame = ctk.CTkFrame(self.frame_principal, fg_color=THEME["background"])
        resultados_frame.grid(row=1, column=0, sticky="nsew", pady=5)
        resultados_frame.columnconfigure(0, weight=1)
        
        # Buscar coincidencias en todas las categorías
        resultados = self.buscar_eventos(termino_busqueda)
        
        if resultados:
            # Mostrar los resultados encontrados
            self.mostrar_resultados_busqueda(resultados_frame, resultados)
        else:
            # Mostrar mensaje de no resultados
            sin_resultados = ctk.CTkLabel(resultados_frame, text="No se encontraron resultados", 
                                        font=("Arial", 18), text_color="white", 
                                        fg_color=THEME["background"])
            sin_resultados.pack(pady=50)

    def buscar_eventos(self, termino):
        """
        Busca eventos que coincidan con el término de búsqueda
        Retorna una lista de diccionarios con información de los eventos encontrados
        """
        resultados = []
        
        # Categorías a buscar (puedes expandir esto para incluir datos reales de tu BD)
        categorias = {
            "cumple": "Cumpleaños",
            "fiesta": "Fiestas", 
            "boda": "Bodas",
            "xv": "XV años",
            "grad": "Graduaciones"
        }
        
        # Buscar en las imágenes de eventos (esto es un ejemplo básico)
        # En una implementación real, deberías buscar en tu base de datos
        for clave, imagen in self.imagenes_eventos.items():
            for prefijo, nombre_cat in categorias.items():
                if prefijo in clave and (
                    termino in nombre_cat.lower() or 
                    termino in clave.lower()
                ):
                    resultados.append({
                        "clave": clave,
                        "imagen": imagen,
                        "categoria": nombre_cat
                    })
        
        return resultados

    def mostrar_resultados_busqueda(self, contenedor, resultados):
        """Muestra los resultados de búsqueda en el contenedor especificado"""
        evento_height = 300
        evento_width = 400
        
        # Crear un frame por categoría para agrupar resultados
        categorias_encontradas = {}
        
        for resultado in resultados:
            categoria = resultado["categoria"]
            if categoria not in categorias_encontradas:
                # Crear frame para esta categoría
                cat_frame = ctk.CTkFrame(contenedor, fg_color=THEME["background"], corner_radius=0)
                cat_frame.pack(fill="x", pady=10)
                
                # Título de la categoría
                ctk.CTkLabel(cat_frame, text=categoria, font=("Arial", 20, "bold"), 
                        text_color="white", fg_color=THEME["background"]).pack(anchor="w", padx=10)
                
                # Frame para los eventos de esta categoría
                eventos_frame = ctk.CTkFrame(cat_frame, fg_color=THEME["background"])
                eventos_frame.pack(fill="x", padx=10, pady=5)
                
                categorias_encontradas[categoria] = eventos_frame
                
        # Mostrar las imágenes en sus respectivas categorías
        for resultado in resultados:
            cat_frame = categorias_encontradas[resultado["categoria"]]
            imagen = resultado["imagen"]
            
            # Crear un frame contenedor para cada evento
            evento_frame = ctk.CTkFrame(cat_frame, fg_color=THEME["background"])
            evento_frame.pack(side="left", padx=5, pady=5)
            
            # Agregar la imagen
            label = ctk.CTkLabel(evento_frame, image=imagen, text="", 
                            width=evento_width, height=evento_height)
            label.pack()
            
            # Agregar el nombre/ID del evento (opcional)
            nombre_evento = resultado["clave"]
            ctk.CTkLabel(evento_frame, text=nombre_evento, text_color="white").pack()

    def cargar_eventos(self):
        """Carga eventos desde la base de datos y los muestra"""
        if not Sesion.usuario_actual:
            return
            
        from sqlalchemy.orm import sessionmaker
        import io
        
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            eventos = session.query(Evento).all()
            
            # Limpiar filas actuales
            for widget in self.fila_cumple.winfo_children():
                widget.destroy()
            for widget in self.fila_fiestas.winfo_children():
                widget.destroy()
            for widget in self.fila_bodas.winfo_children():
                widget.destroy()
            for widget in self.fila_xvs.winfo_children():
                widget.destroy()
            for widget in self.fila_graduaciones.winfo_children():
                widget.destroy()
            
            # Mostrar eventos
            for evento in eventos:
                if evento.imagen_bytes:
                    try:
                        imagen_pil = Image.open(io.BytesIO(evento.imagen_bytes))
                        imagen_pil = imagen_pil.resize((400, 300))
                        imagen_ctk = ctk.CTkImage(imagen_pil, size=(400, 300))
                        
                        # Decidir en qué fila va según el tipo
                        fila = None
                        if evento.tipo_evento == 'Cumpleaños':
                            fila = self.fila_cumple
                        elif evento.tipo_evento == 'Fiesta':
                            fila = self.fila_fiestas
                        elif evento.tipo_evento == 'Boda':
                            fila = self.fila_bodas
                        elif evento.tipo_evento == 'XVAnos':
                            fila = self.fila_xvs
                        elif evento.tipo_evento == 'Graduacion':
                            fila = self.fila_graduaciones
                        
                        if fila:
                            label = ctk.CTkLabel(fila, image=imagen_ctk, text="", width=400, height=300)
                            label.evento_id = evento.id_evento
                            label.evento_fecha = evento.fecha
                            label.evento_hora = evento.hora
                            label.pack(side="left", padx=5, pady=5)
                            label.bind("<Button-1>", lambda e, eid=evento.id_evento: self.on_evento_click(eid))

                    except Exception as e:
                        print(f"Error procesando evento ID {evento.id_evento}: {e}")
                        continue

        except Exception as e:
            print(f"Error: {e}")
        finally:
            session.close()

    def on_evento_click(self, evento_id):
        """Maneja el click en un evento"""
        print(f"Evento clickeado con ID: {evento_id}")
        self.abrir_info_eventos(evento_id)

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