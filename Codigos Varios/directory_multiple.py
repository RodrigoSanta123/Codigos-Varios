import os
n=[]
a=[]
b=[]
c=[]
obj=os.scandir('C:/Users/rodri/Documents/')
for x in obj:
    if x.is_file():
        n.append(x.name)
        status=os.stat('C:/Users/rodri/Documents/'+str(x.name))
        b.append(status)

for x in b:
    for y in x:
        c.append(y)
a=c[6::10]
b=c[8::10]
c=zip(n,a,b)
print(n)
for x in c:
    print(x)