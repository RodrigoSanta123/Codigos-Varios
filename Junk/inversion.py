k=[]
listado=input("ingrese los caracteres que desea invertir separados por una coma ")
lista=listado.split(",")
n=len(lista)
q=1
for x in lista:
    k.append(float(lista[n-q]))
    q=q+1
print(k)
