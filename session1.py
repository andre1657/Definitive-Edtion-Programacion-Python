import datetime as dt
import random as rd
nombre ="Andre Teofanes"
fecha = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
v = rd.randint(0, 1023)
print("Hola Ing.", nombre)
print("Fecha y hora de la medicion:", str(fecha))
print ("Voltaje medido por el sensor " + str(v))
