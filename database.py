import psycopg2 as psy
from tkinter import Listbox, W, E, END

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

