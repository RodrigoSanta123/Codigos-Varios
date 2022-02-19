import re
filename=input('ingrse el nombre del txt a evaluar ')
n=0
p=0
f=open(str(filename))
z=f.readlines()
for x in z:
    t=re.findall('^New Revision: ([0-9.]+)', x)
    if len(t)!=0:
        n=n+1
        p=p+float(t[0])
print(n)
print(p)