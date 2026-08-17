import numpy as np

a=np.array([[3,1],[3,5]])
b=np.array([[2,4],[9,4]])

c=a+b                    #Sum operation (Arrays support element wise operation but python lists do not )
print("Sum of two arrays",c)           #Number of elements of both arrays should be same
print("Subtraction:",a-b)
print("Multiplication:",a*b)     #Element wise multiplication
print("Division:",a/b)
print("Modulus:",a%b)
print("Floor Division:",a//b)              #It remove decimal value from result and print integer only
print("Exponentiation:",a**b)                   