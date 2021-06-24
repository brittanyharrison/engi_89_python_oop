from snake import Snake
"""
"""
class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True

    def digest_large_prey(self):
        return"YUM YUM i digest like a boss"

    def climb(self):
        return "Climb the tree"
    # to hide data(__)
    def __shed_skin(self):
        return "Don't look at me, Im shedding!"

fast_python = Python()
print(fast_python.two_lungs)