q=str(input("ingrese las keys (elementos separados por un espacio) "))
w=str(input("ingrese los valores (elementos separados por un espacio) "))
x=q.split(" ")
y=w.split(" ")
t=dict(zip(x,y))
z={k:v for k,v in sorted (t.items(),key=lambda freq:freq[0])}
for x,y in z.items():
    print(x,y)