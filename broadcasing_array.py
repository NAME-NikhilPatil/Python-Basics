import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])  # v will be broadcasted to match the shape of x

# Using broadcasting to add v to each row of x
y = x + v
print(y)

# Adding a scalar to all elements of x
z = x + 5
print(z)
