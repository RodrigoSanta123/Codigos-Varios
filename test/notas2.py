import pandas as pd
notas={'Agustin':4,"Pedro":8,'Ronaldo':9}
obj=pd.Series(list(notas.values()),index=(list(notas.keys())))
print(obj[obj>=4].sort_values(ascending=False))
