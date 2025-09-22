import matplotlib.pyplot as plt #
import numpy as np

def aleatorio(n=20):
        #Docstring
    """permite generar numeros aleatorios de valor entero entre 1 y 30 y da de salida una lista de valores

    Args:
        n (int, optional): numero el datos ingresados. Defecto 20.
    """
    import random as rd
    Value=[] #lista vacia
    for i in range (n): #incio de un bucle es con el : el identado es importante
        Value.append(rd.randint(1,30)) #append añade a la lista\
    return(Value) #lo que devuelve la funcion

ejex=[i for i in range (30)] #crea una lista de 0 a 29 para el eje X
ejey=np.sin(aleatorio(30)) #genera 30 numeros aleatorios y les aplica la funcion seno
ejey2=np.cos(aleatorio(30)) #genera 30 numeros aleatorios y les aplica la funcion coseno
ejey3=np.array(ejey)-np.array(ejey2) #Calcula la diferencia entre los valores de seno y coseno
figtitle="grafico comparativo de valores aleatorios" #titulo del grafico
plt.title(figtitle.upper(),fontdict={'fontweight': 'bold'}) #establece el titulo en mayuscula y negrita
plt.xlabel("numero de datos") #etiqueta para el eje X
plt.ylabel("valores aleatorios") #etiqueta para el eje Y
plt.plot(ejex,ejey,color="#b058a4d6",marker='o', linestyle=':',linewidth=1, markersize=5,label="aleatorio 1") #(ejex, ejey, caracteristicas)
plt.plot(ejex,ejey2,'b--^',linewidth=1, markersize=5,label="aleatorio 2") #(ejex, ejey, caracteristicas)
plt.plot(ejex,ejey3,'g',linewidth=2, markersize=5,label="aleatorio 2") #(ejex, ejey, caracteristicas)
plt.legend()
plt.grid()
plt.show()