num=input('ingrese el numero a evaluar: ')
ma=None
mi=None
k=0
n=0
while str(num)!='fin':
    if ma is None or float(num)>ma:
        ma=float(num)
    if mi is None or float(num)<mi:
        mi=float(num)
    k=k+float(num)
    n=n+1
    num=input('ingrese el numero a evaluar: ')
print('La media es '+str(k/n))
print('El maximo es '+str(ma))
print('El minimo es '+str(mi))