import os
obj=os.scandir('C:/Users/rodri/Documents/')
k=[]
t=[]
for x in obj:
    if x.is_file():
        z=(x.name).split(os.extsep)
        k.append(z[1])
for x in k:
    if x not in t:
        t.append(x)
counter=[k.count(str(x)) for x in t]
finale=dict(zip(t,counter))
for x,y in finale.items():
    print (x,y)