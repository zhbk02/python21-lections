# ● марка (строка)
# ● модель (строка)
# ● год выпуска (целое число)
# ● объем двигателя (decimal, точность 1 знак)
# ● цвет (строка)
# ● тип кузова (поле одиночного выбора.
# варианты: седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап)
# ● пробег (целое число)
# ● цена (decimal, точность 2 знака)
from .models import *
from .serializers import *
import decimal
from decimal import Decimal
body_types = ["sedan", "universal", "kupe", "hetchbeck", "miniwen", "vnedorojnik", "pikap"]
def create():
    mark = input("Введите марку: ")
    model = input("Введите модель: ")
    year = int(input("Введите год: "))
    eng = round(float((input("Введите объём двигателя: "))), 1)
    color = input("Введите цвет: ")
    print("Выберите тип кузова: ")
    for type in body_types:
        print(f"* {type}")
    body_t = input("==================================\nВыберите тип кузова: ")
    if body_t in body_types:
        kuzov = body_t
    else:
        raise Exception("Такого типа не нет")
    probeg = int(input("Введите пробег: "))
    price = round(float((input("Введите цену: "))), 2)
    Car(mark, model, year, eng, color, kuzov, probeg, price)
    return "Машина добавлена"

def listing():
    serializer = CarSerializer()
    cars = serializer.serialize_queryset()
    return cars

def retrieve(p_id):
    car = obj_404(Car, "id", int(p_id))
    serializer = CarSerializer()
    return serializer.serialize_obj(car)


def update(p_id):
    car = obj_404(Car, "id", int(p_id))
    field = input("Что вы хотите изменить?: ")
    if field in dir(car):
        print(f"старое значение: {getattr(car, field)}")
        value = input(f"{field} = ")
        setattr(car, field, value)
    else:
        raise Exception(f"Поля {field} нет в продукте")
    return retrieve(p_id)


def delete(p_id):
    car = obj_404(Car, "id", int(p_id))
    Car.objects.remove(car)
    return "Продукт успешно удален"

def comment():
    print("Выберите продукт:")
    for p in Car.objects:
        print(p.mark, p.model)
    
        
    model = input("===============\Введите модель: ")
    car = obj_404(Car, "model", model)
    body = input("Введите комментарий: ")
    Comment(car, body)
    return 'Комментарий добавлен'