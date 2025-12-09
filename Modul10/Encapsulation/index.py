class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name

    def get_name(self,name):
        self.__name=name

    def get_age(self):
        return  self.__age

    def get_age(self,age):
        self.__age=age

student1=Student("Daris",15)

print("Name:",student_1.get_name())

student1.set_name("Ahmeti")
print("Name:",student1.get_name())

print("Age:",student1.get_age())
student1.set_age(16)
print("Age:",student1.get_age())
