"==============Абстракция===================="
# абстракция - принцип ООП, в котором создается абстрактный еласс(класс - путсышка), в котором создаются названия аттрибутов и методов, для того чтобы в дочерних классах переопределить их нужным образов. от абстрактных классов мы не создаем обьектов, потому что в них есть только названия и нет логики

from abc import ABC, abstractmethod, abstractclassmethod, abstractproperty

class AbstractAnimal(ABC):
    @abstractclassmethod
    def voice(self):
        ...

    @abstractproperty
    def legs(self):
        ...
# obj = AbstractAnimal() # TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

class Dog(AbstractAnimal):
    ...
# obj = Dog() #TypeError: Can't instantiate abstract class Dog with abstract methods legs, voice

class Dog(AbstractAnimal):
    legs = 4

    def voice(self):
        print("gav-gav")

class Cat(AbstractAnimal):
    legs = 4

    def voice(self):
        print("mew-mew")

dog1 = Cat()
dog1.voice() # gav-gav

cat1 = Cat()
cat1.legs # 4

