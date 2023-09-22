

class Bog:
    def __init__(self,initialPos):
        self.position = initialPos
        self.direction = "right"
    def turn(self):
        if self.direction == "right":
            self.direction = "lift"
        else:
            self.direction = "lift"
    def move(self):
        if self.direction == "right":
            self.position += 1
        else:
            self.position -= 1
    def getPosition(self):
        return self.position

c= Bog(10)
print(c.getPosition())
c.turn()
print(c.getPosition())
c.move()
print(c.getPosition())
