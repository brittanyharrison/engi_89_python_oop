from reptile import Reptile

"""

"""


class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    def use_tongue_to_smell(self):
        return "You can smell with your tongue. SUPER WEIRD, but ok?"


smart_snake = Snake()
print(smart_snake.forked_tongue)
