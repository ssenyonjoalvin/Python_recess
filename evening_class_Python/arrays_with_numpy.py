# while using numpy(numerical python)  library for arrays
# numpy is a powerful library for numerical computation tool, it provides support for arrays
# matrices and many mathematical 
# offering more power and flexibility compared to the array module.

# installation command: pip install numpy
# importing numpy : import numpy as np 
import numpy as np

arr = np.array([1,3,5,6,7,8,9])
print(arr)

names = np.array(['Alvin','ethel','whate'])
print(names)

# creating a 2d array 
arr_2d = np.array([[1,2,3,0],[6,7,9,5]])#make sure both the arrays have the same size
print(arr_2d)

# we can find out the dimensions of an array using the ndim property
a = np.array([[[1,2,3],[4,6,5]], [[0,9,8], [9,5,4]]])
print(a.ndim)

# Accessing elements 

b = np.array([12,45,78])
print(b[0])

c = np.array([[23,45,67,89],[56,52,78,44]])
print(c[0,3]) #access element in the first row at the 3 index
print(c[1,2])

d = np.array([[[1,2,3],[4,6,7]],[[0,9,8],[7,1,4]]])
print(d[0,1,1])

names = np.array(['Alvin','ethel','whate'])
print(type(names))

