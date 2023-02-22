filename=input('ingrse el nombre del txt a evaluar ')
def linecount(filename):
    return len(open(filename).readlines())

n=linecount(filename)
f=open(str(filename))
z=f.readlines()
for x in z [0:10]:
    print(x)
for x in z[n-10:n]:
    print(x)