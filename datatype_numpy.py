import numpy as np 
 
x = np.array([1, 2]) # Let numpy choose the datatype 
print(x.dtype) 
 
x = np.array([1.0, 2.0]) # Let numpy choose the datatype 
print(x.dtype) 
 
x = np.array([1.0, 2.0], dtype=np.int64) # Force a particular datatype 
print(x.dtype) 
