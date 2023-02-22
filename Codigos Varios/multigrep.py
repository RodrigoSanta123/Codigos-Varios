listado=input("ingrese los archivos que desea evaluar separados por un espacio ")
files=listado.split(" ")
def readfiles(files):
    for f in files:
        for line in open(f):
            yield line
def grep(lines):
    return(line for line in lines if len(line)>45)
def printlines(lines):
    for line in lines:
        print (line)

lines=readfiles(files)
lines=(grep(lines))
printlines(lines)
