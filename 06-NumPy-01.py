import numpy as np

# One Dimensional Array
numpy_array = np.array([1, 2, 3])

print (numpy_array)

# Two Dimensional Array

numpy_array = np.array([
                        [1, 2, 3],
                        [4, 5, 6]
                        ])

print(numpy_array)

# Data Type of NumPy Arrays

print("Data Type of NumPy Array:", numpy_array.dtype)


# Create Array with Explicit Data Type
explicit_datatype = np.array((np.arange(5)), dtype=np.int32)

print("\nExplicit Data Array:")
print(explicit_datatype)

print("Data Type:", explicit_datatype.dtype)

# Create an Array of One
one_array = np.ones((3, 5))
print("\nArray of One's")
print(one_array)


# Create an Array of Zeros
zero_array = np.zeros((3,5))
print("\nArray of Zero's")
print(zero_array)

# Create an Array using arange
arange_array = np.arange(3, 10)
print("Arrange Array")
print(arange_array)


# Create an Evenly spaced Array using arange
evenly_spaced_array = np.arange(3, 10, 3)
print("Evenly Spaced Arranged Array")
print(evenly_spaced_array)


# Joining Two Arrays Horizontally
array_1 = np.arange(8).reshape(2, 4)
array_2 = np.arange(4).reshape(2, 2)

print(array_1)
print(array_2)

array_3 = np.hstack((array_1, array_2))

print("\nJoining Array_1 and Array_2:")
print(array_3)
print("\n")

# Joining Two Arrays Vertically
array_1 = np.arange(8).reshape(2, 4)
array_2 = np.arange(4).reshape(1, 4)

array_3 = np.vstack((array_1, array_2))

print(array_1)
print(array_2)
print("\nJoining Array_1 and Array_2 Vertically:")
print(array_3)

