import numpy as np 
 
a	= np.array([1,2,3]) 
# create a rank 1 array 
print(a) 
print(type(a)) 
print(a.shape) 
print(a.ndim) 
# rank or number of dimensions 
print(a[0], a[1], a[2]) 
a[0] = 5 
print(a) 
