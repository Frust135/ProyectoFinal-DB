#https://coolors.co/283d3b-197278-edddd4-c44536-772e25
#-------------------------------------------------------------------
#      Importar librerías
#-------------------------------------------------------------------
from tkinter import Label, Tk, Entry, IntVar, Radiobutton, ttk, Button, messagebox
from database import insertar_cliente, get_cliente, get_empleado, get_examen, ingresar_rendicion, mostrar_rendiciones, busqueda, promedio_puntaje
#-------------------------------------------------------------------
#      Funciones de la intefaz
#-------------------------------------------------------------------

# --- FUNCIÓN PARA INSERTAR UN CLIENTE, Y ACTUALIZAR LA INTERFAZ ---
def insertar_cliente_update(rut,nombre,apellido):
    insertar_cliente(rut,nombre,apellido)
    clientes_update(get_cliente())

# --- FUNCIÓN PARA ACTUALIZAR LA INTERFAZ ---

def clientes_update(valores):
    rendicion_usuario_combobox['values'] = get_cliente()

    valores_busqueda = (["Todos"] + valores)
    busqueda_cliente_combobox['values'] = valores_busqueda

# --- FUNCIÓN PARA INSERTAR UNA RENDICIÓN ---

def ingresar_rendicion_interfaz(ren_id, fecha, puntaje, estado, observaciones, empleado_empl_id, cliente_client_id, tipo_examen_tip_id):
    try:
        #Convertimos los datos en datos que puedan ser almacenados en la tabla
        if estado == 1: estado='A'
        else: estado = 'R'
        empleado_empl_id = empleado_empl_id[4]
        cliente_client_id = cliente_client_id[4]
        tipo_examen_tip_id = tipo_examen_tip_id[4]
        try:
            ingresar_rendicion(ren_id, fecha, puntaje, estado, observaciones, empleado_empl_id, cliente_client_id, tipo_examen_tip_id, mywindow)
        except: 
            messagebox.showerror("Error", "El ID del examen ya esta en uso.")
    except: 
        messagebox.showerror("Error", "Ingrese todos los datos.")
    

# --- FUNCIÓN PARA LIMPIAR LA BUSQUEDA DE LA INTERFAZ ---

def busqueda_limpieza_datos(id_examen, id_empleado, id_cliente, estado, fecha):
    #Convertimos los datos en datos que puedan ser utilizados para realizar la Query
    if (id_examen != "Todos"): id_examen = id_examen[4]
    else: id_examen = '0'

    if (id_empleado != "Todos"): id_empleado = id_empleado[4]
    else: id_empleado = '0'

    if (id_cliente != "Todos"): id_cliente = id_cliente[4]
    else: id_cliente = '0'

    if estado == "Aprobado": estado='A'
    elif estado == "Reprobado": estado='R'
    else: estado ='C'

    if fecha == '': fecha = 'F'
    
    busqueda(id_examen, id_empleado, id_cliente, estado, fecha, mywindow)


#-------------------------------------------------------------------
#      Creación de ventana
#-------------------------------------------------------------------
mywindow = Tk()
mywindow.geometry("1380x920")
mywindow.title("Exámenes de Certificación")
mywindow.configure(bg="#197278")
mostrar_rendiciones(mywindow)
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

rendicion_usuario_combobox = ttk.Combobox(state="readonly")
rendicion_usuario_combobox['values'] = get_cliente()
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

rendicion_empleado_combobox = ttk.Combobox(values=get_empleado(), state="readonly")
rendicion_empleado_combobox.current(0)
rendicion_empleado_combobox.place(x=180, y=453)

# ------------------- RENDICIÓN TIPO EXAMEN --------------------
rendicion_tipoExamen = Label(text = "Tipo de Examen", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")

rendicion_tipoExamen.place(x=40, y=500)

rendicion_tipoExamen_combobox = ttk.Combobox(values=get_examen(), state="readonly")
rendicion_tipoExamen_combobox.current(0)
rendicion_tipoExamen_combobox.place(x=180, y=503)

# ------------------- RENDICIÓN INGRESAR --------------------

rendicion_boton = Button(
    text="Ingresar Examen",
    bg="white",
    fg="black",
    command= lambda: ingresar_rendicion_interfaz(
        rendicion_id_entry.get(),
        rendicion_fecha_entry.get(),
        rendicion_puntaje_entry.get(),
        opcionEstado.get(),
        rendicion_observaciones_entry.get(),
        rendicion_empleado_combobox.get(),
        rendicion_usuario_combobox.get(),
        rendicion_tipoExamen_combobox.get()
        )
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
    fg="black",
    command= lambda: insertar_cliente_update(
        usuario_rut_entry.get(),
        usuario_nombre_entry.get(),
        usuario_apellido_entry.get()
    )
    
)

rendicion_boton.place(x=655, y=305)

#-------------------------------------------------------------------
#      Box de Estadistica
#-------------------------------------------------------------------

box_estadistica = Label(bg = "#EDDDD4",
             width = "50",
             height = "16")
box_estadistica.place( x= 520, y= 370)

titulo_estadistica = Label(text = "Estadísticas", 
               font = ("Mono",15),
               fg = "#772E25",
               bg = "#EDDDD4")

titulo_estadistica.place(x=640, y=380)

# ------------------- ESTADISTICA EXAMENES TOMADOS --------------------

estadistica_examenes_tomados = Label(text = "Promedio de Puntajes", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")
estadistica_examenes_tomados.place(x=540, y=420)


# ------------------- ESTADISTICA EXAMENES APROBADOS --------------------

estadistica_examenes_aprobados = Label(text = "Promedio de Examenes Aprobados", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")
estadistica_examenes_aprobados.place(x=540, y=480)



# ------------------- ESTADISTICA EXAMENES REPROBADOS --------------------

estadistica_examenes_reprobados = Label(text = "Promedio de Examenes Reprobados", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")
estadistica_examenes_reprobados.place(x=540, y=540)



#-------------------------------------------------------------------
#      Box de búsqueda
#-------------------------------------------------------------------

box_busqueda = Label(bg = "#EDDDD4",
             width = "60",
             height = "24")
box_busqueda.place(x = 930, y = 90)
 
titulo_busqueda = Label(text = "Búsqueda", 
               font = ("Mono",15),
               fg = "#772E25",
               bg = "#EDDDD4")

titulo_busqueda.place(x=1100, y=100)

# ------------------- BUSQUEDA POR TIPO DE EXAMEN --------------------

busqueda_tipo_examen = Label(text = "Tipo de Examen", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")
busqueda_tipo_examen.place(x=950, y=150)

valores_busqueda_examen = (["Todos"] + get_examen())

busqueda_tipo_examen_combobox = ttk.Combobox(values=valores_busqueda_examen, state="readonly")
busqueda_tipo_examen_combobox.current(0)

busqueda_tipo_examen_combobox.place(x=1100, y=153)

# ------------------- BUSQUEDA POR EMPLEADO --------------------

busqueda_empleado = Label(text = "Por Empleado", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")
busqueda_empleado.place(x=950, y=200)

valores_busqueda_empleado = (["Todos"] + get_empleado())

busqueda_empleado_combobox = ttk.Combobox(values=valores_busqueda_empleado, state="readonly")
busqueda_empleado_combobox.current(0)

busqueda_empleado_combobox.place(x=1100, y=203)

# ------------------- BUSQUEDA POR CLIENTE --------------------

busqueda_cliente = Label(text = "Por Cliente", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")
busqueda_cliente.place(x=950, y=250)

busqueda_cliente_combobox = ttk.Combobox(state="readonly")
busqueda_cliente_combobox['values'] = (['Todos'] + get_cliente())
busqueda_cliente_combobox.current(0)
busqueda_cliente_combobox.place(x=1100, y=253)

# ------------------- BUSQUEDA POR ESTADO --------------------

busqueda_estado = Label(text = "Por Estado", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")
busqueda_estado.place(x=950, y=300)

busqueda_estado_combobox = ttk.Combobox(values=["Todos","Aprobado", "Reprobado"], state="readonly")
busqueda_estado_combobox.current(0)

busqueda_estado_combobox.place(x=1100, y=303)

# ------------------- BUSQUEDA POR FECHA --------------------

busqueda_fecha = Label(text = "Por Fecha", 
               font = ("Mono",13),
               fg = "#772E25",
               bg = "#EDDDD4")
busqueda_fecha.place(x=950, y=350)

busqueda_fecha_entry = Entry(bg="white")

busqueda_fecha_entry.place(x=1100, y=353)

# ------------------- BUSQUEDA BOTÓN --------------------

rendicion_boton = Button(
    text="Búscar Exámenes",
    bg="white",
    fg="black",
    command = lambda: busqueda_limpieza_datos(
        busqueda_tipo_examen_combobox.get(),
        busqueda_empleado_combobox.get(),
        busqueda_cliente_combobox.get(),
        busqueda_estado_combobox.get(),
        busqueda_fecha_entry.get()
         )
)

rendicion_boton.place(x=1105, y=405)
#-------------------------------------------------------------------
#      Loop de la interfaz
#-------------------------------------------------------------------
busqueda_limpieza_datos(
        busqueda_tipo_examen_combobox.get(),
        busqueda_empleado_combobox.get(),
        busqueda_cliente_combobox.get(),
        busqueda_estado_combobox.get(),
        busqueda_fecha_entry.get()
)

mywindow.mainloop()