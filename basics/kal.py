# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
# s = input("Выберите операцию из следующих +-*/%**// : * ")

# if s == "+":
#     print(a + b)
# elif s == "-":
#     print(a - b)
# elif s == "*":
#     print(a * b)
# elif s == "/":
#         print(a / b)
# elif s == "**":
#     print(a ** b)
# elif s == "//":
#     print(a // b)
# elif s == "%":
#     print(a % b)
# else:
#     print("Данной операции нет в системе")


# Task1 

# numbers_str = input("Введите цифры через запятую: ").split(", ")
# numbers_int = []
# for number in numbers_str:
#     numbers_int.append(int(number))

# print(numbers_int[0], numbers_int[-1])

# numbers_int.pop()
# numbers_int.append('Makers')
# print(numbers_int)

# Task 2
# from random import sample
# numbers = sample(range(0, 20), k = 10)
# print(numbers)
# print(sorted(numbers))
# print(numbers) 
 

#  Task3

# list_length = int(input("Enter list length: "))

# words = []
# words_length = []
# for i in range (list_length):
#     word = input("Enter word: ")
#     words.append(word)

# for i in words:
#     words_length.append(len(i))

# print(words)
# print(words_length)


# try:
#     num1 = input("Enter anything: ")
#     num2 = input("Enter anything: ")
#     result = int(num1) + int(num2)
# except ValueError:
#     result = num1 + num2
# finally:
#     print(result)


# dict_ = {1:"bob123", 2:"lil456"} 

# dict_ = {value: key for key, value in dict_.items{}}
# try:
#     username = input("Enter username: ")
#     ID = dict_{username}
#     print(ID)
# except KeyError:
#     print("There isn't such username in database")
# else:
#     print(f"Welcome, {username} ")
# finally:
#     print("Thank You")

# try:
#     age = int(input("Enter your age: "))
#     if age <= 0:
#         raise Exception ("Do not enter negative integers or zero")
# except ValueError:
#     print("Enter integer, not string")
# else:
#     print(f"Your age: {}")





# random number

# import random

# NumberToGuess = random.randint(1, 100)

# userGuess = -1


# while userGuess != NumberToGuess:
#     userGuess = int(input("Угадайте число от 1 до 100: "))
#     if userGuess > NumberToGuess:
#         print("Число должно быть меньше")
#     elif userGuess < NumberToGuess:
#         print("Число должно быть больше")
#     else:
#         priint("Вы угадали число = ")

#         break

# def get_type(x, y):
#     type1 = type(x, y)
#     return type1
# print(get_type(5, "s"))


# task1
# from random import random


# from random import random


# # def generate_password(param1, param2):
# #     import _random
# #     random_list = random.sample(range(1, 10), k=7)
# #     print(random_list)

# # # def get_info(name=(input("Enter your name: "))),
# # #             last_name(input("Enter your last name: ")):

# # generate_password(1, 2)
# # def generate_password(param1, param2):
# #     import random
# #     random_list = random.sample(range(1, 10), k = 7)
# #     random_list = [str(i) for i in random_list]
# #     password = param1 + param2 + "".join(random_list)
# #     return password
    

# # def get_info(name=input("Enter your name: ")),
# #             last_name=input("Enter your last name: ")
# #             generate_password(param1=name, param2=last_name)
# #             return password

# # print(get_info())

# # def get_data():
# #     num1 = int(input("Enter first number: "))
# #     num2 = int(input("Enter second number: "))

# # dictionary = {"+": add(num1, num2),
            

# # Task 1
# from math import sqrt

# list_ = [4, " abc", 3, 12, True, 2.5, False] 
# new_list = list(map(lambda x: round (sqrt(x)), filter(lambda y: type(y) == int, list_)))
# print(new_list)

# num = 4321

# if str(num)[0] > str(num)[1] and str(num)[1] > str(num)[2] and str(num)[2] > str(num)[3]:
#     print('yes')
# else:
#     print('no')



# number = '1234'
# if number[-1] < number[-2] : 
#     if number[-2] < number[-3]:
#         if number[-3] < number[-4]:
#             print('yes')
# else:
    # print('No')

number = '1233'
if (number[-1] > number[-2]) and (number[-2] and number[-3]) and (number[-3] > number[-4]):
    print('yes')
else:
    print('No')

number = '1233'
if number[-1] < number[-2] : 
    if number[-3] < number[-4]:
        print('yes')
else:
    print('No')


# num = 4321

# if str(num)[0] > str(num)[1] and str(num)[1] > str(num)[2] and str(num)[2] > str(num)[3]:
#     print('yes')
# else:
#     print('no')

# num = 4322

# num1 = int(str(num)[0])
# num2 = int(str(num)[1])
# num3 = int(str(num)[2])
# num4 = int(str(num)[3])


# if (num1 > num2) and (num2 > num3) and (num3 > num4):
#     print('yes')
# else:
#     print('no')








# Task2

# dictionary = [{"name": "Alex", "point": 87},
#             {"name": "Kate", "point":69},
#             {"name": "Billy", "point":57},
#             {"name": "Jerry", "point":56}]

# list_ = list(filter(lambda x: x ["point"] < 60, dictionary))
# print(list_)

# Task3
# from functools import reduce

# list_ = ["m", "a", "k", "e", "r", "s"]

# result = reduce(lambda a, b: a + b, list_)
# print(result)