import customtkinter as CTk
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.filedialog as filedialog
from tkinter import colorchooser
import webcolors, random, string
from tkinter import messagebox
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from utils.orm_utils import Session
from models.evento import Evento, Fiesta, Cumpleaños, Graduacion, XVAnos, Boda 
import json
from pathlib import Path

def cargar_id_usuario_json(ruta="usuario_sesion.json"):
    if not Path(ruta).exists():
        return None
    with open(ruta, "r") as f:
        data = json.load(f)
        return data.get("id_usuario")
class EventosManager:
    
    @staticmethod
    def insertar_fiesta(anfitrion_id,imagen_bytes, fecha, hora, direccion, num_invitados, privacidad, descripcion):
        anfitrion_id = cargar_id_usuario_json()
        if anfitrion_id is None:
            print("No hay usuario logueado")
            return False
        session = Session()
        try:
            nuevo_evento = Evento(
                anfitrion_id=anfitrion_id,
                imagen_bytes=imagen_bytes,
                tipo_evento="Fiesta",
                fecha=fecha,
                hora=hora,
                direccion=direccion,
                num_invitados=num_invitados,
                privacidad=privacidad
                
            )
            session.add(nuevo_evento)
            session.commit()

            fiesta = Fiesta(
                id_evento=nuevo_evento.id_evento,
                anfitrion_id=anfitrion_id,
                imagen_bytes=imagen_bytes,
                tipo_evento="Fiesta",
                fecha=fecha,
                hora=hora,
                direccion=direccion,
                num_invitados=num_invitados,
                privacidad=privacidad,
                descripcion=descripcion,
                
            )
            session.add(fiesta)
            session.commit()
            return True

        except SQLAlchemyError as e:
            session.rollback()
            print(f"❌ Error al registrar: {e}")
            return False

        finally:
            session.close()
    @staticmethod
    def insertar_cumpleaños(anfitrion_id,imagen_bytes, fecha, hora, direccion, num_invitados, privacidad, cumpleañero, edad, mesa_regalos, imagen=None):
        anfitrion_id = cargar_id_usuario_json()
        if anfitrion_id is None:
            print("No hay usuario logueado")
            return False
        session = Session()
        try:
            nuevo_evento = Evento(
                anfitrion_id=anfitrion_id,
                imagen_bytes=imagen_bytes,
                tipo_evento="Cumpleaños",
                fecha=fecha,
                hora=hora,
                direccion=direccion,
                num_invitados=num_invitados,
                privacidad=privacidad
                
            )
            session.add(nuevo_evento)
            session.commit()

            cumpleaños = Cumpleaños(
                id_evento=nuevo_evento.id_evento,
                anfitrion_id=anfitrion_id,
                imagen_bytes=imagen_bytes,
                tipo_evento="Cumpleaños",
                fecha=fecha,
                hora=hora,
                direccion=direccion,
                num_invitados=num_invitados,
                privacidad=privacidad,
                cumpleañero=cumpleañero,
                edad=edad,
                mesa_regalos=mesa_regalos
            )
            session.add(cumpleaños)
            session.commit()
            return True

        except SQLAlchemyError as e:
            session.rollback()
            print(f"❌ Error al registrar: {e}")
            return False

        finally:
            session.close()

    @staticmethod
    def insertar_graduacion(anfitrion_id,imagen_bytes, fecha, hora, direccion, num_invitados, privacidad, escuela, nivel_educativo, generacion, invitados_por_alumno, imagen=None):
        anfitrion_id = cargar_id_usuario_json()
        if anfitrion_id is None:
            print("No hay usuario logueado")
            return False
        session = Session()
        try:
            nuevo_evento = Evento(
                anfitrion_id=anfitrion_id,
                imagen_bytes=imagen_bytes,
                tipo_evento="Graduacion",
                fecha=fecha,
                hora=hora,
                direccion=direccion,
                num_invitados=num_invitados,
                privacidad=privacidad
                
            )
            session.add(nuevo_evento)
            session.commit()

            graduacion = Graduacion(
                id_evento=nuevo_evento.id_evento,
                anfitrion_id=anfitrion_id,
                imagen_bytes=imagen_bytes,
                tipo_evento="Graduacion",
                fecha=fecha,
                hora=hora,
                direccion=direccion,
                num_invitados=num_invitados,
                privacidad=privacidad,
                escuela=escuela,
                nivel_educativo=nivel_educativo,
                generacion=generacion,
                invitados_por_alumno=invitados_por_alumno
            )
            session.add(graduacion)
            session.commit()
            return True

        except SQLAlchemyError as e:
            session.rollback()
            print(f"❌ Error al registrar: {e}")
            return False

        finally:
            session.close()
    
    @staticmethod
    def insertar_xv(anfitrion_id,imagen_bytes, fecha, hora, direccion, num_invitados, privacidad, cumpleañero_xv, padre, madre, padrino, madrina, mesa_regalos_xv, imagen=None):
        anfitrion_id = cargar_id_usuario_json()
        if anfitrion_id is None:
            print("No hay usuario logueado")
            return False
        session = Session()
        try:
            nuevo_evento = Evento(
                anfitrion_id=anfitrion_id,
                imagen_bytes=imagen_bytes,
                tipo_evento="XVAños",
                fecha=fecha,
                hora=hora,
                direccion=direccion,
                num_invitados=num_invitados,
                privacidad=privacidad
                
            )
            session.add(nuevo_evento)
            session.commit()

            xv = XVAnos(
                id_evento=nuevo_evento.id_evento,
                anfitrion_id=anfitrion_id,
                imagen_bytes=imagen_bytes,
                tipo_evento="XV Años",
                fecha=fecha,
                hora=hora,
                direccion=direccion,
                num_invitados=num_invitados,
                privacidad=privacidad,
                cumpleañero_xv=cumpleañero_xv,
                padre=padre,
                madre=madre,
                padrino=padrino,
                madrina=madrina,
                mesa_regalos_xv=mesa_regalos_xv
            )
            session.add(xv)
            session.commit()
            return True

        except SQLAlchemyError as e:
            session.rollback()
            print(f"❌ Error al registrar: {e}")
            return False

        finally:
            session.close()
        
    @staticmethod
    def insertar_boda(anfitrion_id,imagen_bytes, fecha, hora, direccion, num_invitados, privacidad, novia, novio, padrino_boda, madrina_boda, mesa_regalos_boda, misa, iglesia, menores_permitidos, imagen=None):
        anfitrion_id = cargar_id_usuario_json()
        if anfitrion_id is None:
            print("No hay usuario logueado")
            return False
        session = Session()
        try:
            nuevo_evento = Evento(
                anfitrion_id=anfitrion_id,
                imagen_bytes=imagen_bytes,
                tipo_evento="Boda",
                fecha=fecha,
                hora=hora,
                direccion=direccion,
                num_invitados=num_invitados,
                privacidad=privacidad
                
            )
            session.add(nuevo_evento)
            session.commit()

            boda = Boda(
                id_evento=nuevo_evento.id_evento,
                anfitrion_id=anfitrion_id,
                imagen_bytes=imagen_bytes,
                tipo_evento="Boda",
                fecha=fecha,
                hora=hora,
                direccion=direccion,
                num_invitados=num_invitados,
                privacidad=privacidad,
                novia=novia,
                novio=novio,
                padrino_boda=padrino_boda,
                madrina_boda=madrina_boda,
                mesa_regalos_boda=mesa_regalos_boda,
                misa=misa,
                iglesia=iglesia,
                menores_permitidos=menores_permitidos
            )
            session.add(boda)
            session.commit()
            return True

        except SQLAlchemyError as e:
            session.rollback()
            print(f"❌ Error al registrar: {e}")
            return False

        finally:
            session.close()
       
class Ventana(CTk.CTkFrame):

    def __init__(self, master=None):
        super().__init__(master)

        self.anfitrion_id = self.recuperar_id

        # Configuración inicial del tema
        CTk.set_appearance_mode("System")
        CTk.set_default_color_theme("blue")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
    
        self.crear_interfaz()
        self.colores_agregados = []  # Lista para guardar los colores
        self.limite_colores = 5

        self.imagen = None

        self.paquetes_frames = {
        "Fiesta": self.crear_fiesta,
        "Cumpleaños": self.crear_cumple,
        "Graduación": self.crear_grad,
        "XV Años": self.crear_xv,
        "Boda": self.crear_boda
        }
        #Valores para los botones de aumento y disminuyo
        self.valor_edad = 1  # Edad mínima
        self.valor_generacion = 2000  # Generación inicial mínima
        self.valor_inv_grad = 0 # Invitados minimo permitidos por graduado

        # Obtener fecha y hora actual
        self.fecha_actual = datetime.now().strftime("%d/%m/%Y")
        self.hora_actual = datetime.now().strftime("%H:%M")  # Formato 24 horas
        self.entry_cumpleanero = None
        
    def recuperar_id(self):
        engine = create_engine("sqlite:///db/app.db")
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            if not Sesion.usuario_actual:
                raise ValueError("No hay usuario en sesión.")

            # Recuperar el objeto completo del usuario
            user = session.query(Usuario).filter_by(nom_usuario=Sesion.usuario_actual).first()
            id = user.id_usuario

        except (SQLAlchemyError, ValueError) as e:
            print("Error al obtener credenciales:", e)  

        return id      

    def validar_fecha_input(self, texto):
        if texto == "":
            return True  # Permitir borrar todo
    
        if not all(c in "0123456789/" for c in texto) or len(texto) > 10:
            return False

    # Validar formato dd/mm/yyyy mínimo para validaciones
        if len(texto) == 10 and texto[2] == '/' and texto[5] == '/':
            dia_str = texto[0:2]
            mes_str = texto[3:5]
            # año_str = texto[6:10]  # opcional si quieres validar año
        
            try:
               dia = int(dia_str)
               mes = int(mes_str)
            except ValueError:
                return False
        
            if not (1 <= mes <= 12):
                return False
        
        # Días máximos por mes (febrero con 28 días sin bisiestos)
            dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            max_dias = dias_por_mes[mes - 1]
            if not (1 <= dia <= max_dias):
                return False
        
            return True

    # Si la longitud es menor a 10 aún no validar día/mes
        return True


    def validar_hora_input(self, texto):
        if texto == "":
            return True  # permitir borrar todo
        return all(c in "0123456789:" for c in texto) and len(texto) <= 5

    def formato_auto_fecha(self, event):
        contenido = self.entry_fecha.get()
        contenido = contenido.replace("/", "")  # eliminar / si el usuario lo puso
        if len(contenido) == 2 or len(contenido) == 4:
            self.entry_fecha.delete(0, "end")
            nuevo_contenido = contenido[:2] + "/" + contenido[2:]
            if len(contenido) > 2:
                nuevo_contenido = nuevo_contenido[:5] + "/" + nuevo_contenido[5:]
            self.entry_fecha.insert(0, nuevo_contenido)

    def formato_auto_hora(self, event):
        contenido = self.entry_hora.get()
        contenido = contenido.replace(":", "")  # eliminar : si el usuario lo puso
        if len(contenido) == 2:
            self.entry_hora.delete(0, "end")
            nuevo_contenido = contenido[:2] + ":" + contenido[2:]
            self.entry_hora.insert(0, nuevo_contenido)

    def manejar_clasificacion(self, seleccion):
        self.seleccion_actual = seleccion

    # Vaciar etiquetas dinámicas anteriores
        self.vaciar_paquete()

    # Llamar a la función que crea el formulario del evento
        if seleccion in self.paquetes_frames:
            self.paquetes_frames[seleccion]()  # Esto debe incluir también los labels

    # Destruir frames anteriores si existen
    #    if hasattr(self, 'paquete_actual'):
   #         for frame in self.paquete_actual:
    #            try:
    #                frame.destroy()
    #            except:
    #                pass
    #    self.paquete_actual = []

    # Llamar a la función correspondiente usando el diccionario
    #    if seleccion in self.paquetes_frames:
    #        self.paquetes_frames[seleccion]()

    def alternar_widget(self, widget, mostrar=True, metodo="grid"):
        if mostrar:
            if metodo == "grid":
                widget.grid()
            elif metodo == "pack":
                widget.pack()
            elif metodo == "place":
                widget.place()
        else:
            if metodo == "grid":
                widget.grid_remove()
            elif metodo == "pack":
                widget.pack_forget()
            elif metodo == "place":
                widget.place_forget()

    def toggle_widgets_by_checkbox(self, checkbox_var, widgets, metodo="grid"):
        mostrar = checkbox_var.get()
        for w in widgets:
            self.alternar_widget(w, mostrar=mostrar, metodo=metodo)

    def toggle_widgets_by_combobox(self, combobox_widget, widgets_por_valor, metodo="grid"):
        valor = combobox_widget.get()
        for key, widgets in widgets_por_valor.items():
            mostrar = (key == valor)
            for w in widgets:
                self.alternar_widget(w, mostrar=mostrar, metodo=metodo)

    def seleccionar_imagen(self):
        ruta_imagen = filedialog.askopenfilename(
            filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.bmp")]
        )
        if ruta_imagen:
        # Leer la imagen como bytes para guardar en la DB
            with open(ruta_imagen, "rb") as f:
                self.imagen = f.read()
                print("✅ Imagen cargada correctamente. Tamaño en bytes:", len(self.imagen))
            
    def vaciar_paquete(self):
        if hasattr(self, 'paquete_actual'):
            for frame in self.paquete_actual:
                try:
                    frame.destroy()
                except:
                    pass
        self.paquete_actual = []
        self.frame_form.update_idletasks()  # <- fuerza a que el layout se actualice

    def aumentar_edad(self):
        self.valor_edad += 1
        self.label_num_edad.configure(text=str(self.valor_edad))

    def disminuir_edad(self):
        if self.valor_edad > 1:
            self.valor_edad -= 1
            self.label_num_edad.configure(text=str(self.valor_edad))

    def aumentar_generacion(self):
        self.valor_generacion += 1
        if self.valor_generacion > 9999:  # límite visual de 4 dígitos
            self.valor_generacion = 9999
        self.entry_generacion.configure(text=str(self.valor_generacion))

    def disminuir_generacion(self):
        if self.valor_generacion > 2000:
            self.valor_generacion -= 1
            self.entry_generacion.configure(text=str(self.valor_generacion))

    def aumentar_inv_grad(self):
        self.valor_inv_grad += 1
        self.label_num_inv_x_grad.configure(text=str(self.valor_inv_grad))

    def disminuir_inv_grad(self):
        if self.valor_inv_grad > 1:
            self.valor_inv_grad -= 1
            self.label_num_inv_x_grad.configure(text=str(self.valor_inv_grad))

    def generar_codigo_seguro(self, longitud=10):
        while True:
            caracteres = string.ascii_letters + string.digits + string.punctuation
            codigo = ''.join(random.choice(caracteres) for _ in range(longitud))
            # Validar que tenga al menos un carácter de cada tipo_evento
            if (any(c.islower() for c in codigo) and
                any(c.isupper() for c in codigo) and
                any(c.isdigit() for c in codigo) and
                any(c in string.punctuation for c in codigo)):
                return codigo

    def generar_y_mostrar_codigo(self):
        codigo = self.generar_codigo_seguro()
        self.label_codigo_priv.configure(text=codigo)
        self.label_codigo_priv.grid()  # Muestra el label solo cuando hay código

    def copiar_codigo_al_portapapeles(self):
        codigo = self.label_codigo_priv.cget("text")
        if codigo:
            self.clipboard_clear()
            self.clipboard_append(codigo)
            self.update()  # Necesario para que se mantenga en el portapapeles

    def verificar_checkbox_paleta_colores(self):
        if not self.checkbox_paletaco_var.get():
            self.eliminar_todos_los_colores()
        self.actualizar_visibilidad_colores_agregados()

    def actualizar_visibilidad_colores_agregados(self):
        if self.checkbox_paletaco_var.get() and self.colores_agregados:
            self.frame_colores_agregados.grid()
        else:
            self.frame_colores_agregados.grid_remove()

    def obtener_nombre_color(self, hex_color):
        try:
            nombre = webcolors.hex_to_name(hex_color)
            return nombre
        except ValueError:
            return "color sin nombre"

    def abrir_selector_color(self):
        self.agregar_color_visual
        if len(self.colores_agregados) >= self.limite_colores:
            # Puedes mostrar una advertencia o simplemente regresar
            CTk.CTkMessagebox.show_warning(title="Límite alcanzado", message="Solo se pueden agregar hasta 5 colores.")
            return

        color = colorchooser.askcolor()[1]
        if color and color not in self.colores_agregados:
            self.agregar_color_visual(color)
            self.colores_agregados.append(color)
            self.actualizar_visibilidad_colores_agregados()

    def agregar_color_visual(self, hex_color):
        
        self.actualizar_visibilidad_colores_agregados()

        nombre_color = self.obtener_nombre_color(hex_color)

        fila = len(self.colores_agregados)

        frame_color = CTk.CTkFrame(self.frame_colores_agregados, width=20, height=20)
        frame_color.configure(fg_color=hex_color)
        frame_color.grid(row=fila, column=0, padx=5, pady=2)
        frame_color.grid_propagate(False)

        label_codigo = CTk.CTkLabel(self.frame_colores_agregados, text=f"{hex_color} - {nombre_color}")
        label_codigo.grid(row=fila, column=1, padx=5, pady=2)

        boton_eliminar = CTk.CTkButton(self.frame_colores_agregados, text="x", width=5,
                                   command=lambda: self.eliminar_color(hex_color, frame_color, label_codigo, boton_eliminar))
        boton_eliminar.grid(row=fila, column=2, padx=5, pady=2)

    def eliminar_color(self, hex_color, frame, label, boton):
        self.actualizar_visibilidad_colores_agregados()

        frame.destroy()
        label.destroy()
        boton.destroy()
        self.colores_agregados.remove(hex_color)

        self.reordenar_colores()
        self.actualizar_visibilidad_colores_agregados()

    def reordenar_colores(self):
        for i, widget in enumerate(self.frame_colores_agregados.winfo_children()):
            widget.grid(row=i // 3, column=i % 3, padx=5, pady=2)
    
    def eliminar_todos_los_colores(self):
        for widget in self.frame_colores_agregados.winfo_children():
            widget.destroy()
        self.colores_agregados.clear()
        self.actualizar_visibilidad_colores_agregados()
        #Fiesta

    def crear_fiesta(self):
        if self.seleccion_actual != "Fiesta":
         return
        self.crear_labels_fiesta_invitacion_din()
        self.frame_descrip=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_descrip.grid(pady=4, padx=4, row=6, column=0, sticky="nsew")
        self.frame_descrip.columnconfigure(0,weight=1)
        self.frame_descrip.rowconfigure(1,weight=1)
        self.label_descrip=CTk.CTkLabel(self.frame_descrip,text="Descripción", font=("Verdana", 20, "bold"))
        self.label_descrip.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.descripcion=self.entry_descrip=CTk.CTkEntry(self.frame_descrip,placeholder_text="p. ej.Disfraces con temática de Shrek 2", fg_color="white", font=("Verdana", 16))
        self.entry_descrip.grid(row=1, column=0, columnspan=2, pady=5, padx=2, sticky="nsew")

        #Guardar los frames actuales
        self.paquete_actual = [self.frame_descrip,self.frame_din_fiesta]

    def crear_cumple(self):
        if self.seleccion_actual != "Cumpleaños":
         return  
        self.crear_labels_cumple_invitacion_din()      
        self.frame_cumpleanero=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_cumpleanero.grid(pady=4, padx=4, row=6, column=0, sticky="nsew")
        self.frame_cumpleanero.columnconfigure(0,weight=1)
        self.frame_cumpleanero.rowconfigure(0,weight=1)
        self.frame_cumpleanero.rowconfigure(1,weight=1)
        self.label_cumpleanero=CTk.CTkLabel(self.frame_cumpleanero,text="Cumpleañero", font=("Verdana", 20, "bold"))
        self.label_cumpleanero.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.entry_cumpleanero=CTk.CTkEntry(self.frame_cumpleanero,placeholder_text="Nombre del cumpleañero", fg_color="white", font=("Verdana", 16))
        self.entry_cumpleanero.grid(row=1, column=0, columnspan=2, pady=5, padx=2, sticky="nsew")
       
        self.frame_edad=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_edad.grid(pady=4, padx=4, row=7, column=0, sticky="nsew")
        self.frame_edad.columnconfigure(0,weight=1)
        self.frame_edad.columnconfigure(1,weight=1)
        self.frame_edad.columnconfigure(2,weight=1)
        self.frame_edad.columnconfigure(3,weight=1)
        self.frame_edad.rowconfigure(0,weight=1)
        self.frame_edad.rowconfigure(1,weight=1)
        self.label_edad=CTk.CTkLabel(self.frame_edad,text="Edad",width=20, font=("Verdana", 20, "bold"))
        self.label_edad.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.label_num_edad=CTk.CTkLabel(self.frame_edad,text=str(self.valor_edad),width=20, font=("Verdana", 24, "bold"))
        self.label_num_edad.grid(row=1, column=0, pady=5, padx=2, sticky="e")
        self.label_anos=CTk.CTkLabel(self.frame_edad,text="año(s)", font=("Verdana", 24, "bold"))
        self.label_anos.grid(row=1, column=1, pady=5, padx=2, sticky="w")
        self.boton_mas_edad=CTk.CTkButton(self.frame_edad,text="+",width=5, font=("Verdana", 20, "bold"),command=self.aumentar_edad)
        self.boton_mas_edad.grid(row=1, column=2, pady=5, padx=2, sticky="nsew")
        self.boton_menos_edad=CTk.CTkButton(self.frame_edad,text="-",width=5, font=("Verdana", 20, "bold"),command=self.disminuir_edad)
        self.boton_menos_edad.grid(row=1, column=3, pady=5, padx=2, sticky="nsew")

        self.frame_cortesia=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_cortesia.grid(pady=4, padx=4, row=8, column=0, sticky="nsew")
        self.frame_cortesia.columnconfigure(0,weight=1)
        self.frame_cortesia.rowconfigure(0,weight=1)
        self.frame_cortesia.rowconfigure(1,weight=1)
        self.label_cortesia=CTk.CTkLabel(self.frame_cortesia,text="Cortesia",width=20, font=("Verdana", 20, "bold"))
        self.label_cortesia.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.checkbox_mesa_var = tk.IntVar()
        self.checkbox_mesa = CTk.CTkCheckBox(self.frame_cortesia, fg_color="white", text="Mesa de regalos", font=("Verdana", 16),variable=self.checkbox_mesa_var, command=lambda: self.toggle_widgets_by_checkbox(
        self.checkbox_mesa_var,
        [self.entry_mesa]
        ))
        self.checkbox_mesa.grid(row=1, column=0, pady=5, padx=2, sticky="nsew")
        self.entry_mesa=CTk.CTkEntry(self.frame_cortesia,placeholder_text="p. ej.Lluvia de sobres", fg_color="white", font=("Verdana", 16))
        self.entry_mesa.grid(row=2, column=0, columnspan=2, pady=5, padx=2, sticky="nsew")
        self.entry_mesa.grid_remove()

        #Guardar los frames actuales
        self.paquete_actual = [self.frame_cumpleanero,self.frame_edad,self.frame_cortesia,self.frame_din_cumple]

    def crear_grad(self):
        if self.seleccion_actual != "Graduación":
         return
        self.crear_labels_grad_invitacion_din()
        self.frame_instituto=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_instituto.grid(pady=4, padx=4, row=6, column=0, sticky="nsew")
        self.frame_instituto.columnconfigure(0,weight=1)
        self.frame_instituto.rowconfigure(1,weight=1)
        self.frame_instituto.rowconfigure(1,weight=1)
        self.label_instituto=CTk.CTkLabel(self.frame_instituto,text="Instituto", font=("Verdana", 20, "bold"))
        self.label_instituto.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.entry_instituto=CTk.CTkEntry(self.frame_instituto,placeholder_text="Nombre del instituto",placeholder_text_color="dark gray", fg_color="white", font=("Verdana", 16))
        self.entry_instituto.grid(row=1, column=0, columnspan=2, pady=5, padx=2, sticky="nsew")

        self.frame_nivel_edu=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_nivel_edu.grid(pady=4, padx=4, row=7, column=0, sticky="nsew")
        self.frame_nivel_edu.columnconfigure(0,weight=1)
        self.frame_nivel_edu.rowconfigure(0,weight=1)
        self.frame_nivel_edu.rowconfigure(1,weight=1)
        self.label_nivel_edu=CTk.CTkLabel(self.frame_nivel_edu,text="Nivel educativo", font=("Verdana", 20, "bold"))
        self.label_nivel_edu.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.combobox_nivel_edu=CTk.CTkComboBox(self.frame_nivel_edu, fg_color="white",state="readonly",text_color="dark gray", font=("Verdana", 16),values=("Inicial/Preescolar","Básica","Media superior","Superior","Continua"))
        self.combobox_nivel_edu.grid(row=1, column=0, columnspan=2, pady=5, padx=2, sticky="nsew")
        self.combobox_nivel_edu.set("Elija un nivel educativo")

        self.frame_generacion=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_generacion.grid(pady=4, padx=4, row=8, column=0, sticky="nsew")
        self.frame_generacion.columnconfigure(0,weight=1)
        self.frame_generacion.columnconfigure(1,weight=1)
        self.frame_generacion.columnconfigure(2,weight=1)
        self.frame_generacion.columnconfigure(3,weight=1)
        self.frame_generacion.rowconfigure(0,weight=1)
        self.frame_generacion.rowconfigure(1,weight=1)
        self.label_generacion=CTk.CTkLabel(self.frame_generacion,text="Generacion por graduarse", font=("Verdana", 20, "bold"))
        self.label_generacion.grid(row=0, column=0,columnspan=4, pady=5, padx=2, sticky="w")
        self.entry_generacion=CTk.CTkLabel(self.frame_generacion,text=str(self.valor_generacion), font=("Verdana", 24, "bold"))
        self.entry_generacion.grid(row=1, column=0, columnspan=2, pady=5, padx=2, sticky="nsew")
        self.boton_mas_gene=CTk.CTkButton(self.frame_generacion,text="+",width=5, font=("Verdana", 20, "bold"),command=self.aumentar_generacion)
        self.boton_mas_gene.grid(row=1, column=2, pady=5, padx=2, sticky="nsew")
        self.boton_menos_gene=CTk.CTkButton(self.frame_generacion,text="-",width=5, font=("Verdana", 20, "bold"),command=self.disminuir_generacion)
        self.boton_menos_gene.grid(row=1, column=3, pady=5, padx=2, sticky="nsew")

        self.frame_inv_x_grad=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_inv_x_grad.grid(pady=4, padx=4, row=9, column=0, sticky="nsew")
        self.frame_inv_x_grad.columnconfigure(0,weight=1)
        self.frame_inv_x_grad.columnconfigure(1,weight=1)
        self.frame_inv_x_grad.columnconfigure(2,weight=1)
        self.frame_inv_x_grad.columnconfigure(3,weight=1)
        self.frame_inv_x_grad.rowconfigure(0,weight=1)
        self.frame_inv_x_grad.rowconfigure(1,weight=1)
        self.label_inv_x_grad=CTk.CTkLabel(self.frame_inv_x_grad,text="Invitados permitidos por graduado", font=("Verdana", 20, "bold"))
        self.label_inv_x_grad.grid(row=0, column=0,columnspan=4, pady=5, padx=2, sticky="w")
        self.label_num_inv_x_grad=CTk.CTkLabel(self.frame_inv_x_grad,text=str(self.valor_inv_grad), font=("Arial", 24, "bold"))
        self.label_num_inv_x_grad.grid(row=1, column=0,columnspan=2, pady=5, padx=2, sticky="nsew")
        self.boton_mas_inv=CTk.CTkButton(self.frame_inv_x_grad,text="+",width=5, font=("Verdana", 20, "bold"),command=self.aumentar_inv_grad)
        self.boton_mas_inv.grid(row=1, column=2, pady=5, padx=2, sticky="nsew")
        self.boton_menos_inv_x_grad=CTk.CTkButton(self.frame_inv_x_grad,text="-",width=5, font=("Verdana", 20, "bold"),command=self.disminuir_inv_grad)
        self.boton_menos_inv_x_grad.grid(row=1, column=3, pady=5, padx=2, sticky="nsew")

        #Guardar los frames actuales
        self.paquete_actual = [self.frame_instituto,self.frame_nivel_edu,self.frame_generacion,self.frame_inv_x_grad,self.frame_din_grad]

    def crear_xv(self):
        if self.seleccion_actual != "XV Años":
         return
        self.crear_labels_xv_invitacion_din()
        self.frame_quinceanero=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_quinceanero.grid(pady=4, padx=4, row=6, column=0, sticky="nsew")
        self.frame_quinceanero.columnconfigure(0,weight=1)
        self.frame_quinceanero.rowconfigure(0,weight=1)
        self.frame_quinceanero.rowconfigure(1,weight=1)
        self.label_quinceanero=CTk.CTkLabel(self.frame_quinceanero,text="Quinceañero", font=("Verdana", 20, "bold"))
        self.label_quinceanero.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.entry_quinceanero=CTk.CTkEntry(self.frame_quinceanero,placeholder_text="Nombre completo del quinceañero", fg_color="white", font=("Verdana", 16))
        self.entry_quinceanero.grid(row=1, column=0, pady=5, padx=2, sticky="nsew")

        self.frame_xv_padres=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_xv_padres.grid(pady=4, padx=4, row=7, column=0, sticky="nsew")
        self.frame_xv_padres.columnconfigure(0,weight=1)
        self.frame_xv_padres.rowconfigure(0,weight=1)
        self.label_xv_padres=CTk.CTkLabel(self.frame_xv_padres,text="Padres", font=("Verdana", 20, "bold"))
        self.label_xv_padres.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.entry_xv_padre1=CTk.CTkEntry(self.frame_xv_padres,placeholder_text="Nombre del padre", fg_color="white", font=("Verdana", 16))
        self.entry_xv_padre1.grid(row=1, column=0, pady=5, padx=2, sticky="nsew")
        self.entry_xv_padre2=CTk.CTkEntry(self.frame_xv_padres,placeholder_text="Nombre de la madre", fg_color="white", font=("Verdana", 16))
        self.entry_xv_padre2.grid(row=2, column=0, pady=5, padx=2, sticky="nsew")

        self.frame_xv_padrinos=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_xv_padrinos.grid(pady=4, padx=4, row=8, column=0, sticky="nsew")
        self.frame_xv_padrinos.columnconfigure(0,weight=1)
        self.frame_xv_padrinos.rowconfigure(0,weight=1)
        self.label_xv_padrinos=CTk.CTkLabel(self.frame_xv_padrinos,text="Padrinos", font=("Verdana", 20, "bold"))
        self.label_xv_padrinos.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.entry_xv_padrino1=CTk.CTkEntry(self.frame_xv_padrinos,placeholder_text="Nombre del padrino", fg_color="white", font=("Verdana", 16))
        self.entry_xv_padrino1.grid(row=1, column=0, pady=5, padx=2, sticky="nsew")
        self.entry_xv_padrino2=CTk.CTkEntry(self.frame_xv_padrinos,placeholder_text="Nombre de la madrina", fg_color="white", font=("Verdana", 16))
        self.entry_xv_padrino2.grid(row=2, column=0, pady=5, padx=2, sticky="nsew")

        self.frame_xv_cortesia=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_xv_cortesia.grid(pady=4, padx=4, row=9, column=0, sticky="nsew")
        self.frame_xv_cortesia.columnconfigure(0,weight=1)
        self.frame_xv_cortesia.rowconfigure(0,weight=1)
        self.label_xv_cortesia=CTk.CTkLabel(self.frame_xv_cortesia,text="Cortesia", font=("Verdana", 20, "bold"))
        self.label_xv_cortesia.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.checkbox_xv_mesa_var = tk.IntVar()
        self.checkbox_xv_mesa = CTk.CTkCheckBox(self.frame_xv_cortesia, fg_color="white", text="Mesa de regalos", font=("Verdana", 16),variable=self.checkbox_xv_mesa_var, command=lambda: self.toggle_widgets_by_checkbox(
        self.checkbox_xv_mesa_var,
        [self.entry_xv_mesa]
        ))
        self.checkbox_xv_mesa.grid(row=1, column=0, pady=5, padx=2, sticky="nsew")
        self.entry_xv_mesa=CTk.CTkEntry(self.frame_xv_cortesia,placeholder_text="p. ej.Liverpool a nombre de ...", font=("Verdana", 16), fg_color="white")
        self.entry_xv_mesa.grid(row=2, column=0, columnspan=2, pady=5, padx=2, sticky="nsew")
        self.entry_xv_mesa.grid_remove()
 
        self.frame_xv_misa=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_xv_misa.grid(pady=4, padx=4, row=10, column=0, sticky="nsew")
        self.label_xv_misa=CTk.CTkLabel(self.frame_xv_misa,text="Servicio religioso", font=("Verdana", 20, "bold"))
        self.label_xv_misa.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.frame_xv_misa.columnconfigure(0,weight=1)
        self.frame_xv_misa.rowconfigure(0,weight=1)
        self.frame_xv_misa.rowconfigure(1,weight=1)
        self.frame_xv_misa.rowconfigure(2,weight=1)
        self.checkbox_xv_misa_var = tk.IntVar()
        self.checkbox_xv_misa = CTk.CTkCheckBox(self.frame_xv_misa, fg_color="white", text="Incluye misa previa a la celebración", font=("Verdana", 16),variable=self.checkbox_xv_misa_var, command=lambda: self.toggle_widgets_by_checkbox(
        self.checkbox_xv_misa_var,
        [self.entry_xv_misa]
        ))
        self.checkbox_xv_misa.grid(row=1, column=0, pady=5, padx=2, sticky="nsew")
        self.entry_xv_misa=CTk.CTkEntry(self.frame_xv_misa,placeholder_text="Iglesia de Santa Rita", fg_color="white", font=("Verdana", 16))
        self.entry_xv_misa.grid(row=2, column=0, columnspan=2, pady=5, padx=2, sticky="nsew")
        self.entry_xv_misa.grid_remove()

        #Guardar los frames actuales
        self.paquete_actual = [self.frame_quinceanero,self.frame_xv_padres,self.frame_xv_padrinos,self.frame_xv_cortesia,self.frame_xv_misa,self.frame_din_xv]

    def crear_boda(self):
        if self.seleccion_actual != "Boda":
         return
        self.crear_labels_boda_invitacion_din()
        self.frame_novios=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_novios.grid(pady=4, padx=4, row=6, column=0, sticky="nsew")
        self.frame_novios.columnconfigure(0,weight=1)
        self.frame_novios.rowconfigure(0,weight=1)
        self.frame_novios.rowconfigure(1,weight=1)
        self.frame_novios.rowconfigure(2,weight=1)
        self.label_novios=CTk.CTkLabel(self.frame_novios,text="Novios", font=("Verdana", 20, "bold"))
        self.label_novios.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.entry_novio1=CTk.CTkEntry(self.frame_novios,placeholder_text="Nombre del novio", fg_color="white", font=("Verdana", 16))
        self.entry_novio1.grid(row=1, column=0, pady=5, padx=2, sticky="nsew")
        self.entry_novio2=CTk.CTkEntry(self.frame_novios,placeholder_text="Nombre de la novia", fg_color="white", font=("Verdana", 16))
        self.entry_novio2.grid(row=2, column=0, pady=5, padx=2, sticky="nsew")

        self.frame_boda_padrinos=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_boda_padrinos.grid(pady=4, padx=4, row=7, column=0, sticky="nsew")
        self.frame_boda_padrinos.columnconfigure(0,weight=1)
        self.frame_boda_padrinos.rowconfigure(0,weight=1)
        self.frame_boda_padrinos.rowconfigure(1,weight=1)
        self.label_boda_padrinos=CTk.CTkLabel(self.frame_boda_padrinos,text="Padrinos", font=("Verdana", 20, "bold"))
        self.label_boda_padrinos.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.entry_boda_padrino1=CTk.CTkEntry(self.frame_boda_padrinos,placeholder_text="Nombre del padrino", fg_color="white", font=("Verdana", 16))
        self.entry_boda_padrino1.grid(row=1, column=0, pady=5, padx=2, sticky="nsew")
        self.entry_boda_padrino2=CTk.CTkEntry(self.frame_boda_padrinos,placeholder_text="Nombre de la madrina", fg_color="white", font=("Verdana", 16))
        self.entry_boda_padrino2.grid(row=2, column=0, pady=5, padx=2, sticky="nsew")

        self.frame_boda_cortesia=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_boda_cortesia.grid(pady=4, padx=4, row=8, column=0, sticky="nsew")
        self.frame_boda_cortesia.columnconfigure(0,weight=1)
        self.frame_boda_cortesia.rowconfigure(0,weight=1)
        self.frame_boda_cortesia.rowconfigure(1,weight=1)
        self.frame_boda_cortesia.rowconfigure(2,weight=1)
        self.label_boda_cortesia=CTk.CTkLabel(self.frame_boda_cortesia,text="Cortesia", font=("Verdana", 20, "bold"))
        self.label_boda_cortesia.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.checkbox_boda_mesa_var = tk.IntVar()
        self.checkbox_boda_mesa = CTk.CTkCheckBox(self.frame_boda_cortesia, fg_color="white", text="Mesa de regalos", font=("Verdana", 16),variable=self.checkbox_boda_mesa_var, command=lambda: self.toggle_widgets_by_checkbox(
        self.checkbox_boda_mesa_var,
        [self.entry_boda_mesa]
        ))
        self.checkbox_boda_mesa.grid(row=1, column=0, pady=5, padx=2, sticky="nsew")
        self.entry_boda_mesa=CTk.CTkEntry(self.frame_boda_cortesia,placeholder_text="p. ej.Palacio de Hierro a nombre de...", fg_color="white", font=("Verdana", 16))
        self.entry_boda_mesa.grid(row=2, column=0, columnspan=2, pady=5, padx=2, sticky="nsew")
        self.entry_boda_mesa.grid_remove()

        self.frame_boda_misa=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_boda_misa.grid(pady=4, padx=4, row=9, column=0, sticky="nsew")
        self.label_boda_misa=CTk.CTkLabel(self.frame_boda_misa,text="Servicio religioso", font=("Verdana", 20, "bold"))
        self.label_boda_misa.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.frame_boda_misa.columnconfigure(0,weight=1)
        self.frame_boda_misa.rowconfigure(0,weight=1)
        self.frame_boda_misa.rowconfigure(1,weight=1)
        self.frame_boda_misa.rowconfigure(2,weight=1)
        self.checkbox_boda_misa_var = tk.IntVar()
        self.checkbox_boda_misa = CTk.CTkCheckBox(self.frame_boda_misa, fg_color="white", font=("Verdana", 16), text="Incluye misa previa a la celebración",variable=self.checkbox_boda_misa_var, command=lambda: self.toggle_widgets_by_checkbox(
        self.checkbox_boda_misa_var,
        [self.entry_boda_misa]
        ))
        self.checkbox_boda_misa.grid(row=1, column=0, pady=5, padx=2, sticky="nsew")
        self.entry_boda_misa=CTk.CTkEntry(self.frame_boda_misa,placeholder_text="Iglesia de San Juan", fg_color="white", font=("Verdana", 16))
        self.entry_boda_misa.grid(row=2, column=0, columnspan=2, pady=5, padx=2, sticky="nsew")
        self.entry_boda_misa.grid_remove()

        self.frame_boda_menores=CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_boda_menores.grid(pady=4, padx=4, row=10, column=0, sticky="nsew")
        self.label_boda_menores=CTk.CTkLabel(self.frame_boda_menores,text="Menores", font=("Verdana", 20, "bold"))
        self.label_boda_menores.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.frame_boda_menores.columnconfigure(0,weight=1)
        self.frame_boda_menores.rowconfigure(0,weight=1)
        self.frame_boda_menores.rowconfigure(1,weight=1)
        self.frame_boda_menores.rowconfigure(2,weight=1)
        self.checkbox_boda_menores_var = tk.IntVar()
        self.checkbox_boda_menores = CTk.CTkCheckBox(self.frame_boda_menores, fg_color="white", text="No se permiten niños", font=("Verdana", 16),variable=self.checkbox_boda_menores_var)
        self.checkbox_boda_menores.grid(row=1, column=0, pady=5, padx=2, sticky="nsew")

        #Guardar los frames actuales
        self.paquete_actual = [self.frame_novios,self.frame_boda_padrinos,self.frame_boda_cortesia,self.frame_boda_misa,self.frame_boda_menores,self.frame_din_boda]

    def crear_interfaz(self):
        # Frame principal
        self.frame0 = CTk.CTkFrame(self, fg_color="#303AC9")
        self.frame0.grid(row=0, column=0, sticky="nsew")

        for i in range(3):
            self.frame0.columnconfigure(i, weight=1)
        self.frame0.rowconfigure(0, weight=1)

        self.crear_frame_izquierdo_form()
        self.crear_frame_form()
        self.crear_frame_clasif_form()
        self.crear_frame_lugar_fecha_hora_form()
        self.crear_frame_privacidad_form()
        self.crear_frame_cupo_inv_form()
        self.crear_frame_estilo_form()
        self.crear_frame_portada_form()
        self.crear_frame_derecho_vis()
        self.crear_frame_invitacion_vis()

    #Frame izquierdo contenedor del formulario
    def crear_frame_izquierdo_form(self):
        self.frame_izquierdo_form = CTk.CTkFrame(self.frame0, fg_color="#df0f69")
        self.frame_izquierdo_form.grid(pady=30, padx=38, row=0, column=0, rowspan=2, sticky="nsew")
        self.frame_izquierdo_form.columnconfigure(0, weight=1)
        self.frame_izquierdo_form.rowconfigure(0, weight=24)
        self.frame_izquierdo_form.rowconfigure(1, weight=1)

        self.boton_reg_evento = CTk.CTkButton(self.frame_izquierdo_form, fg_color="#1277fa", text="Registrar evento",font=("Verdana",24,"bold"),command=self.on_registrar_eventos)
        self.boton_reg_evento.grid(pady=8, padx=15, row=1, column=0, sticky="nsew")

    def crear_frame_form(self):
        self.frame_form = CTk.CTkScrollableFrame(self.frame_izquierdo_form, fg_color="#220c56")
        self.frame_form.grid(pady=20, padx=30, row=0, column=0, sticky="nsew")
        self.frame_form.columnconfigure(0, weight=1)
        self.frame_form.rowconfigure(0,weight=1)
        self.frame_form.rowconfigure(1,weight=1)
        self.frame_form.rowconfigure(2,weight=1)
        self.frame_form.rowconfigure(3,weight=1)
        self.frame_form.rowconfigure(4,weight=1)
        self.frame_form.rowconfigure(5,weight=1)
        self.frame_form.rowconfigure(6,weight=1)
        self.frame_form.rowconfigure(7,weight=1)
        self.frame_form.rowconfigure(8,weight=1)
        self.frame_form.rowconfigure(9,weight=1)
        self.frame_form.rowconfigure(10,weight=1)
    
    # Clasificación
    def crear_frame_clasif_form(self):
        self.frame_clasif = CTk.CTkFrame(self.frame_form, fg_color="#6da8f4")
        self.frame_clasif.grid(pady=4, padx=4, row=0, column=0, sticky="nsew")
        self.frame_clasif.columnconfigure(0,weight=1)
        self.frame_clasif.rowconfigure(0,weight=1)
        self.frame_clasif.rowconfigure(1,weight=1)
        self.label_clasif = CTk.CTkLabel(self.frame_clasif, text="Clasificación", font=("Verdana", 20, "bold"))
        self.label_clasif.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.combo_eventos= self.combobox_clasif = CTk.CTkComboBox(self.frame_clasif, fg_color="white",text_color="dark gray", font=("Verdana", 16), values=("Fiesta", "Cumpleaños", "Graduación", "XV Años", "Boda"),command=self.manejar_clasificacion,state="readonly")
        self.combobox_clasif.grid(row=1, column=0, pady=5, padx=2, sticky="nsew")
        self.combobox_clasif.set("Elija un tipo de evento")

    # Lugar, fecha, hora
    def crear_frame_lugar_fecha_hora_form(self):
        self.frame_lugar_fecha_hora = CTk.CTkFrame(self.frame_form, fg_color="#5596ec")
        self.frame_lugar_fecha_hora.grid(pady=4, padx=4, row=1, column=0, sticky="nsew")
        self.frame_lugar_fecha_hora.columnconfigure(0,weight=1)
        self.frame_lugar_fecha_hora.columnconfigure(1,weight=1)
        self.frame_lugar_fecha_hora.rowconfigure(0,weight=1)
        self.frame_lugar_fecha_hora.rowconfigure(1,weight=1)
        self.frame_lugar_fecha_hora.rowconfigure(2,weight=1)     
        self.label_lugar_fecha_hora = CTk.CTkLabel(self.frame_lugar_fecha_hora, text="Lugar, fecha y hora", font=("Verdana", 20, "bold"))
        self.label_lugar_fecha_hora.grid(row=0, column=0, columnspan=2, pady=5, padx=2, sticky="w")
        self.lugar=self.entry_lugar = CTk.CTkEntry(self.frame_lugar_fecha_hora,text_color="dark blue", fg_color="white",placeholder_text="Calle/Col./No./Municipio/Ciudad/Estado",placeholder_text_color="dark gray", font=("Verdana", 16))
        self.entry_lugar.grid(row=1, column=0, columnspan=2, pady=5, padx=2, sticky="nsew")
        
        self.fecha=self.entry_fecha = CTk.CTkEntry(self.frame_lugar_fecha_hora,text_color="dark blue", fg_color="white",placeholder_text="dd/mm/yyyy",placeholder_text_color="dark gray", font=("Verdana", 16))
        self.entry_fecha.grid(row=2, column=0, pady=5, padx=2, sticky="nsew")
        self.hora=self.entry_hora = CTk.CTkEntry(self.frame_lugar_fecha_hora,text_color="dark blue", fg_color="white",placeholder_text="HH:MM",placeholder_text_color="dark gray", font=("Verdana", 16))
        self.entry_hora.grid(row=2, column=1, pady=5, padx=2, sticky="nsew")

        # 💡 Establecer fecha y hora actual
        self.entry_fecha.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entry_hora.insert(0, datetime.now().strftime("%H:%M"))

        # 💡 Validación
        vcmd_fecha = self.register(self.validar_fecha_input)
        vcmd_hora = self.register(self.validar_hora_input)

        self.entry_fecha.configure(validate="key", validatecommand=(vcmd_fecha, "%P"))
        self.entry_hora.configure(validate="key", validatecommand=(vcmd_hora, "%P"))
    
        # 💡 Autoformato de hora
        self.entry_hora.bind("<KeyRelease>", self.formato_auto_hora)
        self.entry_fecha.bind("<KeyRelease>", self.formato_auto_fecha)
    
    # Privacidad
    def crear_frame_privacidad_form(self):
        self.frame_privacidad = CTk.CTkFrame(self.frame_form, fg_color="#64a4f8")
        self.frame_privacidad.grid(pady=4, padx=4, row=2, column=0, sticky="nsew")
        self.frame_privacidad.columnconfigure(0,weight=1)
        self.frame_privacidad.columnconfigure(1,weight=1)
        self.frame_privacidad.columnconfigure(2,weight=1)
        self.frame_privacidad.rowconfigure(0,weight=1)
        self.frame_privacidad.rowconfigure(1,weight=1)
        self.frame_privacidad.rowconfigure(2,weight=1)
        self.label_privacidad = CTk.CTkLabel(self.frame_privacidad, text="Privacidad", font=("Verdana", 20, "bold"))
        self.label_privacidad.grid(row=0,column=0,columnspan=3,pady=5, padx=2, sticky="w")

        self.checkbox_privacidad_var = tk.IntVar()
        self.checkbox_privacidad = CTk.CTkCheckBox(self.frame_privacidad, fg_color="white", text="Evento privado", font=("Verdana", 16),variable=self.checkbox_privacidad_var, command=lambda: self.toggle_widgets_by_checkbox(
        self.checkbox_privacidad_var,
        [self.label_codigo_priv,self.boton_generar_cod,self.boton_copiar_cod]
        ))
        self.checkbox_privacidad.grid(row=1,column=0,columnspan=3,pady=5, padx=2, sticky="nsew")

        self.label_codigo_priv=CTk.CTkLabel(self.frame_privacidad,text="- - - - - - - - - -",width=20, font=("Verdana", 16))
        self.label_codigo_priv.grid(row=2, column=0, pady=5, padx=2, sticky="nsew")
        self.label_codigo_priv.grid_remove()
        self.boton_generar_cod=CTk.CTkButton(self.frame_privacidad,text="Generar código",width=5, font=("Verdana", 16),command=self.generar_y_mostrar_codigo)
        self.boton_generar_cod.grid(row=2, column=1, pady=5, padx=2, sticky="nsew")
        self.boton_generar_cod.grid_remove()
        self.boton_copiar_cod=CTk.CTkButton(self.frame_privacidad,text="Copiar",width=5, font=("Verdana", 16),command=self.copiar_codigo_al_portapapeles)
        self.boton_copiar_cod.grid(row=2, column=2, pady=5, padx=2, sticky="nsew")
        self.boton_copiar_cod.grid_remove()
            
    # Cupo invitados
    def crear_frame_cupo_inv_form(self):
        self.frame_cupo_inv = CTk.CTkFrame(self.frame_form, fg_color="#6ea7f1")
        self.frame_cupo_inv.grid(pady=4, padx=4, row=3, column=0, sticky="nsew")
        self.frame_cupo_inv.columnconfigure(0,weight=1)
        self.frame_cupo_inv.rowconfigure(0,weight=1)
        self.frame_cupo_inv.rowconfigure(1,weight=1)
        self.frame_cupo_inv.rowconfigure(2,weight=1)
        self.label_cupo_inv = CTk.CTkLabel(self.frame_cupo_inv, text="Cupo de invitados", font=("Verdana", 20, "bold"))
        self.label_cupo_inv.grid(row=0, column=0, columnspan=2, pady=5, padx=2, sticky="w")
        self.label_personas = CTk.CTkLabel(self.frame_cupo_inv, text="personas", font=("Verdana", 16))
        self.entry_num_inv = CTk.CTkEntry(self.frame_cupo_inv,text_color="dark gray", fg_color="white", font=("Verdana", 16))
        self.label_personas.grid(row=2, column=1, pady=5, padx=2, sticky="w")
        self.entry_num_inv.grid(row=2, column=0, pady=5, padx=2, sticky="nsew")
        self.label_personas.grid_remove()
        self.entry_num_inv.grid_remove()

        self.cupo=combobox_cupo_inv = CTk.CTkComboBox(
            self.frame_cupo_inv,
            fg_color="white",text_color="dark gray", font=("Verdana", 16),
            values=("Limitado", "Ilimitado"),
            command=lambda e: self.toggle_widgets_by_combobox(
                combobox_cupo_inv,
                {"Limitado": [self.label_personas, self.entry_num_inv], "Ilimitado": []}
            ),state="readonly"
        )
        combobox_cupo_inv.grid(row=1, column=0, columnspan=2, pady=5, padx=2, sticky="nsew")
        combobox_cupo_inv.set("Ilimitado")

    # Estilo
    def crear_frame_estilo_form(self):
        self.frame_estilo = CTk.CTkFrame(self.frame_form, fg_color="#7baff4")
        self.frame_estilo.grid(pady=4, padx=4, row=4, column=0, sticky="nsew")
        self.frame_estilo.columnconfigure(0,weight=1)
        self.frame_estilo.rowconfigure(0,weight=1)
        self.frame_estilo.rowconfigure(1,weight=1)
        self.frame_estilo.rowconfigure(2,weight=1)
        self.frame_estilo.rowconfigure(3,weight=1)
        self.frame_estilo.rowconfigure(4,weight=1)
        self.frame_estilo.rowconfigure(5,weight=1)
        self.label_estilo = CTk.CTkLabel(self.frame_estilo, text="Estilo", font=("Verdana", 20, "bold"))
        self.label_estilo.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.checkbox_estilo_var = tk.IntVar()
        self.checkbox_estilo = CTk.CTkCheckBox(self.frame_estilo, fg_color="white", text="Código de vestimenta", font=("Verdana", 16),variable=self.checkbox_estilo_var, command=lambda: self.toggle_widgets_by_checkbox(
        self.checkbox_estilo_var,
        [self.combobox_estilo]
        ))
        self.checkbox_estilo.grid(row=1, column=0, pady=5, padx=2, sticky="nsew")
        self.combobox_estilo = CTk.CTkComboBox(
            self.frame_estilo,
            fg_color="white",text_color="dark gray", font=("Verdana", 16),
            values=("Casual", "Casual elegante", "Coctel", "Formal", "Etiqueta rigurosa", "Temático")
        ,state="readonly")
        self.combobox_estilo.grid(row=2, column=0, pady=5, padx=2, sticky="nsew")
        self.combobox_estilo.grid_remove()
        self.combobox_estilo.set("Elija un nivel de formalidad")
        self.checkbox_paletaco_var = tk.IntVar()
        self.checkbox_paletaco = CTk.CTkCheckBox(self.frame_estilo, fg_color="white", text="Paleta de colores", font=("Verdana", 16),variable=self.checkbox_paletaco_var,command=lambda : [self.toggle_widgets_by_checkbox(
            self.checkbox_paletaco_var, [self.boton_ag_color]
        ),self.verificar_checkbox_paleta_colores()])
        self.checkbox_paletaco.grid(row=3, column=0, pady=5, padx=2, sticky="nsew")
        self.frame_colores_agregados = CTk.CTkFrame(self.frame_estilo, fg_color="#5e73ea")
        self.frame_colores_agregados.grid(row=4, column=0, pady=5, padx=6, sticky="nsew")
        self.frame_colores_agregados.grid_remove()
        self.boton_ag_color = CTk.CTkButton(self.frame_estilo, fg_color="white", text="+ Agregar color", font=("Verdana", 16),command=self.abrir_selector_color)
        self.boton_ag_color.grid(row=5, column=0, pady=5, padx=6, sticky="nsew")
        self.boton_ag_color.grid_remove()

    #Portada
    def crear_frame_portada_form(self):
        self.frame_portada = CTk.CTkFrame(self.frame_form, fg_color="#7baff4")
        self.frame_portada.grid(pady=4, padx=4, row=5, column=0, sticky="nsew")
        self.frame_portada.columnconfigure(0,weight=1)
        self.frame_portada.rowconfigure(0,weight=1)
        self.frame_portada.rowconfigure(0,weight=1)
        self.label_portada = CTk.CTkLabel(self.frame_portada, text="Portada", font=("Verdana", 20, "bold"))
        self.label_portada.grid(row=0, column=0, pady=5, padx=2, sticky="w")
        self.checkbox_portada_var = tk.IntVar()
        self.checkbox_portada = CTk.CTkCheckBox(self.frame_portada, fg_color="white", text="Insertar imagen desde mi dispositivo", font=("Verdana", 16),variable=self.checkbox_portada_var, command=lambda: self.toggle_widgets_by_checkbox(
        self.checkbox_portada_var,
        [self.boton_elegir_imagen]
        ))
        self.checkbox_portada.grid(row=1, column=0, pady=5, padx=2, sticky="nsew")

        self.boton_elegir_imagen = CTk.CTkButton(self.frame_portada, text="Elegir imagen", font=("Verdana", 16), command=self.seleccionar_imagen)
        self.boton_elegir_imagen.grid(row=2, column=0, pady=5, padx=5)
        
        # Label para mostrar la imagen
        self.label_imagen = CTk.CTkLabel(self.frame_portada, text="")
        self.label_imagen.grid(row=2, column=0, pady=5, padx=5)

        self.boton_elegir_imagen.grid_remove()
        self.label_imagen.grid_remove()

    # Vista de la invitación (parte derecha)
    def crear_frame_derecho_vis(self):
        self.frame2 = CTk.CTkFrame(self.frame0, fg_color="#1503b8")
        self.frame2.grid(pady=40, padx=30, row=0, column=1, columnspan=2, sticky="nsew")
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=2)
        self.frame2.rowconfigure(0, weight=8)
        self.frame2.rowconfigure(1, weight=1)
    
    def crear_frame_invitacion_vis(self):
        self.frame3 = CTk.CTkFrame(self.frame2, fg_color="#fae9d0")
        self.frame3.grid(pady=25, padx=20, row=0, column=0, columnspan=2, sticky="nsew")
        self.frame3.rowconfigure(0,weight=1)
        self.frame3.columnconfigure(0,weight=1)

        self.boton_editar = CTk.CTkButton(self.frame2, fg_color="#220c56", text="Editar datos",font=("Verdana",24,"bold"))
        self.boton_editar.grid(pady=10, padx=25, row=1, column=0, sticky="nsew")

        self.boton_guardar_inv=CTk.CTkButton(self.frame2,fg_color="#220c56",text="Guardar invitacion",font=("Verdana",24,"bold"))
        self.boton_guardar_inv.grid(pady=10,padx=25,row=1,column=1,sticky="nsew")

    def crear_frame_con_label(
        self,
        nombre_attr_frame,
        nombre_attr_label,
        parent,
        color,
        pady,
        padx,
        fila,
        columna,
        texto_label,
        fuente_label,
        color_texto="#000000",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="w",
        padx_label=10,
        pady_label=10
    ):
        # Crear y configurar el frame
        frame = CTk.CTkFrame(parent, fg_color=color)
        frame.grid(pady=pady, padx=padx, row=fila, column=columna, sticky=sticky_frame)

        # Hacer que el frame pueda expandirse y alinee bien el contenido
        frame.rowconfigure(row_label, weight=1)
        frame.columnconfigure(column_label, weight=1)
 
        # Guardar referencia al frame
        setattr(self, nombre_attr_frame, frame)

        # Crear el label dentro del frame con estilo y posición
        label = CTk.CTkLabel(frame, text=texto_label, font=fuente_label, text_color=color_texto)
        label.grid(row=row_label, column=column_label, sticky=sticky_label, padx=padx_label, pady=pady_label)

        # Guardar referencia al label
        setattr(self, nombre_attr_label, label)
    
    def crear_frame_con_labels(
        self,
        nombre_attr_frame,
        parent,
        color,
        pady,
        padx,
        fila,
        columna,
        sticky_frame="nsew",
        lista_labels=[]
    ):
    # Crear y posicionar el frame
        frame = CTk.CTkFrame(parent, fg_color=color)
        frame.grid(pady=pady, padx=padx, row=fila, column=columna, sticky=sticky_frame)
        setattr(self, nombre_attr_frame, frame)

    # Crear cada label en el frame
        for label_info in lista_labels:
            nombre = label_info.get("nombre", "")
            texto = label_info.get("texto", "")
            fuente = label_info.get("fuente", ("Arial", 12))
            color_texto = label_info.get("color_texto", "#000000")
            row = label_info.get("row", 0)
            column = label_info.get("column", 0)
            sticky = label_info.get("sticky", "w")
            padx_label = label_info.get("padx", 5)
            pady_label = label_info.get("pady", 5)

        # Configurar expansión del frame
            frame.rowconfigure(row, weight=1)
            frame.columnconfigure(column, weight=1)

        # Crear y posicionar el label
            label = CTk.CTkLabel(frame, text=texto, font=fuente, text_color=color_texto)
            label.grid(row=row, column=column, sticky=sticky, padx=padx_label, pady=pady_label)

        # Guardar la referencia al label como atributo si tiene nombre
            if nombre:
                setattr(self, nombre, label)

    def crear_frame_con_circulos_y_labels(
        self,
        nombre_attr_frame,
        parent,
        color_fondo,
        pady,
        padx,
        fila,
        columna,
        sticky_frame="nsew",
        textos_labels=[],
        colores_circulos=[],
        fuente_label=("Arial", 12),
        color_texto_label="#000000",
        tamaño_circulo=40
    ):
    # Crear el frame contenedor
        frame = CTk.CTkFrame(parent, fg_color=color_fondo)
        frame.grid(pady=pady, padx=padx, row=fila, column=columna, sticky=sticky_frame)
        setattr(self, nombre_attr_frame, frame)

    # Configurar filas del frame
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)

    # Asegurar que haya 5 elementos
        while len(textos_labels) < 5:
            textos_labels.append("")
        while len(colores_circulos) < 5:
            colores_circulos.append("#cccccc")

        for i in range(5):
            frame.columnconfigure(i, weight=1)  # <- columna expandible

        # Círculo
            circle = CTk.CTkLabel(
                frame,
                text="", 
                width=tamaño_circulo, 
                height=tamaño_circulo,
                fg_color=colores_circulos[i],
                corner_radius=tamaño_circulo // 2
            )
            circle.grid(row=0, column=i, padx=10, pady=5, sticky="n")

        # Label debajo
            label = CTk.CTkLabel(
                frame,
                text=textos_labels[i],
                font=fuente_label,
                text_color=color_texto_label
            )
            label.grid(row=1, column=i, padx=10, pady=5, sticky="n")


    def crear_labels_evento_invitacion_din(self):
        self.frame_din_clasif_evento=CTk.CTkFrame(self.frame3,fg_color="#faf7ed")
        self.frame_din_clasif_evento.grid(pady=8,padx=8,row=0,column=0,sticky="nsew")
        
        for i in range(3):
            self.frame_din.columnconfigure(i, weight=1)
        for j in range(8):
            self.frame_din.rowconfigure(j, weight=1)

    def crear_labels_fiesta_invitacion_din(self):
        self.frame_din_fiesta=CTk.CTkFrame(self.frame3,fg_color="#faf7ed")
        self.frame_din_fiesta.grid(pady=8,padx=8,row=0,column=0,sticky="nsew")
        
        for i in range(3):
            self.frame_din_fiesta.columnconfigure(i, weight=1)
        for j in range(7):
            self.frame_din_fiesta.rowconfigure(j, weight=1)
        
        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_evento",
        nombre_attr_label="label_info_evento",
        parent=self.frame_din_fiesta,  
        color="white",
        pady=8,
        padx=10,
        fila=0,
        columna=1,
        texto_label="Fiesta",
        fuente_label=("Verdana", 24, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_descrip",
        nombre_attr_label="label_info_descrip",
        parent=self.frame_din_fiesta,  
        color="white",
        pady=8,
        padx=10,
        fila=1,
        columna=1,
        texto_label="Descripción",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_lugar",
        nombre_attr_label="label_info_lugar",
        parent=self.frame_din_fiesta,  
        color="white",
        pady=8,
        padx=10,
        fila=2,
        columna=1,
        texto_label="Lugar",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_hora",
        nombre_attr_label="label_info_hora",
        parent=self.frame_din_fiesta,  
        color="white",
        pady=8,
        padx=10,
        fila=3,
        columna=1,
        texto_label="Fecha y Hora",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )
        
        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_codigo",
        nombre_attr_label="label_info_codigo",
        parent=self.frame_din_fiesta,  
        color="white",
        pady=8,
        padx=10,
        fila=4,
        columna=1,
        texto_label="Codigo",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_estilo",
        nombre_attr_label="label_info_estilo",
        parent=self.frame_din_fiesta,  
        color="white",
        pady=8,
        padx=10,
        fila=5,
        columna=1,
        texto_label="Estilo",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )
 
        self.crear_frame_con_circulos_y_labels(
        nombre_attr_frame="frame_colores",
        parent=self.frame_din_fiesta,
        color_fondo="#f0f0f0",
        pady=10,
        padx=10,
        fila=6,
        columna=1,
        textos_labels=["Verde", "Azul", "Amarillo", "Rosa", "Rojo"],
        colores_circulos=["#4caf50", "#2196f3", "#ffeb3b", "#fd5db0", "#f44336"],
        fuente_label=("Verdana", 12),
        color_texto_label="#333333",
        tamaño_circulo=50
        )

    def crear_labels_cumple_invitacion_din(self):
        self.frame_din_cumple=CTk.CTkFrame(self.frame3,fg_color="#faf7ed")
        self.frame_din_cumple.grid(pady=8,padx=8,row=0,column=0,sticky="nsew")
        
        for i in range(3):
            self.frame_din_cumple.columnconfigure(i, weight=1)
        for j in range(8):
            self.frame_din_cumple.rowconfigure(j, weight=1)

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_cumpleanero",
        nombre_attr_label="label_info_cumpleanero",
        parent=self.frame_din_cumple,  
        color="white",
        pady=8,
        padx=10,
        fila=0,
        columna=1,
        texto_label="Cumpleanero cumple",
        fuente_label=("Verdana", 24, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_edad",
        nombre_attr_label="label_info_edad",
        parent=self.frame_din_cumple,  
        color="white",
        pady=8,
        padx=10,
        fila=1,
        columna=1,
        texto_label="edad",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_lugar",
        nombre_attr_label="label_info_lugar",
        parent=self.frame_din_cumple,  
        color="white",
        pady=8,
        padx=10,
        fila=2,
        columna=1,
        texto_label="Lugar cumple",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_fecha_y_hora",
        nombre_attr_label="label_info_fecha_y_hora",
        parent=self.frame_din_cumple,  
        color="white",
        pady=8,
        padx=10,
        fila=3,
        columna=1,
        texto_label="Fecha y Hora cumple",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )
        
        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_mesa",
        nombre_attr_label="label_info_mesa",
        parent=self.frame_din_cumple,  
        color="white",
        pady=8,
        padx=10,
        fila=4,
        columna=1,
        texto_label="Mesa de regalos:billullos",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_codigo",
        nombre_attr_label="label_info_codigo",
        parent=self.frame_din_cumple,  
        color="white",
        pady=8,
        padx=10,
        fila=5,
        columna=1,
        texto_label="Codigo cumple",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_estilo",
        nombre_attr_label="label_info_estilo",
        parent=self.frame_din_cumple,  
        color="white",
        pady=8,
        padx=10,
        fila=6,
        columna=1,
        texto_label="Estilo cumple",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )
 
        self.crear_frame_con_circulos_y_labels(
        nombre_attr_frame="frame_colores",
        parent=self.frame_din_cumple,
        color_fondo="#f0f0f0",
        pady=10,
        padx=10,
        fila=7,
        columna=1,
        textos_labels=["Verde", "Azul", "Amarillo", "Rosa", "Rojo"],
        colores_circulos=["#4caf50", "#2196f3", "#ffeb3b", "#fd5db0", "#f44336"],
        fuente_label=("Verdana", 12),
        color_texto_label="#333333",
        tamaño_circulo=50
        )

    def crear_labels_grad_invitacion_din(self):
        self.frame_din_grad=CTk.CTkFrame(self.frame3,fg_color="#faf7ed")
        self.frame_din_grad.grid(pady=8,padx=8,row=0,column=0,sticky="nsew")
        
        for i in range(3):
            self.frame_din_grad.columnconfigure(i, weight=1)
        for j in range(10):
            self.frame_din_grad.rowconfigure(j, weight=1)

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_evento",
        nombre_attr_label="label_info_evento",
        parent=self.frame_din_grad,  
        color="white",
        pady=8,
        padx=10,
        fila=0,
        columna=1,
        texto_label="Graduación",
        fuente_label=("Verdana", 24, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_gene",
        nombre_attr_label="label_info_gene",
        parent=self.frame_din_grad,  
        color="white",
        pady=8,
        padx=10,
        fila=1,
        columna=1,
        texto_label="Generación 0000",
        fuente_label=("Verdana", 20, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_instituto",
        nombre_attr_label="label_info_instituo",
        parent=self.frame_din_grad,  
        color="white",
        pady=8,
        padx=10,
        fila=2,
        columna=1,
        texto_label="Instituto",
        fuente_label=("Verdana", 20, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_nivel_edu",
        nombre_attr_label="label_info_nivel_edu",
        parent=self.frame_din_grad,  
        color="white",
        pady=8,
        padx=10,
        fila=3,
        columna=1,
        texto_label="Nivel educativo",
        fuente_label=("Verdana", 20, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_lugar",
        nombre_attr_label="label_info_lugar",
        parent=self.frame_din_grad,  
        color="white",
        pady=8,
        padx=10,
        fila=4,
        columna=1,
        texto_label="Lugar grad",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_hora",
        nombre_attr_label="label_info_hora",
        parent=self.frame_din_grad,  
        color="white",
        pady=8,
        padx=10,
        fila=5,
        columna=1,
        texto_label="Fecha y Hora",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )
        
        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_invs",
        nombre_attr_label="label_info_invs",
        parent=self.frame_din_grad,  
        color="white",
        pady=8,
        padx=10,
        fila=6,
        columna=1,
        texto_label="00 invitados por graduado",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_codigo",
        nombre_attr_label="label_info_codigo",
        parent=self.frame_din_grad,  
        color="white",
        pady=8,
        padx=10,
        fila=7,
        columna=1,
        texto_label="Codigo",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_estilo",
        nombre_attr_label="label_info_estilo",
        parent=self.frame_din_grad,  
        color="white",
        pady=8,
        padx=10,
        fila=8,
        columna=1,
        texto_label="Estilo",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )
 
        self.crear_frame_con_circulos_y_labels(
        nombre_attr_frame="frame_colores",
        parent=self.frame_din_grad,
        color_fondo="#f0f0f0",
        pady=10,
        padx=10,
        fila=9,
        columna=1,
        textos_labels=["Verde grad", "Azul", "Amarillo", "Rosa", "Rojo"],
        colores_circulos=["#4caf50", "#2196f3", "#ffeb3b", "#fd5db0", "#f44336"],
        fuente_label=("Verdana", 12),
        color_texto_label="#333333",
        tamaño_circulo=50
        )
    
    def crear_labels_xv_invitacion_din(self):
        self.frame_din_xv=CTk.CTkFrame(self.frame3,fg_color="#faf7ed")
        self.frame_din_xv.grid(pady=8,padx=8,row=0,column=0,sticky="nsew")
        
        for i in range(3):
            self.frame_din_xv.columnconfigure(i, weight=1)
        for j in range(10):
            self.frame_din_xv.rowconfigure(j, weight=1)

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_evento",
        nombre_attr_label="label_info_evento",
        parent=self.frame_din_xv,  
        color="white",
        pady=8,
        padx=10,
        fila=0,
        columna=1,
        texto_label="XV años",
        fuente_label=("Verdana", 24, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_xvanero",
        nombre_attr_label="label_info_xvanero",
        parent=self.frame_din_xv,  
        color="white",
        pady=8,
        padx=10,
        fila=1,
        columna=1,
        texto_label="Quinceanero",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_lugar",
        nombre_attr_label="label_info_lugar",
        parent=self.frame_din_xv,  
        color="white",
        pady=8,
        padx=10,
        fila=2,
        columna=1,
        texto_label="Lugar",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_fecha_hora",
        nombre_attr_label="label_info_fecha_hora",
        parent=self.frame_din_xv,  
        color="white",
        pady=8,
        padx=10,
        fila=3,
        columna=1,
        texto_label="Fecha y Hora",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_mama_papa",
        nombre_attr_label="label_info_mama_papa",
        parent=self.frame_din_xv,  
        color="white",
        pady=8,
        padx=10,
        fila=4,
        columna=1,
        texto_label="Mama y Papa",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_padrinos",
        nombre_attr_label="label_info_padrinos",
        parent=self.frame_din_xv,  
        color="white",
        pady=8,
        padx=10,
        fila=5,
        columna=1,
        texto_label="padrinos PADRINO Y MADRINA",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_mesa_xv",
        nombre_attr_label="label_info_mesa_xv",
        parent=self.frame_din_xv,  
        color="white",
        pady=8,
        padx=10,
        fila=6,
        columna=1,
        texto_label="Mesa de regalos:",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_codigo",
        nombre_attr_label="label_info_codigo",
        parent=self.frame_din_xv,  
        color="white",
        pady=8,
        padx=10,
        fila=7,
        columna=1,
        texto_label="Codigo",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_estilo",
        nombre_attr_label="label_info_estilo",
        parent=self.frame_din_xv,  
        color="white",
        pady=8,
        padx=10,
        fila=8,
        columna=1,
        texto_label="Estilo",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )
 
        self.crear_frame_con_circulos_y_labels(
        nombre_attr_frame="frame_colores",
        parent=self.frame_din_xv,
        color_fondo="#f0f0f0",
        pady=10,
        padx=10,
        fila=9,
        columna=1,
        textos_labels=["Verde", "Azul", "Amarillo", "Rosa", "Rojo"],
        colores_circulos=["#4caf50", "#2196f3", "#ffeb3b", "#fd5db0", "#f44336"],
        fuente_label=("Verdana", 12),
        color_texto_label="#333333",
        tamaño_circulo=50
        )

    def crear_labels_boda_invitacion_din(self):
        self.frame_din_boda=CTk.CTkFrame(self.frame3,fg_color="#faf7ed")
        self.frame_din_boda.grid(pady=8,padx=8,row=0,column=0,sticky="nsew")
        
        for i in range(5):
            self.frame_din_boda.columnconfigure(i, weight=1)
        for j in range(11):
            self.frame_din_boda.rowconfigure(j, weight=1)

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_evento",
        nombre_attr_label="label_info_evento",
        parent=self.frame_din_boda,  
        color="white",
        pady=8,
        padx=10,
        fila=0,
        columna=2,
        texto_label="Nuestra Boda",
        fuente_label=("Verdana", 24, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_novios",
        nombre_attr_label="label_info_novios",
        parent=self.frame_din_boda,  
        color="white",
        pady=8,
        padx=10,
        fila=1,
        columna=2,
        texto_label="Novio y Novia",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_lugar",
        nombre_attr_label="label_info_lugar",
        parent=self.frame_din_boda,  
        color="white",
        pady=8,
        padx=10,
        fila=2,
        columna=2,
        texto_label="Lugar",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_fecha_hora",
        nombre_attr_label="label_info_fecha_hora",
        parent=self.frame_din_boda,  
        color="white",
        pady=8,
        padx=10,
        fila=3,
        columna=2,
        texto_label="Fecha y Hora",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )


        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_padrinos",
        nombre_attr_label="label_info_padrinos",
        parent=self.frame_din_boda,  
        color="white",
        pady=8,
        padx=10,
        fila=4,
        columna=2,
        texto_label="padrinos PADRINO Y MADRINA",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_mesa_boda",
        nombre_attr_label="label_info_mesa_boda",
        parent=self.frame_din_boda,  
        color="white",
        pady=8,
        padx=10,
        fila=5,
        columna=2,
        texto_label="Mesa de regalos:",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_mesa_boda",
        nombre_attr_label="label_info_mesa_boda",
        parent=self.frame_din_boda,  
        color="white",
        pady=8,
        padx=10,
        fila=6,
        columna=2,
        texto_label="Ceremonia religiosa",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_menores",
        nombre_attr_label="label_info_menores",
        parent=self.frame_din_boda,  
        color="white",
        pady=7,
        padx=10,
        fila=6,
        columna=2,
        texto_label="No se permiten menores",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_codigo",
        nombre_attr_label="label_info_codigo",
        parent=self.frame_din_boda,  
        color="white",
        pady=8,
        padx=10,
        fila=8,
        columna=2,
        texto_label="Codigo",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )

        self.crear_frame_con_label(
        nombre_attr_frame="frame_info_estilo",
        nombre_attr_label="label_info_estilo",
        parent=self.frame_din_boda,  
        color="white",
        pady=8,
        padx=10,
        fila=9,
        columna=2,
        texto_label="Estilo",
        fuente_label=("Verdana", 16, "bold"),
        color_texto="dark blue",
        sticky_frame="nsew",
        row_label=0,
        column_label=0,
        sticky_label="nsew",
        padx_label=4,
        pady_label=4
        )
 
        self.crear_frame_con_circulos_y_labels(
        nombre_attr_frame="frame_colores",
        parent=self.frame_din_boda,
        color_fondo="#f0f0f0",
        pady=10,
        padx=10,
        fila=10,
        columna=2,
        textos_labels=["Verde", "Azul", "Amarillo", "Rosa", "Rojo"],
        colores_circulos=["#4caf50", "#2196f3", "#ffeb3b", "#fd5db0", "#f44336"],
        fuente_label=("Verdana", 12),
        color_texto_label="#333333",
        tamaño_circulo=50
        )

    def on_registrar_eventos(self):
        anfitrion_id = cargar_id_usuario_json()
        if anfitrion_id is None:
            print("⚠️ No hay usuario logueado, no se puede registrar el evento.")
            return
        tipo_evento = self.combo_eventos.get()
        fecha = self.fecha.get()
        hora = self.hora.get()
        direccion = self.lugar.get()
        num_invitados = self.cupo.get()
        privacidad_valor = self.checkbox_privacidad_var.get()
        privacidad = True if privacidad_valor == 1 else False

        descripcion = ""
        descripcion = self.descripcion.get() if hasattr(self, "entry_descrip")  else ""

        cumpleañero = ""
        if hasattr(self, "entry_cumpleanero") and self.entry_cumpleanero is not None:
            try:
                cumpleañero = self.entry_cumpleanero.get()
            except Exception as e:
                print(f"⚠️ No se pudo obtener el texto de 'entry_cumpleanero': {e}")

        edad = getattr(self, "valor_edad", None)
        mesa_regalos = self.checkbox_estilo_var.get() if hasattr(self, "checkbox_estilo_var") else 0

        escuela = ""
        nivel_educativo = ""
        generacion = getattr(self, "valor_generacion", None)
        invitados_por_alumno = getattr(self, "valor_inv_grad", None)

        

        if tipo_evento == "Graduación":
            if hasattr(self, "entry_instituto"):
                escuela = self.entry_instituto.get()
            if hasattr(self, "combobox_nivel_edu"):
                try:
                    nivel_educativo = self.combobox_nivel_edu.get()
                except Exception as e:
                    print(f"⚠️ No se pudo obtener nivel educativo: {e}")
                    nivel_educativo = ""

        cumpleañero_xv = self.entry_quinceanero.get() if hasattr(self, "entry_quinceanero") else ""
        padre = self.entry_xv_padre1.get() if hasattr(self, "entry_xv_padre1") else ""
        madre = self.entry_xv_padre2.get() if hasattr(self, "entry_xv_padre2") else ""
        padrino = self.entry_xv_padrino1.get() if hasattr(self, "entry_xv_padrino1") else ""
        madrina = self.entry_xv_padrino2.get() if hasattr(self, "entry_xv_padrino2") else ""
        mesa_regalos_xv = self.checkbox_xv_mesa_var.get() if hasattr(self, "checkbox_xv_mesa_var") else 0

        novia = self.entry_novio2.get() if hasattr(self, "entry_novio2") else ""
        novio = self.entry_novio1.get() if hasattr(self, "entry_novio1") else ""
        padrino_boda = self.entry_boda_padrino1.get() if hasattr(self, "entry_boda_padrino1") else ""
        madrina_boda = self.entry_boda_padrino2.get() if hasattr(self, "entry_boda_padrino2") else ""
        mesa_regalos_boda = getattr(self, "checkbox_boda_mesa_var", tk.IntVar()).get()
        misa_valor = getattr(self, "checkbox_boda_misa_var", tk.IntVar()).get()
        misa = True if misa_valor == 1 else False
        iglesia = self.entry_boda_misa.get() if misa else ""
        menores_permitidos = getattr(self, "menores_permitidos", False)
        print(f"Tipo de evento seleccionado: '{tipo_evento}'")
        imagen_bytes = getattr(self, "imagen", None)
        if imagen_bytes is None:
            print("⚠️ No se ha seleccionado ninguna imagen.")
            return
        
        # Inserciones
        if tipo_evento == "Evento":
            EventosManager.insertar_evento(
                anfitrion_id, imagen_bytes, fecha, hora, direccion, num_invitados, privacidad
            )
        elif tipo_evento == "Fiesta":
            EventosManager.insertar_fiesta(
                anfitrion_id, imagen_bytes, fecha, hora, direccion, num_invitados, privacidad, descripcion
            )
        elif tipo_evento == "Cumpleaños":
            EventosManager.insertar_cumpleaños(
                anfitrion_id, imagen_bytes, fecha, hora, direccion, num_invitados, privacidad, cumpleañero, edad, mesa_regalos
            )
        elif tipo_evento == "Graduación":
            EventosManager.insertar_graduacion(
                anfitrion_id, imagen_bytes, fecha, hora, direccion, num_invitados, privacidad, escuela, nivel_educativo, generacion, invitados_por_alumno
            )
        elif tipo_evento == "XV Años":
            EventosManager.insertar_xv(
                anfitrion_id, imagen_bytes, fecha, hora, direccion, num_invitados, privacidad, cumpleañero_xv, padre, madre, padrino, madrina, mesa_regalos_xv
            )
        elif tipo_evento == "Boda":
            EventosManager.insertar_boda(
                anfitrion_id, imagen_bytes, fecha, hora, direccion, num_invitados, privacidad, novia, novio, padrino_boda, madrina_boda, mesa_regalos_boda, misa, iglesia, menores_permitidos
            )
        else:
            print("⚠️ Tipo de evento no reconocido")

    
    def limpiar_campos_dinamicos(self):
        for widget in self.frame_campos_dinamicos.winfo_children():
            widget.destroy()

    # Limpieza segura de atributos dinámicos
        atributos = [
            "entry_quinceanero", "entry_xv_padre1", "entry_xv_padre2",
            "entry_xv_padrino1", "entry_xv_padrino2", "checkbox_xv_mesa_var",
            "entry_cumpleanero", "valor_edad", "checkbox_estilo_var",
            "entry_instituto", "combobox_nivel_edu", "valor_generacion", "valor_inv_grad",
            "entry_novio1", "entry_novio2", "entry_boda_padrino1", "entry_boda_padrino2",
            "checkbox_boda_mesa_var", "checkbox_boda_misa_var", "entry_boda_misa"
        ]
        for attr in atributos:
            if hasattr(self, attr):
                delattr(self, attr)
"""if __name__ == "__main__":
    app = Ventana()
    app.mainloop()"""