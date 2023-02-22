#esto esta para probar
import os
import re
t=[]
n=0
m=0
for path,dirs,files in os.walk('C:/Users/rodri/Documents/Python'):
    for f in files:
        if re.search(r'.+\.py',f):
            for line in open(f):
                if line!='\n':
                    n=n+1
                if re.search('^#',line):
                    m=m+1
print('Hay '+str(n-m)+' lineas en la carpeta destino')