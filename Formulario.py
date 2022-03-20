from tkinter import NSEW, Tk, Label, Button, Entry, Frame, END
import  pandas as pd

window = Tk()
window.configure(background="black")
window.geometry("560x388")
window.resizable(0,0)
window.title("Guardar Datos En Excel")

nombres1,apellidos1,edad1,correo1,telefono1 = [],[],[],[],[]

def agregar_datos():
    global nombres1, apellidos1, edad1, correo1, telefono1
    
    nombres1.append(ingresa_tus_nombres.get())
    apellidos1.append(ingresa_tus_apellidos.get())
    edad1.append(ingresa_tu_edad.get())
    correo1.append(ingresa_tu_correo.get())
    telefono1.append(ingresa_tu_telefono.get())
    
    ingresa_tus_nombres.delete(0,END)
    ingresa_tus_apellidos.delete(0,END)
    ingresa_tu_edad.delete(0,END)
    ingresa_tu_correo.delete(0,END)
    ingresa_tu_telefono.delete(0,END)
    
def guardar_datos():
    global nombres1, apellidos1, edad1, correo1, telefono1
    dates = {"Nombres":nombres1, "Apellidos": apellidos1, "Edad": edad1, "Correo": correo1, "Telefono": telefono1}
    name_excel = str (nombre_archivo.get() + ".xlsx")
    dts = pd.DataFrame(dates, columns= ["Nombres", "Apellidos", "Edad", "Correo", "Telefono"])
    dts.to_excel(name_excel, index = False)
    nombre_archivo.delete(0,END)
    
frame1 = Frame(window, bg= "gray15")
frame1.grid(column = 0, row = 0, sticky = NSEW)
frame2 = Frame(window, bg= "gray16")
frame2.grid(column = 1, row = 0, sticky = NSEW)

nombre = Label(frame1, text ='Nombres', width=10).grid(column=0, row=0, pady=20, padx= 10)
ingresa_tus_nombres = Entry(frame1,  width=20, font = ('Arial',12))
ingresa_tus_nombres.grid(column=1, row=0)
    
apellidos = Label(frame1, text ='Apellido', width=10).grid(column=0, row=1, pady=20, padx= 10)
ingresa_tus_apellidos = Entry(frame1, width=20, font = ('Arial',12))
ingresa_tus_apellidos.grid(column=1, row=1)

edad = Label(frame1, text ='Edad', width=10).grid(column=0, row=2, pady=20, padx= 10)
ingresa_tu_edad = Entry(frame1,  width=20, font = ('Arial',12))
ingresa_tu_edad.grid(column=1, row=2)

correo = Label(frame1, text ='Correo', width=10).grid(column=0, row=3, pady=20, padx= 10)
ingresa_tu_correo = Entry(frame1,  width=20, font = ('Arial',12))
ingresa_tu_correo.grid(column=1, row=3)

telefono = Label(frame1, text ='Telefono', width=10).grid(column=0, row=4, pady=20, padx= 10)
ingresa_tu_telefono = Entry(frame1, width=20, font = ('Arial',12))
ingresa_tu_telefono.grid(column=1, row=4)

agregar = Button(frame1, width=20, font = ('Arial',12, 'bold'), text='Agregar', bg='orange',bd=5, command =agregar_datos)
agregar.grid(columnspan=2, row=5, pady=20, padx= 10)

archivo = Label(frame2, text ='Ingrese Nombre del archivo', width=25, bg='gray16',font = ('Arial',12, 'bold'), fg='white')
archivo.grid(column=0, row=0, pady=10, padx= 10)

nombre_archivo = Entry(frame2, width=23, font = ('Arial',12),highlightbackground = "green", highlightthickness=4)
nombre_archivo.grid(column=0, row=1, pady=1, padx= 10)

guardar = Button(frame2, width=20, font = ('Arial',12, 'bold'), text='Guardar', bg='green2',bd=5, command =guardar_datos)
guardar.grid(column=0, row=2, pady=20, padx= 10)


window.mainloop()
