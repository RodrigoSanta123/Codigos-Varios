import os
for path,dirs,files in os.walk('C:/Users/rodri/Documents/BioWare'):
    vec=path.split(os.sep)
    print('|',(len(vec)-1)*'--',os.path.basename(path))
    for file in files:
        print((len(vec))*'--','>',file)