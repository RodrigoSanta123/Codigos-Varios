listado=input('ingrese las palabras a evaluar separadas por un espacio ')
lista=listado.split(" ")
c=0
t=[]
m=0
n=0
finale=[]
v=[]
import string
alph=list(string.ascii_lowercase)
k=range(len(alph))
alf={x:y for x in alph for y in k if alph.index(x)==k[y]}
for x in lista:
    c=0
    for y in x:
        c=c+alf[y]
    t.append(c)
comp=dict(zip(lista,t))
print(t)
for x in lista:
    m=m+1
    n=0
    for y in lista:
        n=n+1
        if n!=m and len(x)==len(y) and comp[x]==comp[y] and x not in v:
            v=[x for x in lista if n!=m and len(x)==len(y) and comp[x]==comp[y] and x not in v]
            finale.append(v)
print(finale)
