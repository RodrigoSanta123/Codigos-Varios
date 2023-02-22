def mapa(lista,key):
    z=[x for x if key(x)=True]
    print(z)
mapa(range(5),key=lambda x: x%2==0)
