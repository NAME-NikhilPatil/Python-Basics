# differentiating between rank 1 and rank 2 numpy arrays
import numpy as np 
 
a = np.array([1,2,3,4,5,6]) 
# rank 1 array 
b = np.array([[1,2,3,4,5,6]]) 
# rank 2 array 
 
print('a.shape = ', a.shape, ' a.ndim = ', a.ndim) 
print('b.shape = ', b.shape, ' b.ndim = ', b.ndim) 
