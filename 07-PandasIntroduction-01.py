import numpy as np
import pandas as pd

array_1 = np.array([np.arange(10, 15), np.arange(15, 20)])

dataframe_1 = pd.DataFrame(array_1)

print("Value of Array_1: \n", array_1)
print("\nValue of DataFrame_1: \n", dataframe_1)
