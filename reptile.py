# If not in the same dir you need to give absolute path
from animal import Animal

"""
Code along 
"""


# Create a reptile class to inherit animal
class Reptile(Animal):
    def __init__(self):
        # super() inherits from parent class
        super().__init__()
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chamber = [3, 4]

    def seek_heat(self):
        return "oh nooo, Look for the sun!"

    def hunt(self):
        return "Bet youre hungry, go hunt!"

    def use_venom(self):
        return "DANGER, Hit em' with the venom!"

# create an object of the reptile class
smart_reptile = Reptile()
print(smart_reptile.eyes)
