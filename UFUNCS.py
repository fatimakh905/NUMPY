import numpy as np

arr=np.array([2,3,4,56,7])
br=np.array([3,5,8,9,7])

#Universal functions for element_wise operations


print("Addition:",np.add(arr,br))
print("Subtarction",np.subtract(arr,br))
print("Multiplication",np.multiply(arr,br))
print("Division",np.divide(arr,br))
print("Remainder",np.mod(arr,br))    #mod and remainder are used fo same purpose
print("Power",np.power(arr,br))
#The divmod() function return both the quotient and the mod. The return value is 
#two arrays, the first array contains the quotient and second array contains the mod.
print("Quotient and Remainder:",np.divmod(arr,br))
#Absolute values refer to the non-negative magnitude of a number, disregarding its sign.
#Both the absolute() and the abs() functions do the same absolute operation element-wise
#but we should use absolute() to avoid confusion with python's inbuilt math.abs()
a=np.array([-2,-5,-7,4,-6])
print("Absolute values",np.absolute(a))

#Arithmetic Conditionally: means that we can define conditions where the arithmetic operation should happen.
#All of the discussed arithmetic functions take a where parameter in which we can specify that condition.