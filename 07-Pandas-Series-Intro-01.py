import  numpy as np
import pandas as pd

array_1 = np.array(np.arange(10, 15))

pd_series_1 = pd.Series(array_1)

print(pd_series_1)

# Series with Index in Pandas Series

indexes = ['a', 'b', 'c', 'd', 'e']
array_2 = np.array(np.arange(15, 20))

pd_series_2 = pd.Series(array_2, index=indexes)

print(pd_series_2)
