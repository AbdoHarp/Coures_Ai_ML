# class coordinates():
#     def __init__(self,x,y):
#         self.x =x
#         self.y =y
#
# c = coordinates(3,4)
#
# print(c.x)
# print(c.y)



# class bank_account():
#     def __init__(self, account_number,balance):
#         self.account_number =account_number
#         self.balance = balance
#         self.rate =0.5
#     def __bank(self):
#         return f"Account Number = {self.account_number}, balance = {self.balance}"
#     def store(self):
#         return f"Your Account number saved successfuly"
#
# obj = bank_account(4444444,4444)
# print(obj)

# class



# class humen:
#     def __init__(self, name, age):
#         self.name= name
#         self.age =age
#         print("Hello")
# orj = humen("Abdo",22)
# print(orj.name,orj.age)

# class parson:
#     def __init__(self,age,name):
#         self.age = age
#         self.name =name
# #
# #     def __init__(self, age):
# #             self.age = age
#     def __str__(self):
#         return f"{self.name}({self.age})"
# #
# h1= parson(22,"abdo")
# print(h1)
# int
# class data:
#     def __int__(self):
#         return 30
# x= data()
# res = int(x)
# print(res)
# # float
# class data:
#     def __float__(self):
#         return 30.0
# x= data()
# res = float(x)
# print(res)


# class parson:
#     def __init__(self,name,phone):
#         self.name   = name
#         self.phone = phone
#     def my_date(self):
#         return "Hello " + self.name + " Your phone " + self.phone
# h1 = parson("Abdo", "01010968854")
# print(h1.my_date())

# class bank_account:
#     def __init__(self):
#         self.balanse =0
#         print("Hello welecom to your Account")
#     def deposit(self):
#         amount  = float(input("Enter to amount to deposit "))
#         self.balanse+= amount
#         print ("the amount deposited = ",amount )
#     def withdraw(self):
#         amount = float(input("Enter the amount to withdraw "))
#         if self.balanse>= amount:
#             self.balanse -= amount
#             print("the amount withdraw = ", amount)
#         else:
#             print( "Your balance is insufficient , try agein ")
#     def display(self):
#         print("the final balanse",self.balanse)
#
# c =bank_account()
# c.deposit()
# c.withdraw()
# c.display()


# class person:
#     def __init__(self,name,age):
#         self.age= age
#         self.name = name
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def set_name(self,new_name):
#         self.name =new_name
#     def set_age(self,new_age):
#         self.age = new_age
#
# c =person("abdo",22)
# print(f"Your name is  {c.name}  and age age  { c.age}")
#
# c.set_name("ahmed")
# print(c.get_name())
# c.set_age(25)
# print(c.get_age())


# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def set_name(self,newname):
#         self.name= newname
#     def  get_name(self):
#         return self.name
#     def set_age(self,newage):
#         self.age = newage
#     def get_age(self):
#         return self.age
#     def __str__(self):
#         return "Hello " + self.name + " Your age " + self.age
#
# class cat(Animal):
#     def speak(self):
#         print("meow")
#     def __str__(self):
#         return "cat name is  " + self.name + " and age " + self.age
#
#
# c = Animal("abdo",22)
# print(f"Your name is  {c.name}  and age age  { c.age}")
#
# c.set_name("ahmad")
# print(c.get_name())
#
# s = cat("cat",3)
# c.set_age(4)
# print(c.get_age())
# s.speak()


class customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def set_name(self,newname):
        self.name = newname
    def set_age(self,newage):
        self.age = newage
    def get_name(self,):
        return self.name
    def get_age(self,):
        return self.age

user_data = customer("abdo", 22)
print(user_data.name, (user_data.age))

class MainBikeRental:
    def __init__(self):
        self.list_bikes = []
        self.list_rental = []
    def get_bikes(self):
        return self.list_bikes
    def get_rental(self):
        return self.list_rental
    def set_bikes(self, value):
        self.list_bikes.append(value)
    def set_rental(self,  value):
        self.list_rental.append(value)

    def requestBikes(self, number_of_bikes, user_data):
        if user_data.age > 6:
            if len(self.list_bikes) >= number_of_bikes:
                for i in range(number_of_bikes):
                    self.list_bikes.pop()
                    self.set_rental(user_data)
            else:
                print("plz wait 10 minutes")

        else:
            print("You cant rent a bikes")
    def returnBike(self, rental_time, num_of_bikes):
        cost = rental_time * 40 * num_of_bikes
        for i in range(num_of_bikes):
            bike = bike("bike1", 250)
            self.set_bikes(bike)
        return cost
    def totalCost(self):
        total = 0
        for i in self.list_bikes:
            total += i.get_price()
        return total

b1 = MainBikeRental()
b1.requestBikes(5, user_data)

class bike:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def set_name(self, newName):
        self.name = newName
    def set_price(self, newPrice):
        self.price = newPrice
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
# bike1 =
pr = bike("b1", 5)
pr.set_price(5)
class electricBike(bike):
    def __init__(self, name, price, maxSpead):
        super(electricBike, self).__init__(name, price)
        self.maxSpead = maxSpead

        def set_maxspead(self, newspead):
            self.name = newspead

        def get_maxspead(self):
            return maxSpead


b = electricBike("e", 550, 2000)
print(b.name)

b1.set_bikes(7)
print(b1.totalCost())
