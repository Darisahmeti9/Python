class MyClass:
    def __init__(self):
        self._producted_variable = "This is a private variable"

    def _producted_method(self):
        print("This is a producted method")


my_class = MyClass()

print(my_class._producted_variable)
print(my_class._producted_nethod())