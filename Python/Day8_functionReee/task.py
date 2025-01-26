# def greet():
#     print("hi")
#     print("hoho")
#     print("kkkk")
#
# greet()
#
# # Function that allow inputs
# def greet_my_name(who):
#     print(f"What's your name?")
#     print(input(f"my name is {who}"))
#
#
# greet_my_name("ho")
#
#
def greet_with(name, location):
    print(f"Hello my name is {name} ")
    print(f"I live in {location}")

name = input("What's your name?")
location = input("Where are you live?")

greet_with(name, location)