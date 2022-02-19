iterar=input('ingrese el iterador ')
try:
    iterador=(eval(iterar))
    k=list(iterador)
except:
    k=list(iterar)
counter=range(len(k))
f=dict(zip(counter,k))
finale=iter(f.items())
for x,y in list(finale):
    print(x,y)