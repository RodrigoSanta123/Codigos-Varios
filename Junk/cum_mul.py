listado=input("ingrese los caracteres que desea evaluar separados por una coma ")
lista=listado.split(",")
k=[]
q=1
for x in lista:
    q=q*float(x)
    k.append(q)
print(k)
