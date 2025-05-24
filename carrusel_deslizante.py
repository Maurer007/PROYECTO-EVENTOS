import customtkinter as ctk
from PIL import Image, ImageTk
import itertools

class CarruselDeslizante(ctk.CTkFrame):
    def __init__(
        self, master, content, width=400, height=300,
        bg_color="#FFFFFF", text_font=("Arial", 20),
        text_fg="#FFFFFF", text_bg="#518D65",
        duracion=3000, velocidad=5, **kwargs
    ):
        super().__init__(master, **kwargs)
        self.width = width
        self.height = height
        self.duracion = duracion
        self.velocidad = velocidad
        self.content = content
        self.bg_color = bg_color
        self.text_font = text_font
        self.text_fg = text_fg
        self.text_bg = text_bg

        self.canvas = ctk.CTkCanvas(self, width=width, height=height, highlightthickness=0, bg=bg_color)
        self.canvas.pack()

        # Cargar imágenes
        for item in self.content:
            if item["type"] == "image":
                img = Image.open(item["path"]).resize((width, height), Image.LANCZOS)
                item["image"] = ImageTk.PhotoImage(img)

        # Widgets reutilizables
        self.image_label = ctk.CTkLabel(self.canvas, text="")
        self.text_label = ctk.CTkLabel(
            self.canvas, text="", font=self.text_font,
            width=width, height=height,
            fg_color=self.text_bg, text_color=self.text_fg
        )

        self.ciclo = itertools.cycle(self.content)
        self.current_window = None
        self.next_window = None

        self.mostrar_siguiente()

    def animar_transicion(self, x_salida=0, x_entrada=None):
        if x_entrada is None:
            x_entrada = self.width
        # Mover ventana actual y siguiente hacia la izquierda
        self.canvas.coords(self.current_window, x_salida, 0)
        self.canvas.coords(self.next_window, x_entrada, 0)

        if x_entrada <= 0:
            # Fin de la animación
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
        # Preparar widget nuevo
        if item["type"] == "image":
            self.image_label.configure(image=item["image"])
            widget = self.image_label
        else:
            self.text_label.configure(text=item["text"])
            widget = self.text_label

        # Crear ventana para widget entrante fuera del canvas (a la derecha)
        self.next_window = self.canvas.create_window(
            self.width, 0, anchor="nw", window=widget
        )

        if self.current_window is None:
            # Primer widget: colocarlo sin animación
            self.canvas.coords(self.next_window, 0, 0)
            self.current_window = self.next_window
            self.next_window = None
            self.after(self.duracion, self.mostrar_siguiente)
        else:
            self.animar_transicion()

# Ejemplo de uso:
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x400")
    app.title("Carrusel deslizante")

    contenido = [
        {"type": "image", "path": "assets/cumples/cumple1.png"},
        {"type": "text", "text": "Este es un mensaje"},
        {"type": "image", "path": "assets/Logo/logo.png"},
        {"type": "text", "text": "Otro mensaje importante"},
    ]

    carrusel = CarruselDeslizante(
        app, contenido, width=400, height=300,
        duracion=3000, velocidad=5
    )
    carrusel.pack(pady=40)

    app.mainloop()