#https://coolors.co/283d3b-197278-edddd4-c44536-772e25
#-------------------------------------------------------------------
#      Importación de librerías
#-------------------------------------------------------------------
from tkinter import Label, Tk, Entry, IntVar, Radiobutton, ttk, Button

#-------------------------------------------------------------------
#      Creación de ventana
#-------------------------------------------------------------------
mywindow = Tk()
mywindow.geometry("1300x920")
mywindow.title("mywindow")
mywindow.configure(bg="#197278")

#-------------------------------------------------------------------
#      Titulo
#-------------------------------------------------------------------

titulo = Label(text = "Exámenes de Certificación", 
               font = ("Mono",15),
               fg = "#edddd4",
               bg = "#283d3b",
               width = "200",
               height = "3")

titulo.pack()

#-------------------------------------------------------------------
#      Box de ingresar de Examen
#-------------------------------------------------------------------

box_ingresar = Label(bg = "#EDDDD4",
             width = "60",
             height = "34")
box_ingresar.place(x = 25, y = 90)
 
titulo_seleccion = Label(text = "Ingresar Examen", 
               font = ("Mono",15),
               fg = "#772E25",
               bg = "#EDDDD4")

titulo_seleccion.place(x=165, y=100)

# ------------------- RENDICIÓN ID --------------------

rendicion_id = Label(text = "Rendición ID", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")
rendicion_id.place(x=40, y=150)

rendicion_id_entry = Entry(bg="white")

rendicion_id_entry.place(x=180, y=153)

# ------------------- RENDICIÓN USUARIO --------------------

rendicion_cliente = Label(text = "Cliente", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")
rendicion_cliente.place(x=40, y=200)
rendicion_usuario_combobox = ttk.Combobox(values=["Java Nivel 1","Java Nivel 2", "Java Nivel 3", "Oracle Básico","Oracle Intermedio", "Oracle Experto"], state="readonly")

rendicion_usuario_combobox.place(x=180, y=203)

# ------------------- RENDICIÓN FECHA --------------------

rendicion_fecha = Label(text = "Fecha", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")

rendicion_fecha.place(x=40, y=250)

rendicion_fecha_entry = Entry(bg="white")

rendicion_fecha_entry.place(x=180, y=253)

# ------------------- RENDICIÓN PUNTAJE --------------------

rendicion_puntaje = Label(text = "Puntaje", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")

rendicion_puntaje.place(x=40, y=300)

rendicion_puntaje_entry = Entry(bg="white")

rendicion_puntaje_entry.place(x=180, y=303)

# ------------------- RENDICIÓN OBSERVACIONES --------------------

rendicion_observaciones = Label(text = "Observaciones", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")

rendicion_observaciones.place(x=40, y=350)

rendicion_observaciones_entry = Entry(bg="white")

rendicion_observaciones_entry.place(x=180, y=353)

# ------------------- RENDICIÓN ESTADO --------------------

rendicion_estado = Label(text = "Estado", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")

rendicion_estado.place(x=40, y=400)

opcionEstado = IntVar()

opcionEstado_aprobado = Radiobutton(text="Aprobado", 
            bg= "#EDDDD4",
            variable=opcionEstado, 
            value=1)
            
opcionEstado_aprobado.place(x=160, y=403)

opcionEstado_reprobado = Radiobutton(text="Reprobado", 
            bg= "#EDDDD4",
            variable=opcionEstado, 
            value=2)
opcionEstado_reprobado.place(x=250, y=403)

# ------------------- RENDICIÓN EMPLEADO --------------------
rendicion_empleado = Label(text = "Empleado", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")

rendicion_empleado.place(x=40, y=450)

rendicion_empleado_combobox = ttk.Combobox(values=["Inés","Martín"], state="readonly")
rendicion_empleado_combobox.current(0)
rendicion_empleado_combobox.place(x=180, y=453)

# ------------------- RENDICIÓN TIPO EXAMEN --------------------
rendicion_tipoExamen = Label(text = "Tipo de Examen", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")

rendicion_tipoExamen.place(x=40, y=500)

rendicion_tipoExamen_combobox = ttk.Combobox(values=["Java Nivel 1","Java Nivel 2", "Java Nivel 3", "Oracle Básico","Oracle Intermedio", "Oracle Experto"], state="readonly")
rendicion_tipoExamen_combobox.current(0)
rendicion_tipoExamen_combobox.place(x=180, y=503)

# ------------------- RENDICIÓN INGRESAR --------------------

rendicion_boton = Button(
    text="Ingresar Examen",
    bg="white",
    fg="black"
)

rendicion_boton.place(x=190, y=560)

#-------------------------------------------------------------------
#      Box de Usuario
#-------------------------------------------------------------------

box_revisar = Label(bg = "#EDDDD4",
             width = "50",
             height = "17")
box_revisar.place( x= 520, y= 90)

titulo_revisar = Label(text = "Ingresar Cliente", 
               font = ("Mono",15),
               fg = "#772E25",
               bg = "#EDDDD4")

titulo_revisar.place(x=630, y=100)

# ------------------- USUARIO NOMBRE --------------------

usuario_nombre = Label(text = "Nombre", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")
usuario_nombre.place(x=540, y=150)

usuario_nombre_entry = Entry(bg="white")

usuario_nombre_entry.place(x=640, y=153)

# ------------------- USUARIO APELLIDO --------------------

usuario_apellido = Label(text = "Apellido", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")
usuario_apellido.place(x=540, y=200)

usuario_apellido_entry = Entry(bg="white")

usuario_apellido_entry.place(x=640, y=203)

# ------------------- USUARIO RUT --------------------

usuario_rut = Label(text = "RUT", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")
usuario_rut.place(x=540, y=250)

usuario_rut_entry = Entry(bg="white")

usuario_rut_entry.place(x=640, y=253)

# ------------------- USUARIO INGRESAR --------------------

rendicion_boton = Button(
    text="Ingresar Cliente",
    bg="white",
    fg="black"
)

rendicion_boton.place(x=655, y=305)
#-------------------------------------------------------------------
#      Box de Tabla
#-------------------------------------------------------------------


#-------------------------------------------------------------------
#      Loop de la interfaz
#-------------------------------------------------------------------
mywindow.mainloop()