# "==================Наследование=================="
# "Наследование - принцип ООП, где мы можем в дочерном классе унаслодовать, переопределять и использовать все аттрибуты и методы родительского класса"


# class A:
#     def method(self):
#         print("mehtod in class A")

# obj_a =  A()
# obj_a.method() # "method in claass A"

# class B(A):
#     """
#     Наследовали все методы и аттрибуты у класса А
#     """
# obj_b = B()
# obj_b.method() # "method in claass A"

# "class A - родительский класс"
# "class B - дочерний класс"

# class C(A):
#     """Наследовали все методы и аттрибу у класса А и переопределили метод method"""
#     def method(self):
#         print("methon in class C")

# obj_a = A()
# obj_c = C()
# obj_a.method() # "method in claass A "
# obj_c.method() # "method in claass C"

# "Переопределение - даем то же название, но другое значение"

# "super() - функция которая позволяет обратиться к родителькскому классу и вызвать определенные методы или аттрибуты"

# class A:
#     def my_range(self, n):
#         return list(range(0, n+1))

# class B(A):
#     def my_range(self):
#         # через super  мы обращаемся к методу родительского класса
#         return super().range(10)
# # obj_a.A()
# # obj_a.my_range(3) # [0, 1, 2, 3]

# obj_b = B()
# obj_b.my_range() # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# "=====================Множественное Наследование==========================="
# # - это наследование от 2 или более классов

# class A:
#     a = "a"
# class B:
#     b = "b"
# class C(A,B):
#     """Наследовались от 2 кдассов А и В"""
#     c = "c"

# obj_c = C()
# obj_c.a # "a"
# obj_c.b # "b"
# obj_c.c # "c"


"================Проблемы множественного наследования==================="
# 1. проблема ромба - решенная проблема начиная с версии 2.3 (с помощью MRO - method resolution order)
class A:
    ...
class B(A):
    ...
class C(A):
    ...
class D(B,C):
    ...
print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# 2. проблема перекрестного наследования - нерешенная проблема
class A: ...
class B: ...

class C(B,A): ...
class D(A, B): ...

class E(C,D): ...
#  TypeError: Cannot create a consistent method resolution coorder (MRO) for bases B, A



"============================Виды наследование==========================="
# Одиночное наследование
# множественное наследование
# многоуровневое наследование 
# иерархическое наследование
# гибридное наследование 


