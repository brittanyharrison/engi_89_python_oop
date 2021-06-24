"""

"""


#  Capital for class name
class Animal:
    # self refers to current class
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breath(self):
        return "dun dun dun dun....Staying alive!,Staying alive"

    def eat(self):
        return "Eat please"

    def move(self):
        return "don't be lazy and MOVE"


# need to create an object in order to use the methods
cat = Animal()
print(cat.alive)
