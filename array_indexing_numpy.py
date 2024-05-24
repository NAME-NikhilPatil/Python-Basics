import numpy as np  
# Use slicing to pull out the subarray consisting of the first 2 rows 
# and columns 1 and 2. So b will be a 2 x 2 array consisting of following elements: 
#[[2,3], # [6,7]] 
a= np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) 
# create an array of rank 2 and shape (3,4) 
b= a[:2, 1:3] # shape of b = (2,2); [[2,3], [6,7]] 
 
print(a) 
print(a.shape) 
print(b) 
print(b.shape) 
print(a[0,1]) 
# prints 2 
b[0,0] = 45 
print(a[0,1]) 
 
print('a:', a) 
print('b:',b) 
