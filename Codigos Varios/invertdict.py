q=str(input("ingrese las keys (elementos separados por un espacio) "))
w=str(input("ingrese los valores (elementos separados por un espacio) "))
x=q.split(" ")
y=w.split(" ")
t=dict(zip(y,x))
for x,y in t.items():
    print(x,y)