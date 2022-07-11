"==================Инкапсуляция======================="
#  Инкапсуляция - принцип ООП
# 1. Сокрытие данных (ограничение доступа к определенным методам и классам)
# 2. Сбор всех необходимых для класса методов и аттрибутов в "капсулу" (класс)

"===================Модификаторы доступа к аттрибутам==============="
# 1. public (публичный)
# 2. pritected(защищенный)
# 3. privat(приватный)
class A():
    attr1 = "публичный"
    _attr2 = "защищенный"
    __attr3 = "приватный"

A.attr1 # "публичный"
A._attr2 # "защищенный"
# A.__attr3 # AttributeError: type object 'A' has no attribute '__attr3'
# A._A__attr3 # "приватный"  


"===============getters / setters==============="
class Person:
    def __init__(self,name, age):
        self.name = name
        self.__age = age
    @property #(декоратор, он делает из метода аттрибут, поэтоиму вызываем без скобочек)
    def age(self): # def get_age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 120 and new_age > 0:
            self.__age = new_age
        else:
            raise Exception("age can not be less than 0 or more than 120")
obj = Person("Nastya", 52) # AttributeError: 'Person' object has no attribute '__age'
# print(obj.get_age) # 52
# print(obj.age) # 52
print(obj.age)
obj.age = -5
print(obj.age)
