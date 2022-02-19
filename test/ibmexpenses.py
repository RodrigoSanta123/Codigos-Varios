import pandas as pd
k=pd.DataFrame({
    'Ventas':[30500,35600,28300,33900],
    'Gastos':[22000,23400,18100,20700]},index=['Enero','Febrero','Marzo','Abril'],)
print(k)
print('Ganancias')
print(k['Ventas']-k['Gastos'])