
import numpy as np
import random

#1. Create a 1-dimensional NumPy array with values from 1 to 10.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr)


#  Create a 2-dimensional NumPy array (3x3) with random integers between 0 and 100.

arry = np.random.randint(0,101, size=(3,3))
print(arry)


# 3- Given the 2-dimensional array from question 2, extract the second column
# and store it in a new variable

second_column = arry[:, 1]

print("Second Column:")
print(second_column)
print(arry)


#  4-Create a new 1-dimensional array that contains only the even numbers
# from the array in question 1

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        print(arr[i])
# or another answer

even_numbers = arr[arr % 2 == 0]
print(even_numbers)


# 5-Calculate the dot product of the arrays A and B: A = [1, 2, 3] and B = [4, 5, 6].

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

dot = np.multiply(A, B)
print(dot)


# 6- Create a 1-dimensional array of 100 equally spaced values between 0 and 1
# (inclusive).

s = np.random.random((1, 100))
print(s)


# 7. Given the array [10, 20, 30, 40, 50], add 5 to each element using
# broadcasting.

add = np.array([10,20,30,40,50,60])
addd = add+5
print(addd)

# or another answer
b = np.array([5])
v = add + b
print(v)

# 8. Create a 2-dimensional array (4x4) with values ranging from 1 to 16 and reshape it into a 4x2 array.
# x = np.arange(1, 17).reshape(4, 4)

x = np.arange(1, 17).reshape(4, 4)
# TEST(4,4) is not accepted because the size of TEST is not suitable with the size of the original array
y = x.reshape(8, 2)
print(x)
print(y)

# 9. Calculate the element-wise square root of the array in question 8.

sort = np.sqrt(y)
print(sort)

# 10.Find the index of the maximum value and the index of the minimum value
# in the array from question 8.

maxx = np.max(y)
minn = np.min(y)
print("maximum value is = ", maxx)
print("minimum value is = ", minn)
