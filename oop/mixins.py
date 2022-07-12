"=================Миксины===================="
#  Миксин - класс, которфй булет использоваться для наследования. от Мискинов не создаются обьекты.

from pyexpat import model


class CreateMixin:
    def product_create(self, title, price):
        #  self.__class__ - обращение к классу, который наследовалс от этого миксина
        _id = model._id
        self.title = title
        self.price = price
        self.id = _id
        model.objects[_id] = self
        model._id += 1


class ReadMixin:
    def product_detail(self):
        from pprint import pprint
        pprint({"id":self.id, "title":self.title, "price":self.price})

class Update:
    ...

class DeleteMixin:
    def delete_product(self):
        model = self.__class__
        model.objects.pop(self.id)



class ProductCRUD(CreateMixin, ReadMixin, Update, DeleteMixin):
    objects = {}
    _id = 1

crud = ProductCRUD()
crud.product_create("obj1", 45)
crud.product_create("obk2", 456)
print(crud.objects)