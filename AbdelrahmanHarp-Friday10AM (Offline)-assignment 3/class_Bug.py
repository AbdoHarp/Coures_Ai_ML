#
#
class Bug:
   def __init__(self, initialPos):
       self.position = initialPos
       self.direction = "right"
   def turn(self):
       if self.direction == "right":
           self.direction = "left"
       else:
           self.direction = "right"
   def move(self):
       if self.direction == "right":
           self.position += 1
       else:
           self.position -= 1
   def getPosition(self):
       return self.position

# ===================================== Another solution to the code ========================================

# class Bug:
#     def __init__(self, initial_position):
#         self.position = initial_position
#         self.direction = 1  # 1 for right, -1 for left
#
#     def turn(self):
#         self.direction *= -1  # Change direction
#
#     def move(self):
#         self.position += self.direction
#
#     def getPosition(self):
#         return self.position
#
bugsy = Bug(float(input("Enter your Number = ")))
print("Initial position:", bugsy.getPosition())  # Expected output: 10

bugsy.move()
print("New position:", bugsy.getPosition())  # Expected output: 11

bugsy.turn()
bugsy.move()
print("New position:", bugsy.getPosition())  # Expected output: 10