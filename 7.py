# class Animal:
#     animal_type_count = 0
#     title_zoo = 'Zoo'
#     animal_type: str
#
#     def __init__(self, animal_type):
#         self.animal_type = animal_type
#
#     @classmethod
#     def add_1_animal(cls):
#         cls.animal_type_count += 1
#         print('Животное добавлено')
#
# lion = Animal('Lion')
# Animal.add_1_animal()
#
# print(lion.animal_type, lion.title_zoo)
# print(Animal.animal_type_count)

# class Calc:
#
#     @staticmethod
#     def sloz(x, y):
#         return x + y
#
#     @staticmethod
#     def wych(x, y):
#         return x - y
#
#     @staticmethod
#     def umn(x, y):
#         return x * y
#
#     @staticmethod
#     def delen(x, y):
#         return x / y
#
# print(Calc.sloz(1, 4))
# print(Calc.wych(73, 3))
# print(Calc.umn(5, 5))
# print(Calc.delen(10, 2))

# class User:
#     skills = 'Python'
#     name: str
#     age: int
#
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
# user1 = User('Vitali', 27)
# print(user1.name, user1.age, user1.skills)

