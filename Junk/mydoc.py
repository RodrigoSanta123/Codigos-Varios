import re
name=input('ingrese nombre del modulo a evaluar ')
__import__(name)
for x in dir(name):
    y=getattr(name, str(x))
    print('\n',x,'\n')
    print(y.__doc__)