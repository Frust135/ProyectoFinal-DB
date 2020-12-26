import psycopg2 as psy

#-------------------------------------------------------------------
#      Función para Agregar un Cliente
#-------------------------------------------------------------------
password = "admin123"

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
