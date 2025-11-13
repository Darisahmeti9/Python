# def greet():
#     print("Hello World")
#
# greet()
#
# def greet_person(name):
#     print("Hello",name)
#
# greet_person("Daris")
# greet_person("Ahmeti")
#
#
#
# def greet(name):
#     message=f"Hello,{name}"
#     print(message)
#
# greet("Alice")
# print(message)
#
# greeting="Hello"
#
# def greek(name):
#     message=f"{greeting},{name}"
#     print(message)
#
# greek("Bob")
# print(greeting)
#
# greeting="Hello"
#
#
# def greek():
#     global greeting
#     greeting="Goodbay"
#     name="Daris"
#
#     message=f"{greeting},{name}"
#
#     print(message)
#
# greek()
# print(greeting)

def greet_person(name,greeting="Hello"):
    message=f"{greeting},{name}"
    return message

print(greet_person("Daris"))
print(greet_person("Ahmeti","Hi"))