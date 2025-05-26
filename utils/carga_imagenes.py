
from PIL import Image, ImageOps, ImageFilter
import customtkinter as ctk
import os
import concurrent.futures

def cargar_imagenes_desde_carpeta(
    carpeta, 
    prefijo, 
    cantidad, 
    size=(400, 300), 
    placeholder_path=None, 
    sharpen=True, 
    allow_upscale=True
):
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
            img = Image.open(ruta).convert("RGBA") 
            orig_w, orig_h = img.size
            target_w, target_h = size

            # Evitar ampliación si no se permite
            if not allow_upscale and (orig_w < target_w or orig_h < target_h):
                # Centrar la imagen en un fondo transparente o blanco
                fondo = Image.new("RGBA", size, (255, 255, 255, 0))
                img = ImageOps.contain(img, size, method=Image.LANCZOS)
                offset = ((target_w - img.width) // 2, (target_h - img.height) // 2)
                fondo.paste(img, offset, img)
                img = fondo
            else:
                img = ImageOps.fit(img, size, method=Image.LANCZOS)

            # Aplicar filtro de nitidez si se desea
            if sharpen:
                img = img.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3))

            return clave, ctk.CTkImage(img, size=size)
        except Exception as e:
            print(f"Error al cargar {ruta}: {e}")
            return clave, placeholder_img

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for clave, imagen in executor.map(cargar_uno, rutas):
            if imagen:
                imagenes[clave] = imagen
    return imagenes
