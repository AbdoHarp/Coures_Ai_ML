
# 1 • Write a program to determine if a year is a leap year or not.

# make input for users Write year

# year = int(input("Plz Enter year do you no leep or not: "))
#
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f"{year} is leep year")
# else:
#     print(f"{year} is not leep year")
#

# 2 • Write a program to find the largest of three numbers entered by the user.

# num1 = float(input("Plz Enter Your first number: "))
# num2 = float(input("Plz Enter Your second  number: "))
# num3 = float(input("Plz Enter Your third number: "))
#
# if (num1 > num2) and (num1 > num3):
#     largest = num1
# elif (num2 > num1) and (num2 > num3):
#     largest = num2
# else:
#     largest = num3
#
# print(f"{largest} this is largest number input with user")


# 3 • Write a program to calculate the factorial of a number.

# num = int(input("Plz Enter Your number: "))
# factorial=1
# if num < 0:
#     print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1 , num + 1):
#         factorial = factorial * i
#     print(f" The factorial of {num} is {factorial}")



# 4 • Write a program to find the sum of all numbers in a given list.

# lst = []
#
# # number of elements as input
# n = int(input("Enter number of elements : "))
#
# # iterating till the range
# for i in range(0, n):
#     ele = int(input("Enter Your Numbers: "))
#     # adding the element
#     lst.append(ele)
#
# total= 0
# # lst= [11, 5, 17, 18, 23]
#
# for i in range(0,len(lst)):
#     total = total+lst[i]
# print(f"Sum of all elements in given list: {total}")


# 5 • Write a function to calculate the area of a circle given its radius.

# from math import pi
#
#
# Radius = float(input("Input the radius of the circle = "))
# print("The area of the circle with radius " ,Radius, " is: " ,pi * Radius**2)



# 6 • Write a function to find the maximum element in a list.

def find_max(lst):
    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element
# my_list = [1,2,3,4,6,10,15,48,16]
lst = []
#
# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input("Enter Your Numbers: "))
    # adding the element
    lst.append(ele)
print(find_max(lst))
