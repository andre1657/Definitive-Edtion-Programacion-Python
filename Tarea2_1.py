valor_txt = input("ingrese los valores de Temperatura en C")
print(valor_txt)
t = float(valor_txt)
if t >= 30 :
               print("Hace calor")
elif t < 0 :
               print("Hace frio")
else:
               print("Hace un clima agradable")

print("Por favor, ingrese un número válido para la temperatura.")


