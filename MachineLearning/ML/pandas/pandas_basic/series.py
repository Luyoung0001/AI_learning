import pandas as pd
import numpy as np

pd.Series(data=None, index=None, dtype=None)

arr = pd.Series(np.arange(10))
print(arr)

arr = pd.Series([1,2,3,4,5,6,7],index=[11,22,33,44,55,66,77])
print(arr)

print(arr.index)
print(arr.values)
print(arr[55])