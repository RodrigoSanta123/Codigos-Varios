k=0
listado=input("ingrese los caracteres que desea evaluar separados por una coma ")
lista=listado.split(",")
m=(float(lista[0])+1)
for x in lista:
    if float(x)<m:
        k=float(x)
        m=float(x)
print(k)
