import this


#
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# dog = Animal("con cho", 22)
# print(dog.name)
# print(dog.age)
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name}({self.age})"
#
#
# p1 = Person("John", 36)
#
# print(p1)
#
#
# def test(a, b):
#     a + b
#
#
# y = test(3, 5)
# print(y)


class Person:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def __init__(self, age):
        self.age = age

    def __abs__(self):
        return abs(self.age)


son = Person(-22)
print(abs(son))
