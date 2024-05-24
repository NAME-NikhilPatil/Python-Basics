import numpy as np  
# matrices 
x = np.array([[1,2], [3,4]]) 
y = np.array([[5,6], [7,8]])  
# vectors 
v = np.array([9,10]) 
w = np.array([11,12])  
# Inner product of two vectors 
print(v.dot(w)) # method 1 
print(np.dot(v,w)) # method 2  
# Matrix/vector multiplication 
print(x.dot(v)) # shape ?? 
print(np.dot(x,v))  
# Matrix/Matric multiplication 
print(x.dot(y)) 
print(np.dot(x,y)) 
