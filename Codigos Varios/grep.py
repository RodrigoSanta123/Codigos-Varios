filename=input('ingrse el nombre del txt a evaluar ')
N=int(input('ingrese numero de lineas de sesgo '))
try:
    f=open(str(filename))
except:
    print('nombre de archivo no valido')
    exit
z=f.readlines()
try:
    sub = [z[n:n+N] for n in range(0, len(z), N)]
except:
    print('numero ingresado no valido')
print(sub)