iterar=input('ingrese el iterador ')
try:
    iterador=(eval(iterar))
    k=list(iterador)
except:
    k=list(iterar)
iterar=input('ingrese el iterador ')
try:
    iterador=(eval(iterar))
    c=list(iterador)
except:
    c=list(iterar)
f=dict(zip(k,c))
finale=iter(f.items())
for x,y in list(finale):
    print(x,y)