import numpy as np 
 
x = np.array([[1,2], [3,4]], dtype=np.float64) 
y = np.array([[5,6], [7,8]], dtype=np.float64)  
# Elementwise addition 
print(x + y) 
print(np.add(x,y)) 
 
# Elementwise subtraction 
print(x - y) 
print(np.subtract(x,y)) 
 
# Elementwise multiplication 
print(x * y) 
print(np.multiply(x,y)) 
 
# Elementwise division 
print(x / y) 
print(np.divide(x,y))  
# Elementwise square root
print(np.sqrt(x)) 
