import customtkinter as ctk
from PIL import Image, ImageTk
import itertools

# Configuración inicial
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x400")
app.title("Carrusel")

# Contenedor principal
slider = ctk.CTkFrame(app, width=400, height=300, fg_color="#518D65")
slider.pack(pady=40)

# Contenido a mostrar
content = [
    {"type": "image", "path": "assets/cumples/cumple1.png"},
    {"type": "text", "text": "Este es un mensaje"},
    {"type": "image", "path": "assets/Logo/logo.png"},
    {"type": "text", "text": "Otro mensaje importante"},
]

# Cargar imágenes
for item in content:
    if item["type"] == "image":
        img = Image.open(item["path"]).resize((400, 300), Image.LANCZOS)
        item["image"] = ImageTk.PhotoImage(img)

# Widgets reutilizables
image_label = ctk.CTkLabel(slider, text="")
text_label = ctk.CTkLabel(slider, text="", font=("Arial", 20), width=400, height=300)

# Iterador cíclico
ciclo = itertools.cycle(content)

# Función para actualizar el contenido
def mostrar_siguiente():
    item = next(ciclo)
    image_label.pack_forget()
    text_label.pack_forget()

    if item["type"] == "image":
        image_label.configure(image=item["image"])
        image_label.pack()
    else:
        text_label.configure(text=item["text"])
        text_label.pack()

    app.after(3000, mostrar_siguiente)

# Iniciar carrusel
mostrar_siguiente()
app.mainloop()
