import customtkinter as ctk
from PIL import Image, ImageTk
import itertools
from utils.carga_imagenes import cargar_imagenes_desde_carpeta

class CarruselDeslizante(ctk.CTkFrame):
    def __init__(
        self, master, content, width=None, height=300,
        bg_color="#FFFFFF", text_font=("Arial", 100),
        text_fg="#FFFFFF", text_bg="#518D65",
        duracion=3000, velocidad=5, **kwargs
    ):
        super().__init__(master, **kwargs)
        self.height = height
        self.duracion = duracion
        self.velocidad = velocidad
        self.content = content
        self.bg_color = bg_color
        self.text_font = text_font
        self.text_fg = text_fg
        self.text_bg = text_bg

        self.canvas = ctk.CTkCanvas(self, width=width, height=height, highlightthickness=0, bg=bg_color)
        self.canvas.pack(fill="both", expand=True)

        self.image_label = ctk.CTkLabel(self.canvas, text="")
        self.text_label = ctk.CTkLabel(
            self.canvas, text="", font=self.text_font,
            fg_color=self.text_bg, text_color=self.text_fg
        )

        self.ciclo = itertools.cycle(self.content)
        self.current_window = None
        self.next_window = None

        self.bind("<Configure>", self._on_resize)
        self._resize_images_and_labels()
        self.after(0, self.mostrar_siguiente)
        self._imagenes_procesadas = False

    def cargar_imagenes_desde_carpeta(self, carpeta, prefijo, cantidad, placeholder_path=None, sharpen=True, allow_upscale=True):
        """Carga imágenes usando el método de carga optimizado"""
        width = self.winfo_width() or 800
        imagenes_cargadas = cargar_imagenes_desde_carpeta(
            carpeta=carpeta,
            prefijo=prefijo,
            cantidad=cantidad,
            size=(width, self.height),
            placeholder_path=placeholder_path,
            sharpen=sharpen,
            allow_upscale=allow_upscale
        )
        
        # Convertir a formato del carrusel y agregar al contenido
        for clave, imagen_ctk in imagenes_cargadas.items():
            self.content.append({
                "type": "image",
                "image": imagen_ctk,
                "key": clave
            })
        
        # Recrear el ciclo con el nuevo contenido
        self.ciclo = itertools.cycle(self.content)
        return len(imagenes_cargadas)

    def _on_resize(self, event):
        self.canvas.config(width=event.width)
        self._resize_images_and_labels()

    def _resize_images_and_labels(self):
        contenedor_width = self.winfo_width()
        if contenedor_width < 2:
            return  # Evita errores si el frame aún no tiene tamaño
        self.width = contenedor_width
        for item in self.content:
            if item["type"] == "image":
                img = Image.open(item["path"])
                w_percent = self.width / float(img.size[0])
                new_height = int(float(img.size[1]) * w_percent)
                img = img.resize((self.width, new_height), Image.LANCZOS)
                top = max(0, (new_height - self.height) // 2)
                bottom = top + self.height
                img = img.crop((0, top, self.width, bottom))
                item["image"] = ctk.CTkImage(img, size=(self.width, self.height))
        self.image_label.configure(width=self.width, height=self.height)
        self.text_label.configure(width=self.width, height=self.height, font=self.text_font)

    def animar_transicion(self, x_salida=0, x_entrada=None):
        contenedor_width = self.winfo_width()
        if x_entrada is None:
            x_entrada = contenedor_width
        self.canvas.coords(self.current_window, x_salida, 0)
        self.canvas.coords(self.next_window, x_entrada, 0)

        if x_entrada - self.velocidad <= 0:
            self.canvas.coords(self.next_window, 0, 0)
            self.canvas.delete(self.current_window)
            self.current_window = self.next_window
            self.next_window = None
            self.after(self.duracion, self.mostrar_siguiente)
            return

        self.after(11, lambda: self.animar_transicion(
            x_salida - self.velocidad, x_entrada - self.velocidad
        ))

    def mostrar_siguiente(self):
        item = next(self.ciclo)
        if item["type"] == "image" and "image" in item:
            self.image_label.configure(image=item["image"])
            widget = self.image_label
        elif item["type"] == "text":
            self.text_label.configure(text=item["text"])
            widget = self.text_label
        else:
            return  # Si no hay imagen procesada, no muestra nada

        contenedor_width = self.winfo_width()
        self.next_window = self.canvas.create_window(
            contenedor_width, 0, anchor="nw", window=widget
        )

        if self.current_window is None:
            self.canvas.coords(self.next_window, 0, 0)
            self.current_window = self.next_window
            self.next_window = None
            self.after(self.duracion, self.mostrar_siguiente)
        else:
            self.animar_transicion()