import numpy as np 
a	= np.zeros((2,3)) # create an array of all zeros 
print(a) 
 
b	= np.ones((1,2)) # create an array of all ones 
print(b) 
print(b.shape) 
c = np.full((2,2), 7) # create an array of constants 
print(c) 
 
d = np.eye(3) # create a 3 x 3 identity matrix 
print(d) 
 
e = np.random.random((2,2)) # create an array filled with random values 
print(e) 
