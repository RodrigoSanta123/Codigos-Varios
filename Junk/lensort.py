#lensort
particion=[]
listado=str(input("ingrese los caracteres que desea evaluar separados por un espacio "))
lista=listado.split(" ")
for x in lista:
    z=x.split(".")
    particion.append(z)
for x in particion:
    particion.sort(key=lambda x: x[1])    
    sum(str(x))
print(particion)