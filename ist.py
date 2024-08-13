import numpy as np
a = np.array([[1, 2, 3, 13], 
              [4, 5, 6, 14], 
              [7, 8, 9, 15], 
              [10, 11, 12, 16]]) 
  
b = np.array([10, 20, 30, 40]) 
  
print("Matrix a =", a) 
print("Matrix b =", b) 
print("Product of a and b =",np.matmul(a, b))