import numpy as np
import pandas as pd

index = ['Row1', 'Row2', 'Row3']
columns = ['Col1', 'Col2', 'Col3', 'Col4']

array_1 = np.array([
    (np.arange(11, 15)),
    (np.arange(15, 19)),
    (np.arange(19, 23))])


print("Value of Array_1: \n", array_1)

dataframe_1 = pd.DataFrame(data=array_1, index=index, columns=columns)

print("\nValue of DataFrame_1 is: \n", dataframe_1)

print(dataframe_1.shape)
print(len(dataframe_1.index))


