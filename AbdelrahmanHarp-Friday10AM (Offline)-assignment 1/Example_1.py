
#  Given a string, write a python program that convert the string based on the following
# conditions:
# • If lower case letter less than upper case letter convert string to upper case
# • If upper case letter less than lower case letter convert string to upper case


x = input("Enter a string: ")

if  (x.isupper()):
    print(x.lower())
elif (x.islower()):
    print(x.upper())
else:
    print(x)

