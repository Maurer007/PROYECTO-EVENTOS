import json
import os

# Archivo para guardar configuraciones
CONFIG_FILE = "user_config.json"

def guardar_config():
    """Guarda la configuración actual en un archivo JSON"""
    try:
        config_data = {
            "theme_background": THEME["background"]
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config_data, f)
    except Exception as e:
        print(f"Error al guardar configuración: {e}")

def cargar_config():
    """Carga la configuración desde el archivo JSON"""
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                config_data = json.load(f)
                if "theme_background" in config_data:
                    THEME["background"] = config_data["theme_background"]
    except Exception as e:
        print(f"Error al cargar configuración: {e}")

# Rutas de assets
ASSETS = {
    "iconos": "assets/iconos/",
    "placeholder": "assets/placeholder.png",
    "categorias": {
        "cumple": "assets/cumples",
        "boda": "assets/bodas",
        "fiesta": "assets/fiestas",
        "xv": "assets/xvs",
        "grad": "assets/graduaciones",
        "evento": "assets/eventos",
        "grande": "assets/grandes",
    }
}

# Iconos
ICONOS = {
    "user": "user.png",
    "user2": "user2.png",
    "lupa": "lupa.png",
    "home": "home.png",
    "calendario": "calendario.png",
    "mis_eventos": "mis_eventos.png",
    "notificaciones": "notificaciones.png",
    "ajustes": "ajustes.png",
    "logout": "logout.png"
}

# Temas y colores
THEME = {
    "background": "#053d57",
    "text": "black",
    "placeholder": "white",
    "button_fg": "white",
    "evento_height": 300,
    "evento_width": 400,
    "font_main": ("Arial", 25, "bold"),
    "font_title": ("Arial", 30),
}


# Categorías de eventos
CATEGORIAS_EVENTOS = [
    {"nombre": "Cumpleaños", "clave": "cumple", "cantidad": 10},
    {"nombre": "Fiestas", "clave": "fiesta", "cantidad": 10},
    {"nombre": "Bodas", "clave": "boda", "cantidad": 10},
    {"nombre": "XV años", "clave": "xv", "cantidad": 10},
    {"nombre": "Graduaciones", "clave": "grad", "cantidad": 10},
    {"nombre": "Eventos", "clave": "evento", "cantidad": 10},
    {"nombre": "Grandes", "clave": "grande", "cantidad": 4},
]

# Textos
TEXTOS = {
    "bienvenida": "¡Bienvenido a JoinUp!",
    "organiza": "¡Así podrías anunciar tu fiesta!",
    "inolvidable": "¡Haz tu evento inolvidable!",
    "celebra": "¡Celebra con nosotros!",
    "barra_busqueda": "Barra de búsqueda",
    "horarios": "HORARIOS",
    "mostrar_horarios": "MOSTRAR HORARIOS",
}

# Parámetros de animación
ANIMACION = {
    "duracion": 3000,
    "velocidad": 8,
    "max_workers": 30,
}

