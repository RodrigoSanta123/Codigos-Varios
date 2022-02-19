filename=input('ingrse el nombre del txt a evaluar ')
def linecount(filename):
    return len(open(filename).readlines())

n=linecount(filename)
f=open(str(filename))
z=f.readlines()
for x in range (n):
    print(z[n-x-1])
