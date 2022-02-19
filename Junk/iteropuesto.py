listado=input("ingrese los caracteres que desea evaluar separados por un espacio ")
lista=listado.split(" ")
n=len(lista)
k=0
r=lista
for x in r:
    r[k]=lista[(n-k-1)]
    k=k+1
    lista=listado.split(" ")
i=iter(r)
while True:
    try:
        print(i.__next__())
    except:
        break