def filtro(lista,key):
    z=[x for x in lista if key(x)==True]
    print(z)
filtro(range(5),key=lambda x: x%2==0)
