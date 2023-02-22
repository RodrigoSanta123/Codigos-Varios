from math import pi
print("Por favor ingrese radio del circulo")
r=float(input())
if r>0:
    a=pi*r**2
    print("El radio del circulo es "+str(a))
else:
    print("El Radio ingresado no es valido,por favor reingrese el valor")
    r=float(input())
    while r<=0:
        print ("El Radio ingresado no es valido,por favor reingrese el valor")
        r=float(input())     
a=pi*r**2
print("El radio del circulo es "+str(a))