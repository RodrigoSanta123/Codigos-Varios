#lensort
particion=[]
listado=str(input("ingrese los caracteres que desea evaluar separados por un espacio "))
lista=listado.split(" ")
for x in lista:
    z=x.split(".")
    particion.append(z)
particion.sort(key=lambda x: x[1])
k=0
for x in particion:
    for y in x:
        y=str(y)
    particion[k]=str(".".join(x))
    k=k+1
print(particion)