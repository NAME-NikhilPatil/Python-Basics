import numpy as np 
a	= np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]]) # a rank 2 array of shape (4,3) 
print(a)  
# Create an array of indices 
b	= np.array([0, 2, 0, 1]) 
 
print(a[np.arange(4),b]) # prints [1,6,7,11] 
 
a[np.arange(4),b] += 10 
print(a) 
