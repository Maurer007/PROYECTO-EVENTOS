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


class EventosManager:
    
    @staticmethod
    def insertar_fiesta(fecha, hora, direccion, num_invitados, privacidad, descripcion):
        session = Session()
        try:
            nuevo_evento = Evento(
                #anfitrion=anfitrion,
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
                #anfitrion=anfitrion,
                tipo_evento="Fiesta",
                fecha=fecha,
                hora=hora,
                direccion=direccion,
                num_invitados=num_invitados,
                privacidad=privacidad,
                descripcion=descripcion
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
    def insertar_cumpleaños(fecha, hora, direccion, num_invitados, privacidad, cumpleañero, edad, mesa_regalos):
        session = Session()
        try:
            nuevo_evento = Evento(
                #anfitrion=anfitrion,
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
                #anfitrion=anfitrion,
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
    def insertar_graduacion(fecha, hora, direccion, num_invitados, privacidad, escuela, nivel_educativo, generacion, invitados_por_alumno):
        session = Session()
        try:
            nuevo_evento = Evento(
                #anfitrion=anfitrion,
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
                #anfitrion=anfitrion,
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
    def insertar_xv(fecha, hora, direccion, num_invitados, privacidad, cumpleañero_xv, padre, madre, padrino, madrina, mesa_regalos_xv):
        session = Session()
        try:
            nuevo_evento = Evento(
                #anfitrion=anfitrion,
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
                #anfitrion=anfitrion,
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
    def insertar_boda(fecha, hora, direccion, num_invitados, privacidad, novia, novio, padrino_boda, madrina_boda, mesa_regalos_boda, misa, iglesia, menores_permitidos):
        session = Session()
        try:
            nuevo_evento = Evento(
                #anfitrion=anfitrion,
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
                #anfitrion=anfitrion,
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
        #self.anfitrion_id = anfitrion_id

        # Configuración inicial del tema
        CTk.set_appearance_mode("System")
        CTk.set_default_color_theme("blue")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
    
        self.crear_interfaz()
        self.colores_agregados = []  # Lista para guardar los colores
        self.limite_colores = 5

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
        self.entry_fecha.bind("<FocusOut>", self.on_fecha_focus_out)

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
        if self.checkbox_portada_var.get():
            ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg *.png *.jpeg *.gif")])
            if ruta:
                print("Ruta seleccionada:", ruta)
            
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
        self.paquete_actual = [self.frame_descrip]

    def crear_cumple(self):
        if self.seleccion_actual != "Cumpleaños":
         return        
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
        self.paquete_actual = [self.frame_cumpleanero,self.frame_edad,self.frame_cortesia]

    def crear_grad(self):
        if self.seleccion_actual != "Graduación":
         return
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
        self.paquete_actual = [self.frame_instituto,self.frame_nivel_edu,self.frame_generacion,self.frame_inv_x_grad]

    def crear_xv(self):
        if self.seleccion_actual != "XV Años":
         return
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
        self.paquete_actual = [self.frame_quinceanero,self.frame_xv_padres,self.frame_xv_padrinos,self.frame_xv_cortesia,self.frame_xv_misa]

    def crear_boda(self):
        if self.seleccion_actual != "Boda":
         return
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
        self.paquete_actual = [self.frame_novios,self.frame_boda_padrinos,self.frame_boda_cortesia,self.frame_boda_misa,self.frame_boda_menores]

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
        self.entry_fecha.bind("<FocusOut>", self.on_fecha_focus_out)

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

    def crear_labels_evento_invitacion_din(self):
        self.label_din_clasif=CTk.CTkLabel(self.frame3,text="Evento...")
        self.label_din_clasif.grid()
        self.label_din_lugar=CTk.CTkLabel(self.frame3,text="Aquí se mostrará la dirección")
        self.label_din_lugar.grid()
        self.label_din_fecha=CTk.CTkLabel(self.frame3,text="Aquí se mostrará la fecha")
        self.label_din_fecha.grid()
        self.label_din_hora=CTk.CTkLabel(self.frame3,text="Aquí se mostrará la hora")
        self.label_din_hora.grid()
        self.label_din_codigo=CTk.CTkLabel(self.frame3,text="Aquí se mostrará el código")
        self.label_din_codigo.grid()
        self.label_din_estilo=CTk.CTkLabel(self.frame3,text="Aquí se mostrará el estilo")
        self.label_din_estilo.grid()
        self.label_din_colores=CTk.CTkLabel(self.frame3,text="Aquí se mostrarán los colores")
        self.label_din_colores.grid()
        self.label_din_descrip=CTk.CTkLabel(self.frame3,text="Aquí se mostrará la descripción")
        self.label_din_descrip.grid()

    def crear_labels_fiesta_invitacion_din(self):
        self.frame_din_clasif_fiesta=CTk.CTkFrame(self.frame3,fg_color="#faf7ed")
        self.frame_din_clasif_fiesta.grid(pady=8,padx=8,row=0,column=0,sticky="nsew")
        self.frame_din_clasif_fiesta.columnconfigure(0,weight=1)
        self.frame_din_clasif_fiesta.columnconfigure(1,weight=1)
        self.frame_din_clasif_fiesta.columnconfigure(2,weight=1)
        self.frame_din_clasif_fiesta.rowconfigure(0,weight=1)
        self.frame_din_clasif_fiesta.rowconfigure(1,weight=1)
        self.frame_din_clasif_fiesta.rowconfigure(2,weight=1)
        self.frame_din_clasif_fiesta.rowconfigure(3,weight=1)
        self.frame_din_clasif_fiesta.rowconfigure(4,weight=1)
        self.frame_din_clasif_fiesta.rowconfigure(5,weight=1)
        self.frame_din_clasif_fiesta.rowconfigure(6,weight=1)
        self.label_din_clasif_fiesta=CTk.CTkLabel(self.frame_din_clasif_fiesta,text="Fiesta",text_color="dark blue")
        self.label_din_clasif_fiesta.grid(pady=4,padx=4,row=0,column=1)
        self.label_din_lugar_fiesta=CTk.CTkLabel(self.frame_din_clasif_fiesta,text="Aquí se mostrará la dirección",text_color="dark blue")
        self.label_din_lugar_fiesta.grid(pady=4,padx=4,row=1,column=1)
        self.label_din_fecha_fiesta=CTk.CTkLabel(self.frame_din_clasif_fiesta,text="Aquí se mostrará la fecha",text_color="dark blue")
        self.label_din_fecha_fiesta.grid(pady=4,padx=4,row=2,column=1,sticky="e")
        self.label_din_hora_fiesta=CTk.CTkLabel(self.frame_din_clasif_fiesta,text="Aquí se mostrará la hora",text_color="dark blue")
        self.label_din_hora_fiesta.grid(pady=4,padx=4,row=2,column=2,sticky="w")
        self.label_din_codigo_fiesta=CTk.CTkLabel(self.frame_din_clasif_fiesta,text="Aquí se mostrará el código",text_color="dark blue")
        self.label_din_codigo_fiesta.grid(pady=4,padx=4,row=3,column=1)
        self.label_din_estilo_fiesta=CTk.CTkLabel(self.frame_din_clasif_fiesta,text="Aquí se mostrará el estilo",text_color="dark blue")
        self.label_din_estilo_fiesta.grid(pady=4,padx=4,row=4,column=1)
        self.label_din_colores_fiesta=CTk.CTkLabel(self.frame_din_clasif_fiesta,text="Aquí se mostrarán los colores",text_color="dark blue")
        self.label_din_colores_fiesta.grid(pady=4,padx=4,row=5,column=1)
        self.label_din_descrip_fiesta=CTk.CTkLabel(self.frame_din_clasif_fiesta,text="Aquí se mostrará la descripción",text_color="dark blue")
        self.label_din_descrip_fiesta.grid(pady=4,padx=4,row=6,column=1)


    def on_registrar_eventos(self):
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

        novia = self.entry_novia.get() if hasattr(self, "entry_novia") else ""
        novio = self.entry_novio.get() if hasattr(self, "entry_novio") else ""
        padrino_boda = self.entry_padrino_boda.get() if hasattr(self, "entry_padrino_boda") else ""
        madrina_boda = self.entry_madrina_boda.get() if hasattr(self, "entry_madrina_boda") else ""
        mesa_regalos_boda = getattr(self, "checkbox_boda_mesa_var", tk.IntVar()).get()
        misa = getattr(self, "misa", "")
        iglesia = getattr(self, "iglesia", "")
        menores_permitidos = getattr(self, "menores_permitidos", False)
        print(f"Tipo de evento seleccionado: '{tipo_evento}'")
        # Inserciones
        if tipo_evento == "Evento":
            EventosManager.insertar_evento(
                fecha, hora, direccion, num_invitados, privacidad
            )
        elif tipo_evento == "Fiesta":
            EventosManager.insertar_fiesta(
                fecha, hora, direccion, num_invitados, privacidad, descripcion
            )
        elif tipo_evento == "Cumpleaños":
            EventosManager.insertar_cumpleaños(
                fecha, hora, direccion, num_invitados, privacidad, cumpleañero, edad, mesa_regalos
            )
        elif tipo_evento == "Graduación":
            EventosManager.insertar_graduacion(
                fecha, hora, direccion, num_invitados, privacidad, escuela, nivel_educativo, generacion, invitados_por_alumno
            )
        elif tipo_evento == "XV Años":
            EventosManager.insertar_xv(
                fecha, hora, direccion, num_invitados, privacidad, cumpleañero_xv, padre, madre, padrino, madrina, mesa_regalos_xv
            )
        elif tipo_evento == "Boda":
            EventosManager.insertar_boda(
                fecha, hora, direccion, num_invitados, privacidad, novia, novio, padrino_boda, madrina_boda, mesa_regalos_boda, misa, iglesia, menores_permitidos
            )
        else:
            print("⚠️ Tipo de evento no reconocido")
"""if __name__ == "__main__":
    app = Ventana()
    app.mainloop()"""