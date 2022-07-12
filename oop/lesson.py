# Множественное наследование, миксины

# task1
'''
from datetime import datetime

class Smartphone:
    def call(self, phone_number):
        print(f"Calling to {phone_number} number")

    def where_to_wear(self):
        print("You can keep me any where")

class Watch:
    def see_time(self):
        print(f"It's {datetime.now()} now")

    def where_to_wear(self):
        print("You should wear me on your hand")

class SmartWatch(Watch, Smartphone):
    pass

smartwatch = SmartWatch()
smartwatch.call(phone_number="996505164790")
smartwatch.see_time()
smartwatch.where_to_wear()
'''
# Task2
'''
class CheckMixin:
    def check(self, username, password):
        if self.username == username and self.password == password:
            print("Succesfully created")
            self.count += 1

        else:
            print("Wrong")

class Instagram(CheckMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.count = 0

    def post_post(self, title, username, password):
        super().check(username=username, password=password)
      

class Tiktok(CheckMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.count = 0

    def post_video(self, video, username, password):
        super().check(username=username, password=password)


obj1 = Instagram(username="zhibek", password="qwerty12")
obj1.post_post(title="hello",username="zhibek", password="qwerty12")
obj1.post_post(title="test post", username="zhibek", password="qwerty")

print(obj1.count)

obj2 = Tiktok(username="zhbk", password="ololo")
obj2.post_video(video="rainy day", username="zhbk", password="ololo")

print(obj2.count)

'''