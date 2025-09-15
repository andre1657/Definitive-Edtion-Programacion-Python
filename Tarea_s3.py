#Generar 10 numeros aleatorios entre 1 y 10.
#Ordenar los numeros en una lista mayor a menor
#mostrar la lista ordenada en ascendente y descendente
import random as rd #importar libreria random
numeros = [] #Lista vacia
for i in range(10):          
               n = rd.randint(1, 10) #Generar numero aleatorio
               numeros.append(n) #Agregar numero a la lista
print("Lista original:", numeros) #Mostrar lista original
numeros.sort() #Ordenar lista
print("Lista ordenada ascendente:", numeros) #Mostrar lista ordenada
numeros.sort(reverse=True) #Ordenar lista en orden descendente
print("Lista ordenada descendente:", numeros) #Mostrar lista ordenada en orden descendente
#por Algoritmo de ordenamiento
print("///////////////////////////////////////////////////////////////") #Ordenamiento Burbuja
import random as rdm
numeros2 = [] #Lista vacia
for i in range(10):          
               n = rdm.randint(1, 10) #Generar numero aleatorio
               numeros2.append(n) #Agregar numero a la lista
print("Lista original:", numeros2) #Mostrar lista original
#Algoritmo de ordenamiento burbuja
for i in range(len(numeros2)): #Recorrer la lista
               for j in range(0, len(numeros2)-i-1): #Recorrer la lista
                              if numeros2[j] > numeros2[j+1]: #Comparar elementos
                                             numeros2[j], numeros2[j+1] = numeros2[j+1], numeros2[j] #Intercambiar elementos
print("Lista ordenada ascendente (burbuja):", numeros2) #Mostrar lista ordenada
#Orden descendente
for i in range(len(numeros2)): #Recorrer la lista
               for j in range(0, len(numeros2)-i-1): #Recorrer la lista
                              if numeros2[j] < numeros2[j+1]:#Comparar elementos
                                             numeros2[j], numeros2[j+1] = numeros2[j+1], numeros2[j] #Intercambiar elementos
print("Lista ordenada descendente (burbuja):", numeros2) #Mostrar lista ordenada  