import os
for path,dirs,files in os.walk('C:/Users/rodri/Documents/BioWare'):
    for file in files:
        print(os.path.abspath(os.path.join(path, file)))