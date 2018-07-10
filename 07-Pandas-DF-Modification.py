import numpy as np
import pandas as pd

# Define Numpy Array
array_1 = np.array([np.arange(10, 14),
                    np.arange(14, 18),
                    np.arange(18, 22)])

# Print Numoy Array
print("NumPy Array is:")
print(array_1)

# Convert it to DataFrame
dataframe_1 = pd.DataFrame(array_1, columns=['Col1', 'Col2', 'Col3', 'Col4'])

# Print DataFrame
print("\n DataFrame is; ")
print(dataframe_1)


# Setting the Index
print("\n Modified DataFrame After Adding the Index:")
print(dataframe_1.set_index('Col1'))


# Adding a Column to DataFrame
to_add = [22, 23, 24]
dataframe_1['Col5'] = to_add

print("\n Modified DataFrame")
print(dataframe_1)

# Add new row to DataFrame
add_row = [25, 26, 27, 28, 29]
dataframe_1.loc[3] = add_row

print("\n Modified DataFrame")
print(dataframe_1)


