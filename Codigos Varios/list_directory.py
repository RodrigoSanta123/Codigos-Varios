import os
obj=os.scandir('C:/Users/rodri/Documents/')
for x in obj:
    if x.is_file:
        z=(x.name).split(os.extsep)
        print(z)