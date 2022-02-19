import numpy as np
import pandas as pd
notas={'Agustin':1,"Pedro":5,'Ronaldo':7}
arr=np.array(list(notas.values()))
print(np.min(arr))
print(pd.Series([np.min(arr),np.max(arr),np.std(arr)],index=['Min','Max','Std']))