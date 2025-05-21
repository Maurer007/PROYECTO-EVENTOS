import customtkinter as CTk

# Configuración inicial del tema 
CTk.set_appearance_mode("System")  # Puedes cambiar a "Light" o "Dark"
CTk.set_default_color_theme("blue")  # Otros temas: "green", "dark-blue"

# Crear ventana principal
ventana = CTk.CTk()
ventana.title("Invitaciones")
ventana.geometry("900x700+150+150")

frame0=CTk.CTkFrame(ventana,fg_color="#303AC9")
frame0.pack(fill="both",expand=True,pady=10,padx=20)

frame0.columnconfigure(0,weight=1)
frame0.columnconfigure(1,weight=1)
frame0.columnconfigure(2,weight=1)
frame0.columnconfigure(3,weight=1)
frame0.columnconfigure(4,weight=1)
frame0.rowconfigure(0,weight=1)

frame4=CTk.CTkFrame(frame0,fg_color="#1503b8")
frame4.grid(pady=15,padx=8,row=0,column=0,columnspan=2,rowspan=2,sticky="nsew")
frame4.columnconfigure(0,weight=1)
frame4.rowconfigure(0,weight=24)
frame4.rowconfigure(1,weight=1)
#formulario general eventos
frame1=CTk.CTkScrollableFrame(frame4,fg_color="#220c56")
frame1.grid(pady=2,padx=10,row=0,column=0,sticky="nsew")
frame1.columnconfigure(0,weight=1)
frame1.rowconfigure(0,weight=1)

frame_clasif=CTk.CTkFrame(frame1,fg_color="#6da8f4")
frame_clasif.grid(pady=4,padx=4,row=0,column=0,sticky="nsew")
frame_clasif.columnconfigure(0,weight=1)
frame_clasif.rowconfigure(0,weight=1)
frame_clasif.rowconfigure(1,weight=1)
label_clasif=CTk.CTkLabel(frame_clasif,text="Clasificacion",font=("Verdana",14,"bold"))
label_clasif.grid(row=0,column=0,pady=5,padx=2,sticky="w")
combobox_clasif=CTk.CTkComboBox(frame_clasif,fg_color="white",values=("Evento","Fiesta","Cumpleanos","Graduacion","XVs","Boda"))
combobox_clasif.grid(row=1,column=0,pady=5,padx=2,sticky="nsew")
combobox_clasif.set("Evento")

frame_lugar_fecha_hora=CTk.CTkFrame(frame1,fg_color="#5596ec")
frame_lugar_fecha_hora.grid(pady=4,padx=4,row=1,column=0,sticky="nsew")
frame_lugar_fecha_hora.columnconfigure(0,weight=1)
frame_lugar_fecha_hora.columnconfigure(1,weight=1)
frame_lugar_fecha_hora.rowconfigure(0,weight=1)
frame_lugar_fecha_hora.rowconfigure(1,weight=1)
frame_lugar_fecha_hora.rowconfigure(2,weight=1)
label_lugar_fecha_hora=CTk.CTkLabel(frame_lugar_fecha_hora,text="Lugar, fecha y hora",font=("Verdana",14,"bold"))
label_lugar_fecha_hora.grid(row=0,column=0,columnspan=2,pady=5,padx=2,sticky="w")
entry_fecha=CTk.CTkEntry(frame_lugar_fecha_hora,fg_color="white")
entry_fecha.grid(row=1,column=0,pady=5,padx=2,sticky="nsew")
entry_hora=CTk.CTkEntry(frame_lugar_fecha_hora,fg_color="white")
entry_hora.grid(row=1,column=1,pady=5,padx=2,sticky="nsew")
entry_lugar=CTk.CTkEntry(frame_lugar_fecha_hora,fg_color="white")
entry_lugar.grid(row=2,column=0,columnspan=2,pady=5,padx=2,sticky="nsew")

frame_privacidad=CTk.CTkFrame(frame1,fg_color="#64a4f8")
frame_privacidad.grid(pady=4,padx=4,row=2,column=0,sticky="nsew")
frame_privacidad.columnconfigure(0,weight=1)
frame_privacidad.rowconfigure(0,weight=1)
frame_privacidad.rowconfigure(1,weight=1)
label_privacidad=CTk.CTkLabel(frame_privacidad,text="Privacidad",font=("Verdana",14,"bold"))
label_privacidad.grid(pady=5,padx=2,sticky="w")
checkbox_privacidad=CTk.CTkCheckBox(frame_privacidad,fg_color="white",text="Evento privado")
checkbox_privacidad.grid(pady=5,padx=2,sticky="nsew")

frame_cupo_inv=CTk.CTkFrame(frame1,fg_color="#6ea7f1")
frame_cupo_inv.grid(pady=4,padx=4,row=3,column=0,sticky="nsew")
frame_cupo_inv.columnconfigure(0,weight=1)
frame_cupo_inv.rowconfigure(0,weight=1)
frame_cupo_inv.rowconfigure(1,weight=1)
frame_cupo_inv.rowconfigure(2,weight=1)
label_cupo_inv=CTk.CTkLabel(frame_cupo_inv,text="Cupo de invitados",font=("Verdana",14,"bold"))
label_cupo_inv.grid(row=0,column=0,columnspan=2,pady=5,padx=2,sticky="w")
combobox_cupo_inv=CTk.CTkComboBox(frame_cupo_inv,fg_color="white",values=("Limitado","Ilimitado"))
combobox_cupo_inv.grid(row=1,column=0,columnspan=2,pady=5,padx=2,sticky="nsew")
entry_num_inv=CTk.CTkEntry(frame_cupo_inv,fg_color="white")
entry_num_inv.grid(row=2,column=0,pady=5,padx=2,sticky="nsew")
label_personas=CTk.CTkLabel(frame_cupo_inv,text="personas",font=("Verdana",14,"bold"))
label_personas.grid(row=2,column=1,pady=5,padx=2,sticky="w")

frame_estilo=CTk.CTkFrame(frame1,fg_color="#7baff4")
frame_estilo.grid(pady=4,padx=4,row=4,column=0,sticky="nsew")
frame_estilo.columnconfigure(0,weight=1)
frame_estilo.rowconfigure(0,weight=1)
frame_estilo.rowconfigure(1,weight=1)
frame_estilo.rowconfigure(2,weight=1)
frame_estilo.rowconfigure(3,weight=1)
frame_estilo.rowconfigure(4,weight=1)
frame_estilo.rowconfigure(5,weight=1)
label_estilo=CTk.CTkLabel(frame_estilo,text="Estilo",font=("Verdana",14,"bold"))
label_estilo.grid(row=0,column=0,pady=5,padx=2,sticky="w")
checkbox_estilo=CTk.CTkCheckBox(frame_estilo,fg_color="white",text="Codigo de vestimenta")
checkbox_estilo.grid(row=1,column=0,pady=5,padx=2,sticky="nsew")
combobox_estilo=CTk.CTkComboBox(frame_estilo,fg_color="white",values=( "Casual",
    "Casual elegante",
    "Coctel",
    "Formal",
    "Etiqueta rigurosa",
    "Temático"))
combobox_estilo.grid(row=2,column=0,pady=5,padx=2,sticky="nsew")
checkbox_paletaco=CTk.CTkCheckBox(frame_estilo,fg_color="white",text="Paleta de colores")
checkbox_paletaco.grid(row=3,column=0,pady=5,padx=2,sticky="nsew")
boton_ag_color=CTk.CTkButton(frame_estilo,fg_color="white",text="+ Agregar color")
boton_ag_color.grid(row=4,column=0,pady=5,padx=6,sticky="nsew")

boton_reg_evento=CTk.CTkButton(frame4,fg_color="#1277fa",text="Registrar evento")
boton_reg_evento.grid(pady=4,padx=8,row=5,column=0,sticky="nsew")

#frame invitacion
frame2=CTk.CTkFrame(frame0,fg_color="#1503b8")
frame2.grid(pady=30,padx=16,row=0,column=2,columnspan=3,sticky="nsew")
frame2.columnconfigure(0,weight=1)
frame2.columnconfigure(1,weight=2)
frame2.rowconfigure(0,weight=8)
frame2.rowconfigure(1,weight=1)

frame3=CTk.CTkFrame(frame2,fg_color="#fae9d0")
frame3.grid(pady=14,padx=16,row=0,column=0,columnspan=2,sticky="nsew")

boton_editar=CTk.CTkButton(frame2,fg_color="#220c56",text="Editar datos")
boton_editar.grid(pady=10,padx=25,row=1,column=0,sticky="nsew")

boton_guardar_inv=CTk.CTkButton(frame2,fg_color="#220c56",text="Guardar invitacion")
boton_guardar_inv.grid(pady=10,padx=25,row=1,column=1,sticky="nsew")



# Ejecutar la ventana
ventana.mainloop()

