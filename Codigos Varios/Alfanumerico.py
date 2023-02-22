elementos=input("Coloque los elementos a multiplicar, separados por un espacio ")
lista=elementos.split(" ")
k=1
for x in lista:
    k=k*float(x)
print("el resultado de su multiplicacion es "+ str(k))