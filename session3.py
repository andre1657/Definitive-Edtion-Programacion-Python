import random as rad 
lista=[]
for i in range(5):
               n=rad.randint(1,10)
               lista.append(n)
print(lista)

vol_square=[]
V= [4.5 , 2.32 ,4.88]
for i in V:
        vol_square.append(i**2)
print(vol_square)

lecturas=[4.9 , 4.10 , 4.88]
for idx, vol in enumerate(lecturas, start=1):
    print(f"Lectura {idx}: {vol:.2f} V")

import random as dr
valores=[]
for i in range(10):
               n=dr.randint(1,10)
               valores.append(n)
               if n>5:
                              print(f"Valor {i+1}: {n} -Voltaje Alto")
               else:
                              print(f"Valor {i+1}: {n} - Voltaje Bajo")
vmayor=[]
Vmenor=[]
for v in valores:
               if v>5:
                              vmayor.append(v)
               else:
                              Vmenor.append(v)
print("Valores mayores a 5:", vmayor)
print("Valores menores o iguales a 5:", Vmenor)

import random as rds
valores_medio=[]
valores_alto=[]
Valores_bajo=[]
for i in range(30):
        m = rds.randint(1, 30)
        if m > 20:
            valores_alto.append(m)
        elif m > 10:
            valores_medio.append(m)
        else:
            Valores_bajo.append(m)

print("Valores Altos:", valores_alto)
print("Valores Medios:", valores_medio)  
print("Valores Bajos:", Valores_bajo)


