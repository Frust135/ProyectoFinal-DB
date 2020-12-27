import psycopg2 as psy
from tkinter import Listbox, W, E, END, Entry, Place

password = "admin123"
#-------------------------------------------------------------------
#      Función para Agregar un Cliente
#-------------------------------------------------------------------

def insertar_cliente(rut, nombre, apellido):
    #Indicamos los datos de la db a la cual nos vamos a conectar
    con = psy.connect(dbname="postgres",
            user="postgres",
            password=password,
            host="localhost",
            port="5432"
    )
    #Generamos el cursos, el cual permite ejecutar que python ejecute comandos de PostgreSQL
    cursor = con.cursor()
    #Generamos la consulta
    query = '''INSERT INTO cliente(rut, nombre, apellido)  VALUES (%s, %s, %s)'''
    #Ejecutamos la consulta con los valores ingresados
    cursor.execute(query,(rut,nombre,apellido))
    print("Cliente ingresado con éxito.")
    #Finalizamos la conexión
    con.commit()
    con.close()

#-------------------------------------------------------------------
#      Función para Agregar una rendición
#-------------------------------------------------------------------

def ingresar_rendicion(ren_id, fecha, puntaje, estado, observaciones, empleado_empl_id, cliente_client_id, tipo_examen_tip_id, ventana):
    #Indicamos los datos de la db a la cual nos vamos a conectar
    con = psy.connect(dbname="postgres",
            user="postgres",
            password=password,
            host="localhost",
            port="5432"
    )
    #Generamos el cursos, el cual permite ejecutar que python ejecute comandos de PostgreSQL
    cursor = con.cursor()
    #Generamos la consulta
    query = '''INSERT INTO rendicion(ren_id, fecha, puntaje, estado, observaciones, empleado_empl_id, cliente_client_id, tipo_examen_tip_id)  
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
    #Ejecutamos la consulta con los valores ingresados
    cursor.execute(query,(ren_id, fecha, puntaje, estado, observaciones, empleado_empl_id, cliente_client_id, tipo_examen_tip_id))
    print("Examen ingresado con éxito.")
    #Finalizamos la conexión
    con.commit()
    con.close()
    #Refrescamos la tabla
    mostrar_rendiciones(ventana)

#-------------------------------------------------------------------
#      Función para mostrar la tabla
#-------------------------------------------------------------------

def mostrar_rendiciones(ventana):
    con = psy.connect(dbname="postgres",
        user="postgres",
        password=password,
        host="localhost",
        port="5432"
    )
    cursor = con.cursor()
    query = '''SELECT * FROM rendicion 
    inner join cliente on rendicion.cliente_client_id = cliente.client_id 
    inner join empleado on rendicion.empleado_empl_id = empleado.empl_id
    inner join tipo_examen on rendicion.tipo_examen_tip_id = tipo_examen.tip_id'''
    cursor.execute(query)
    fila = cursor.fetchall() #Obtenemos la fila de datos
    lista = Listbox(ventana, width=226, heigh=17) 
    lista.place(x=10, y=630)
    #Agregamos las filas a la tabla
    for recorrido in fila:
        lista.insert(END, 
        " ID Examen: " + str(recorrido[0]) + " - " +
        " ID Tipo de Examen: " + str(recorrido[7]) + " - " + 
        " Nombre del Examen: " + recorrido[17] + " - " +
        " ID Cliente: " + str(recorrido[6]) + " - " +
        " RUT Cliente: " + recorrido[9] + " - " +
        " Puntaje: " + str(recorrido[2]) + " - " +
        " Estado: " + recorrido[3] + " - " + 
        " Observaciones: " + recorrido[4] + " - " +
        " Fecha: " + recorrido[1] + " - " + 
        " ID Empleado: " + str(recorrido[5]) + " - "+
        " Nombre Empleado: " + recorrido[14] + " " + recorrido[15]
        )
    con.commit()
    con.close()    

#-------------------------------------------------------------------
#      Función de búsqueda
#-------------------------------------------------------------------
def busqueda(id_examen, id_empleado, id_cliente, estado, fecha,ventana):
    con = psy.connect(dbname="postgres",
        user="postgres",
        password=password,
        host="localhost",
        port="5432"
    )
    cursor = con.cursor()
    select = '''SELECT * '''
    query = '''
    FROM rendicion inner join cliente on rendicion.cliente_client_id = cliente.client_id 
    inner join empleado on rendicion.empleado_empl_id = empleado.empl_id
    inner join tipo_examen on rendicion.tipo_examen_tip_id = tipo_examen.tip_id
    where 
    '''
    if (id_examen == "0"): query+= '''tipo_examen.tip_id > %s and '''
    else: query+= '''tipo_examen.tip_id = %s and '''

    if (id_empleado == "0"): query+= '''empleado.empl_id > %s and '''
    else: query+= '''empleado.empl_id  = %s and '''

    if (id_cliente == "0"): query+= '''cliente.client_id > %s and '''
    else: query+= '''cliente.client_id = %s and '''

    if (estado == "C"): query+= '''rendicion.estado != %s and '''
    else: query+= '''rendicion.estado = %s and '''

    if (fecha == "F"): query+= '''rendicion.fecha != %s'''
    else: query+= '''rendicion.fecha = %s '''

    query_estadistica = query #Query para luego utilizar en la estadistica

    query=select+query

    cursor.execute(query,(id_examen,id_empleado, id_cliente, estado, fecha))
    fila = cursor.fetchall() #Obtenemos la fila de datos
    lista = Listbox(ventana, width=226, heigh=17) 
    lista.place(x=10, y=630)
    #Agregamos las filas a la tabla
    for recorrido in fila:
        lista.insert(END, 
        " ID Examen: " + str(recorrido[0]) + " - " +
        " ID Tipo de Examen: " + str(recorrido[7]) + " - " + 
        " Nombre del Examen: " + recorrido[17] + " - " +
        " ID Cliente: " + str(recorrido[6]) + " - " +
        " RUT Cliente: " + recorrido[9] + " - " +
        " Puntaje: " + str(recorrido[2]) + " - " +
        " Estado: " + recorrido[3] + " - " + 
        " Observaciones: " + recorrido[4] + " - " +
        " Fecha: " + recorrido[1] + " - " + 
        " ID Empleado: " + str(recorrido[5]) + " - "+
        " Nombre Empleado: " + recorrido[14] + " " + recorrido[15]
        )
    con.commit()
    con.close()    
    try:
        promedio_puntaje(id_examen,id_empleado, id_cliente, estado, fecha, query_estadistica)
        promedio_aprobacion(id_examen,id_empleado, id_cliente, estado, fecha, query_estadistica)
    except:
        None
   
#-------------------------------------------------------------------
#      Función para obtener el promedio del puntaje
#-------------------------------------------------------------------

def promedio_puntaje(id_examen,id_empleado, id_cliente, estado, fecha, query_estadistica):
    con = psy.connect(dbname="postgres",
        user="postgres",
        password=password,
        host="localhost",
        port="5432"
    )
    cursor = con.cursor()
    query_estadistica = '''SELECT sum(rendicion.puntaje), count(*) ''' + query_estadistica
    cursor.execute(query_estadistica,(id_examen,id_empleado, id_cliente, estado, fecha))
    fila = cursor.fetchall()
    con.commit()
    con.close() 

    promedio = str(round((fila[0][0] / fila[0][1]),2))
    promedio = "Total de examenes: " + str(fila[0][1]) +" - "+ " Promedio: " + promedio

    estadistica_examenes_tomados_entry = Entry(bg="white", width=50)
    estadistica_examenes_tomados_entry.insert(0, promedio)
    estadistica_examenes_tomados_entry.config(state="disable")
    estadistica_examenes_tomados_entry.place(x=545, y=450)

#-------------------------------------------------------------------
#      Función para obtener el promedio de examenes aprobados y reprobados
#-------------------------------------------------------------------
def promedio_aprobacion(id_examen,id_empleado, id_cliente, estado, fecha, query_estadistica):
    con = psy.connect(dbname="postgres",
        user="postgres",
        password=password,
        host="localhost",
        port="5432"
    )
    cursor = con.cursor()
    query_estadistica = '''
    SELECT 
	count(CASE WHEN rendicion.estado='R' then 1 END) as reprobados,
	count(CASE WHEN rendicion.estado='A' then 1 END) as aprobados 
    ''' + query_estadistica
    cursor.execute(query_estadistica,(id_examen,id_empleado, id_cliente, estado, fecha))
    fila = cursor.fetchall()
    con.commit()
    con.close() 
    total = fila[0][0] + fila[0][1]
    promedio_reprobados = round((fila[0][0] / total), 2)
    promedio_aprobados = round((fila[0][1] / total), 2)

    texto_aprobados = "Examenes aprobados: " + str(fila[0][1]) +" - " + "Promedio: " + str(promedio_aprobados)
    texto_reprobados = "Examenes reprobados: " + str(fila[0][0]) +" - " + "Promedio: " + str(promedio_reprobados)

    estadistica_examenes_aprobados_entry = Entry(bg="white", width=50)
    estadistica_examenes_aprobados_entry.insert(0, texto_aprobados)
    estadistica_examenes_aprobados_entry.config(state="disable")
    estadistica_examenes_aprobados_entry.place(x=545, y=510)

    estadistica_examenes_reprobados_entry = Entry(bg="white", width=50)
    estadistica_examenes_reprobados_entry.insert(0, texto_reprobados)
    estadistica_examenes_reprobados_entry.config(state="disable")
    estadistica_examenes_reprobados_entry.place(x=545, y=570)
#-------------------------------------------------------------------
#      Función para obtener información de los clientes
#-------------------------------------------------------------------

def get_cliente():
    con = psy.connect(dbname="postgres",
            user="postgres",
            password=password,
            host="localhost",
            port="5432"
    )
    cursor = con.cursor()
    query = '''SELECT * FROM cliente'''
    cursor.execute(query)
    datos_clientes = cursor.fetchall()
    lista_clientes = []
    for recorrido in datos_clientes:
        lista_clientes.append("ID: "+ str(recorrido[0])+ " RUT " + recorrido[1])
    con.commit()
    con.close()
    return lista_clientes

#-------------------------------------------------------------------
#      Función para obtener información de los empleados
#-------------------------------------------------------------------

def get_empleado():
    con = psy.connect(dbname="postgres",
            user="postgres",
            password=password,
            host="localhost",
            port="5432"
    )
    cursor = con.cursor()
    query = '''SELECT * FROM empleado'''
    cursor.execute(query)
    datos_empleado = cursor.fetchall()
    lista_empleado = []
    for recorrido in datos_empleado:
        lista_empleado.append("ID: "+ str(recorrido[0])+" RUT: "+recorrido[1])
    con.commit()
    con.close()
    return lista_empleado

#-------------------------------------------------------------------
#      Función para obtener información de los exámenes
#-------------------------------------------------------------------

def get_examen():
    con = psy.connect(dbname="postgres",
            user="postgres",
            password=password,
            host="localhost",
            port="5432"
    )
    cursor = con.cursor()
    query = '''SELECT * FROM tipo_examen'''
    cursor.execute(query)
    datos_examenes = cursor.fetchall()
    lista_examenes = []
    for recorrido in datos_examenes:
        lista_examenes.append("ID: "+ str(recorrido[0])+" - "+recorrido[1])
    con.commit()
    con.close()
    return lista_examenes

