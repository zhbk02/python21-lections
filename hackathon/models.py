# Задание:
# 1. Создайте класс Cars со следующими атрибутами объекта:
# ● марка (строка)
# ● модель (строка)
# ● год выпуска (целое число)
# ● объем двигателя (decimal, точность 1 знак)
# ● цвет (строка)
# ● тип кузова (поле одиночного выбора.
# варианты: седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап)
# ● пробег (целое число)
# ● цена (decimal, точность 2 знака)
# 2. Добавьте views:
# ● create для создания записей
# ● listing для получения списка записей
# ● retrieve для получения одной записи
# ● update для обновления записей
# ● delete для удаления записей

class Car():
    objects = []
    _id = 0
    def __init__(self, mark, model, year, eng, color, kuzov, probeg, price):
        self.id = Car._id
        self.mark = mark
        self.model = model
        self.year = year
        self.eng = eng
        self.color = color
        self.kuzov = kuzov
        self.probeg = probeg
        self.price = price
        Car.objects.append(self)
        Car._id += 1

    @property
    def comments(self):
        return [c for c in Comment.objects if c.product == self]
class Comment:
    objects = []

    def __init__(self, product, body):
        from datetime import datetime
        self.product = product
        self.body = body
        self.created_at = datetime.now()
        Comment.objects.append(self)


# class Car:
#     objects = []
#     _id = 0

#     def __init__(self, mark, model, year, eng_cap, color, body_type, probeg, price):
#         self.id = Car._id
#         self.mark = mark
#         self.model = model
#         self.year = year
#         self.eng_cap = eng_cap
#         self.color = color
#         self.body_type = body_type
#         self.probeg = probeg
#         self.price = price
#         Car.objects.append(self)
#         Car._id += 1

#     def get_info(self):
#         return '\n'.join((
#             f"Моя марка -{self.mark}",
#             f"Моя модель - {self.model}",
#             f"Год выпуска -{self.year}",
#             f"Обьем двигателя - {self.eng_cap}",
#             f"Мой цвет - {self.color}",
#             f"Тип кузова - {self.body_type}",
#             f"Пробег - {self.probeg}"
#             f"Цена -{self.price}"

#         ))

# lamborgini = Car('Lamborgini', 'Huracan', 2022, 650, 'мятно-черный', 'sedan', 0, 200000)   
# lexus = Car('lexus','lexus600 rx edition', 2015, 300, 'нардагрей', 'внедорожник', 1000,150000)
# Toyota = Car('Toyota', 'camry70',2020, 500, 'черный-снег', 'купе', 1500, 99999)
# Nissan = Car('Nissan', 'SKY-line', 2004, 450, 'белый-негр', 'седан', 0 , 111110)
# Subaru = Car('Subaru', 'Subaru BrZ', 2022, 500, 'черно-голубой', 'седан', 200 , 200213231)
# #  вызываем машины с помощью функциююю гет инфо
# print(lamborgini.get_info())
# print(lexus.get_info())
# print(Toyota.get_info())
# print(Nissan.get_info())
# print(Subaru.get_info())

