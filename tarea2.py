import datetime as dt #import, de importa una libreria; as, recortar el termino
import random as rd
nombre ="Andre Teofanes" #valor constante
fecha = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Hola Ing. {nombre}, se le envia datos de temperatura, la fecha y hora actual es {fecha}.")  #f-string para formatear la salida
#Conversiones para Celcius y Fahrenheit
for i in range(15):
    #v,c,f valores aleatorios o diferentes
    v = rd.randint(0, 1023) #considerando valores en kelvin
    c = v - 273.15 #redondear valor 2, para que tenga 2 decimales
    f = 1.8*(v-273.15)+32
    if v < 341:
        print(f"Temperatura Baja:     {v} K    {c:.2f} °C   {f:.2f} °F")
    elif v < 682:
        print(f"Temperatura Media:    {v} K    {c:.2f} °C   {f:.2f} °F")
    elif v < 1023:
          print(f"Temperatura Alta:     {v} K    {c:.2f} °C   {f:.2f} °F")

