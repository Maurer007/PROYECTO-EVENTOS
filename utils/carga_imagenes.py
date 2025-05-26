
from PIL import Image
import customtkinter as ctk
import os
import concurrent.futures

def cargar_imagenes_desde_carpeta(carpeta, prefijo, cantidad, size=(400, 300), placeholder_path=None):
    """
    Carga imágenes en paralelo desde una carpeta, usando un prefijo y cantidad.
    Devuelve un diccionario {clave: imagen}.
    Si una imagen falla, usa un placeholder si se proporciona.
    """
    imagenes = {}
    rutas = [(f"{prefijo}{i}", os.path.join(carpeta, f"{prefijo}{i}.png")) for i in range(1, cantidad + 1)]
    placeholder_img = None
    if placeholder_path:
        try:
            placeholder_img = ctk.CTkImage(Image.open(placeholder_path), size=size)
        except Exception:
            placeholder_img = None

    def cargar_uno(clave_ruta):
        clave, ruta = clave_ruta
        try:
            return clave, ctk.CTkImage(Image.open(ruta), size=size)
        except Exception as e:
            print(f"Error al cargar {ruta}: {e}")
            return clave, placeholder_img

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for clave, imagen in executor.map(cargar_uno, rutas):
            if imagen:
                imagenes[clave] = imagen
    return imagenes
