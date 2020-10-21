import pandas as pd
import numpy as np
ser = pd.Series()
print(ser)
data = np.array(['g','e','e','k','s'])
ser = pd.Series(data)
print(ser)

df = pd.DataFrame()
lst = ['Geeks','for','geeks','is','portal','for','geeks']
df = pd.DataFrame(lst)
print(df)

