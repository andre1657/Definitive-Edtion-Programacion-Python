print("Genera tu boleta de reporte")
print("Ingrese los siguientes datos:")
nombre = str(input("Nombre del trabajador:"))
equip=str(input("Equipo:"))
codigo= int(input("Codigo:"))
print("Considere las siguiente opciones para voltaje 1 y para temepartura en celcius 2 ")
mues = str(input("Muestras a considerarse:"))
formato=input("Formato de las muestras:")
Acum=0
for i in formato:
     valor_1= input(f"Valor de la muestra: {i}")

     Acum=Acum+valor_1
     
try:
    promedio=(Acum)/i
    valor_1.append(i)
    if promedio >=30:
        print(f"Alumno: {nombre} a| equipo: {equip} - {codigo}")
        print(f"Valor muestra {i }: {valor_1} | Promedio: {promedio} V")
        print(f"Estado: Alto(>= 30 C°)")
    elif promedio < 0 :
        print(f"Alumno: {nombre} | equipo: {equip} - {codigo}")
        print(f"Valor muestra {i }: {valor_1} | Promedio: {promedio} V")
        print(f"Estado: Bajo(< 0 C°)")
    else:
        print(f"Alumno: {nombre} | equipo: {equip} - {codigo}")
        print(f"Valor muestra {i }: {valor_1} | Promedio: {promedio} V")
        print(f"Estado: Normal (0 a 30 C°)")
except ValueError:
    print("Error: Por favor ingrese valores numéricos válidos para las muestras. ejemplo 12.5")

            