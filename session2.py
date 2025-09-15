nombre = "Andre"              #constante por convecion - str
edad = 20                     #constante por convecion - int
voltaje = 3.14159                   #constante por convecion - float
activo = True                  #constante por convecion - bool
print(type(voltaje))       #imprime el tipo de dato de la variable voltaje
#f-string para formato para cadenas de caracteres, letras
print(f"Hola {nombre}, tienes {edad} años, el voltaje es {voltaje} V y el estado es {activo}.") 
#f-string para formatear la salida
print(f"voltaje: {voltaje:.2f} V | Activo: {activo}")  #imprime voltaje con 2 decimales
print(f"Tipos -> edad:{type(edad).__name__}, voltaje:{type(voltaje).__name__}, activo:{type(activo).__name__}")  #imprime el tipo de dato de cada variable

print(f"Hola ing. {nombre}, tienes {edad} años, el voltaje medido es { voltaje:.2f} V | Activo: {activo}.")  #f-string para formatear la salida