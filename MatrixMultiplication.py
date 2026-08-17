import numpy as np
a=np.array([[3,5],[3,5]])
b=np.array([[2,8,7],[9,4,6]])
#Matrix Multiplication
print("Matrix multiplication:",np.dot(a,b))
#For matrix multiplication,no of coulmns in first matrix=no.of rows in 2nd matrix

        #Or
print(a@b)
print(a.dot(b))
