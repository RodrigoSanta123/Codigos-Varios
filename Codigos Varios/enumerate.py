listado=input("ingrese los caracteres que desea evaluar separados por un espacio ")
lista=listado.split(" ")
z=[(x,y) for x in lista for y in range(len(lista)) if y==lista.index(x)]
for x,y in z:
    print(x,y)