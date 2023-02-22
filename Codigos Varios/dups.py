#unique
k=[]
q=[]
listado=input("ingrese los caracteres que desea evaluar separados por una coma ")
lista=listado.split(",")
for x in lista:
    if x not in k:
        k.append(x) 
print(k)