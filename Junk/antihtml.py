import urllib.request
import re
a=input('ingrese el url a guardar ')
b=input('ingrese nombre de guardado ')
urllib.request.urlretrieve(a,b)
f=open(str(b),errors='ignore')
z=f.readlines()
for x in z:
        x=x.rstrip('\n')
        if '<' in x or '[' in x:
                p=re.sub(r'<.*?>','',x)
                t=re.sub(r'\[.*?\]','',p)
                print(t)
        else:
                print(x)
