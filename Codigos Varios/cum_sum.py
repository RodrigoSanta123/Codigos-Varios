import numpy
import pandas as pd
listado=input("ingrese los meses que desea evaluar separados por una coma ")
lista=listado.split(",")
listado=input("ingrese las ventas separadas por una coma ")
lista2=listado.split(",")
lista2=[int(x) for x in lista2]
k=pd.Series(lista2,index=lista)
print(k)
k=k*0.9
print(k)