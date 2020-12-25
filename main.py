#https://coolors.co/283d3b-197278-edddd4-c44536-772e25
#-------------------------------------------------------------------
#      Importación de librerías
#-------------------------------------------------------------------
from tkinter import * 

#-------------------------------------------------------------------
#      Creación de ventana
#-------------------------------------------------------------------
mywindow = Tk()
mywindow.geometry("1100x920")
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
             width = "70",
             height = "25")
box_ingresar.place(x = 25, y = 90)
 
titulo_seleccion = Label(text = "Ingresar Examen", 
               font = ("Mono",15),
               fg = "#772E25",
               bg = "#EDDDD4")

titulo_seleccion.place(x=185, y=100)
#-------------------------------------------------------------------
#      Box de Revisar Examen
#-------------------------------------------------------------------

box_revisar = Label(bg = "#EDDDD4",
             width = "70",
             height = "25")
box_revisar.place( x= 580, y= 90)

titulo_revisar = Label(text = "Revisar Examen", 
               font = ("Mono",15),
               fg = "#772E25",
               bg = "#EDDDD4")

titulo_revisar.place(x=765, y=100)

#-------------------------------------------------------------------
#      Box de Tabla
#-------------------------------------------------------------------

box_tabla = Label(bg = "#EDDDD4",
             width = "153",
             height = "27")
box_tabla.place(x=12, y = 500)
#-------------------------------------------------------------------
#      Loop de la interfaz
#-------------------------------------------------------------------
mywindow.mainloop()