elementos=input("Coloque los elementos alfanumericos que desea sumar, separados por un espacio ")
lista=elementos.split(" ")
z=0
m=[]
n=[]
w=[]
k=""
t=[]
for x in lista:
    if (x.isalpha())==True:
        t.append(x)
        for p in t:
            p=str(p)
        k=k+p
        m.append(k)
    else:
        w.append(float(x))
        for q in w:
            q=float(q)
        z=z+q
        n.append(z)

print("su vector numerico es "+ str(w)+" y la suma acumulativa de los elementos es "+str(n))
print("su vector alfabetico es "+ str(t)+" y la suma acumulativa de los elementos es "+str(m))