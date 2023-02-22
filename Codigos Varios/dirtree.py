import os
d='C:/Users/rodri/Documents/BioWare'
def dirtree(d,n):
    n=n+1
    k=os.listdir(d)
    for x in k:
        if os.path.isdir(str(d)+'/'+str(x))==True:
            print('|'+'--'*n+str(x))
            dirtree(str(d)+'/'+str(x),n)
        else:
            print ('--'*n+'>'+str(x))
print(dirtree(d,0))