import numpy as np 
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) 
 
row_r1 = a[1, :] # Rank 1 view of the second row of a 
print(row_r1, row_r1.shape) 
 
row_r2 = a[1:2, :] # Rank 2 view of the second row of a 
print(row_r2, row_r2.shape)  
# We can make the same distinctions when accessing columns of an array 
col_r1 = a[:, 1] 
col_r2 = a[:, 1:2] 
 
print(col_r1, col_r1.shape) 
print(col_r2, col_r2.shape) 
