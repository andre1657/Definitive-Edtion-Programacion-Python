from pathlib import Path
ROOT = Path(__file__).resolve().parents[0] # Ir a la carpeta padre
TXT = ROOT /"Archivos"/ "mediciones_200_mixto.txt"
valores = [] #lista vacia para almacenar los valores leidos del archivo
with open(TXT,'r', encoding='"utf-8"') as f:
               for linea in f: #lee linea porlinea del achivo ingresado
                       s=linea.strip() #elimina los espacios en blanco al inicio y al final de la linea
                       if not s or s.startswith('#'): #si la linea esta vacia o empieza con # (comentario) la ignora
                               continue
                       if not s or s.startswith('!'): #si la linea esta vacia o empieza con ! (comentario) la ignora
                               continue
                       s=s.replace(',','.') #reemplaza las comas por puntos para manejar decimales
                       try:
                               valores.append(s) #convierte la linea en un numero flotante y lo agrega a la lista valores
                       except ValueError:
                               pass
Vmayor=[]
Vmenor=[]
for i in valores:
       if float(i)>5:
              Vmayor.append(i)
       else:
              Vmenor.append(i)
print("Valores mayores a 5:", Vmayor)
print("Valores menores o iguales a 5:", Vmenor)
print(len(Vmayor), "valores mayores a 5")
print(len(Vmenor), "valores menores o iguales a 5")
