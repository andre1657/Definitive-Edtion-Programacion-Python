import datetime as dt #import, de importa una libreria; as, recortar el termino
import random as rd
nombre ="Andre Teofanes" #valor constante
fecha = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Hola Ing.", nombre)
print("Fecha y hora de la medicion:", str(fecha))
print("Valores tomados respecto al sensor de voltaje: ")
print("                      Kelvin   Celcius   Fahrenheit")
#Conversiones para Celcius y Fahrenheit
for i in range(15):
    #v,c,f valores aleatorios o diferentes
    v = rd.randint(0, 1023) #considerando valores en kelvin
    c = round(v - 273.15 , 2) #redondear valor 2, para que tenga 2 decimales
    f = round(1.8*(v-273.15)+32 , 2)
    if v < 341:
        print("Temperatura Baja:     " + str(v) +" K    "+ str(c) +" °C   "+ str(f) +" °F")
    elif v < 682:
        print("Temperatura Media:    " + str(v) +" K    "+ str(c) +" °C   "+ str(f) +" °F")
    elif v < 1023:
        print("Temperatura Alta:     " + str(v) +" K    "+ str(c) +" °C   "+ str(f) +" °F")
