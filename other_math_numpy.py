import numpy as np 
 
x = np.array([[1,2], [3,4]]) 
print(np.sum(x)) 
print(np.sum(x, axis=0)) 
# add elements in each column 
print(np.sum(x, axis=1))
# add elements in each row 
