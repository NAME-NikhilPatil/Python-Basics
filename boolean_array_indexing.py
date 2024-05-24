import numpy as np 
 
a = np.array([[1,2], [3,4], [5,6]]) # a rank 2 array of shape (3,2) 
bool_indx = (a > 2)
# Find the elements of a that are bigger than 2; 
# this returns a numpy array of the same shape as a, 
# where each slot of bool_idx tells whether that element # of a is > 2 
print(bool_indx) 
print(a[bool_indx]) 
print(a[a>2]) 
