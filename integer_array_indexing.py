import numpy as np 
a = np.array([[1,2], [3,4], [5,6]]) # a rank 2 array with shape (3,2) 
 
print(a[[0,1,2], [0,1,0]]) # Prints 1, 4 and 5 
print(a[0,0], a[1,1], a[2,0]) 
 
print(a[[0,0],[1,1]]) 
