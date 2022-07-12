"================Ассоциации============================="
# это принцип ООП, в котором два класса друг с другом связаны
# ассоциация делится на 2 принципа:
# 1 - агрегация (более слабая связь)
# 2 - композиция (более сильная связь)

class Battery:
    power = 100

    def charge(self):
        if self.power < 100:
            self.power = 100


class Iphone:
    def __init__(self, color:str):
        self.color = color
        self.battery = Battery
        # когда мы создаем обьект от класса прям внутри другого - тесная связь - композиция

class Nokia:
    def __init__(self, color:str, battery:Battery):
        self.color = color
        self.battery = battery
        # когда мы принимаем уже созданный вне класса обьект - агрегация



iphone = Iphone("золотой")

del iphone
# обьект батарейки удаляется вместе с обьектом iphone

battery = Battery()
nokia = Nokia("черный", battery)

# удаляется только обьект nokia
# обьект батарейка сохраняется  "агрегация"