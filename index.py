# x =int(input('Enter first number '))
# y = int(input("Enter secund number "))
# w = int(input("Enter third number "))
#
# print("vales of sum {} vales of Subtraction {} ".format((x+y),(x-y)) )
# print("vales of multiplicatoin {} vales of Division {} ".format((x*y),(x/y)) )

# a,s,d = 7,8,9


# if x==y and x==w :
#     print("x is = y = w ")
# elif x>y:
#     print("x is Bigger than y")
# elif x > w:
#     print("x is Bigger than w")
# else:
#     print('y and W is bigger than x')
#
# print("Thanks")

# x ="Enter first number "
# y = "Enter secund number "
# w = "Enter third number "


# function for string update

# print(len(x))
# print(len(y))
# print(len(w))
# print(x.split("first"))
# print(x.index("first"))
# print(x.find("i",0,9))
# print(x.replace("first",'your'))
# print(x.lower())
# print(x.upper())
# print(x.capitalize())

# S = "Python is a high-level, general-purpose and very popular programming language. The Python programming language is being used in Web Development,Machine Learning applications, Computer Vision, along with all the cutting-edge technology in the software industry"
#
# print(len(S))
# print(S.split())
# print(S.count("Python",0,len(S)))
# print(S.index("Machine Learning"))
# print(S.find("l",0,255))
# print(S.replace("Machine Learning",'Your Machine Learning'))
# print(S.replace("Python","c++"))
# print(S.lower())
# print(S.upper())
# print(S.capitalize())

# loobing with for and while

# first while

# x=0
# while x<=5:
#     print(x)
#     x= x+1

# sec for loob

# for x in range(10):
#     for n in range(x+1):
#         print("/", end="")
#     print()


sum = 0
for x in range(3,10,2):
    sum += x
    print(sum)

# sum = 0
# for x in range(5, 11, 2):
#     sum += x
#     if sum == 12 :
#         break
# print(sum)

# sum =0
# x =int(input("Enter range num: "))
# for i in range(x+1):
#     print(i)
#     sum +=i
# print(sum)

# loob in string by for loob

# s ="abcdefgh"
# for i in range(len(s)):
#     if s[i]=="a" or s[i]=="u":
#         print("ok a not u")
#
# for i in s:
#     if i=="x" or i=="u":
#         print("ok a not u")
#

# word = input("Enter any word: ")
# sum = 0
# for i in word:
#     if i == "o" or i == "u" or i == "y" or i == "e":
#          sum += 1
# print(sum)

# word = input("Enter any word: ")
# sum = 0
# vawels = "aeiou"
# for i in word:
#     if i in vawels:
#          sum += 1
# print(sum)

# word = input("Enter any word: ")
# if word==word[::-1]:
#     print("true")
# else:
#     print("false")




# **************************************************************************************
#
# session_2
#
# Functions
#
# def is_even(i):
#     print("the number is even ")
#     return i%2 ==0
# print(is_even(1))
#
# def  f(x):
#     x=x+1
#     print("X=",x)
#     return x
# x=3
# print(f(x))
# print(x)


# def is_even():
#     print("the number is even ")
#
# is_even()
#
# def function_y(b):
#     print("inside function ",b)
#     return b
# # # print(function_y(5))
#
# def fun_c(z):
#     print("inside function c")
#     return z
# print(fun_c(function_y(5))# )

# def function_x(y):
#     if y % 2 == 0:
#         print("number in function is even ",y)
#     else:
#         print("This num is odd")
#     return y
# i=int(input("enter"))
# function_x(i)


# def fun_x(d,y):
#     print(d+y)
#     print(d-y)
#     print(d*y)
#     print(d/y)
#     return d,y
#
# d= int(input("enter: "))
# y= int(input("enter: "))
# fun_x(d,y)
#


# x=3
# y=5

# tamp =x
# x=y

# y=tamp
# or
# (x,y)=(y,x)

# print(x,y)


# list

# l= [1,2,3,4,5]
# l[1]=5
# print(l)

# for i in l:
#     print(i)
#     i+=1

# l.append(7)
# print(l)
# l.pop()
# print(l)
# l.remove(4)
# print(l)
# del(l[2])
# print(l)

# l.insert(1,3)
# print(l)


# s = "walecom to Ai coures"
# list=list(s)
# a= ' '.join(list)
# print(a)
# print(len(s))
# e=str(s)
# print(e)
# print(e.split("to"))

# print("58",not in l)
# print(l*3)


# l =[0,1,2,3,4,5,6,7,8,9]
# print(l)
# print(l[0:10:2])
# print(l[1:10:2])

# def split(l):
#     even_1= []
#     odd_1= []
#     for i in l:
#       if  i % 2 == 0:
#           even_1.append(i)
#       else:
#           odd_1.append(i)
#     print(even_1)
#     print(odd_1)
# l =[0,1,2,3,4,5,6,7,8,9]
# split(l)


# cobe list if chenge any thing in lis two list oun no apend in
# l1= [1,3,2,4]
# l2 =l1[:]
# print(l2)


# sort تارتيب list
# l1.sort()
# print(l1)


# Dictionary

Dict = {"ann":"b","john":"a","ali":"c"}
# # print(Dict)
# print(Dict)

# keys = ["a","b","c"]
# values = [1,2,3]
# tuples = [(keys,values)
#             for i, (keys,values) in enumerate(zip(keys,values))]
# resilt=

# # add data in dictionary
# Dict["Abdo"]= "R"
# print(Dict)
# # delete data in dictionary
# del(Dict['ann'])
# print(Dict)
# # show data in dictionary
# print('Abdo' in Dict)
# # show All Keys in Dictionary
# print(Dict.keys())
# # show All values in Dictionary
# print(Dict.values())

# class_list=[["mohammed",18,3.00],["yara",19,4.00],["omer",18,3.75]]
#
# print(class_list)
# class_list.append(["mohsen",20,2.5])
# print(class_list)
# class_list[2].append("pass")
# print(class_list)
# class_list.sort()
# print(class_list)
# print(class_list[0])
# print(f"GPA for omar is {class_list[2][2]}")
# print(f"Age for mohsen is {class_list[1][1]}")
# print(f"Name is {class_list[3][0]}")


# dict_data ={
#     "brand":"ford",
#     "model":"Mustang",
#     "year":1964
# }
# print(dict_data)
# dict_data["color"]="red"
# print(dict_data)
# del(dict_data["brand"])
# print(dict_data)
# print(dict_data["model"])
# print(dict_data)
# dict_data["year"]=2020
# print(dict_data)
# dict_data.pop("model")
# print(dict_data)
# dict_data ={
#     "BMW" : {
#     "brand":"BMW","color":"green","year":2020,"model":"340i"
#     },
#     "ford":{
#         "brand":"ford"
#     }
# }
# print(dict_data)
#
# dict_data.clear()
# print(dict_data)
