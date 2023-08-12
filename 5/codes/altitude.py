#1.3.5 Verify that ((A-H)^T)(B-C) = 0
import numpy as np
A = np.array([[1],[-1]])
B = np.array([[-4],[6]])
C = np.array([[-3],[-5]])
H = (1/6)*np.array([[17],[-5]])     #H is orthocentre
V = ((A - H).T) @ (B - C)
print(V) 
