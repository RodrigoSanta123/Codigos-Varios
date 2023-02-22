def mejorado(lista,key):
    k=[]
    for x in lista:
        x=str(x)
        x=key(x)
        if x not in k:
            k.append(x)
    print("La lista eliminando los duplicados es "+ str((k)))
mejorado(['Python', 'python', 'Ruku', 'rUku', 6, 6],key=lambda x: x.lower())