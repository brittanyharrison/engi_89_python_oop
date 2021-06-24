"""
Code along
#  pass: keyword allows interpreter to skip
"""


# # Lets create a function
# def greeting():
#     print("Welcome on Board!")
#
#
# greeting()  # function call
#
#
# def greetings():
#     return "Welcome on Board!"  # Alternative
#
#
# print(greetings())


# def greeting_name(name=input("whats your name?")):
#     print(f"Welcome on board {name}")
#
#
# greeting_name()

def add(
        num1 = input(),
        num2 = input()):
    return int(num1) + int(num2)

print(add())