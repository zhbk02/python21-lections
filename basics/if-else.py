
"========== Логические операторы==============="

# логические операторы = выражения, которые возвращают, True, если правда, False,если ложь



5 == 5 # True
4 == 5 # False

5 != 5 # False (1=  не равно)
5 !=  # True

 5 > 10 # False
10 > 5 # True
5 > 5 # False

5 < 10 # True
10 < 5 # False
5 < 5 # False

5 <= 10 # True
10 <= 5 # False
5 <= 5 # True

5 >= 10 # False
10 >= 5 # True
5 >= 5 # True

"5" == 5 # False

"=================And / Or================"
# and - и 
# or - или
a = 5
b = 6

a == 5 and b == 6 # True (правая сторона true левая тоже True)
a == 5 and b == 5  # False правая тру, но левая фолс




not True # False
not False # True
not a == 5 # False (потому что a == 5)
not a == 4 # True (потому что a == 5)

# если обе части выдают True -будет True
# если обе части выдают False - будет False
# если одна частть True, второая False
# 1. если стоит and - выйдет False
# 2. если соит or - выйдет True

not a == 5 # false
not a == 4 # True 
"=========Boolean Type========="
# булевый тип данных - имеет всего два значени Tue и False
bool (1) # True (все числа кроме 0 будет  True)
bool(0) # False 


bool("hello") # False
bool("") # False
bool(" ") # True

bool(True) # True
bool (False) # False 

"==========None============="
#  None  - тип данных с одним значением  None который zиспользуется для обозначения пустых значений или отсутсвия
bool(None) # False
bool("None") #True

# a = None (это специальная пустота в которую позже можно мжно ввести значение)

a = None 
print(bool(a)) # False
print(a is None) # True
# is  это проверка на полное соответствие (это как вопрос)


"============== Условные операторы =============="
# условные операторы нужны для того чтобы при разных данных код работал по разному 

if условие1:
    тело1
    # будет работать только если условие1 верно

if условие1:
    тело1
    # будет работать только если условие1 верно
else:
    тело2
    # будет работать если условие1 не верно

if условие1:
    тело1
    # будет работать только если условие1 верно
elif условие2:
    тело2
    # будет работать если условие1 не верно и условие2 верно

if условие1:
    тело1
    # будет работать только если условие1 верно
elif условие2:
    тело2
    # будет работать если условие1 не верно и условие2 верно
else:
    тело3
    # будет работать если условие1 не верно и условие2 не верно

# в одной конструкции мы можем исользовать неограниченное кол-во elif
# в одной конструкции мы можем использовать только один if
# else  мы также можем использовать тольк один раз или не указывать вообще







a = int(input("Введите число: "))

if a > 0:
    print(f"Число {a} -положительное")
elif a < 0:
    print(f"Число {a} -отрицательное")
else:
    print(f"Число {a} - это 0")

"=========FizzBuzz======"
# если число кратно 3 - вывести Fizz
# если число кратно 5 - вывести Buzz
# если число кратно и 5 и 3 - вывести FizzBuzz
# если число не кратно ни 5 ни 3 - вывести число 
'''



# for i in range(1, 101):
#     if i % 3:
#         print("Fizz")
#     if i % 5:
#         print("Buzz")
#     if i % 5 or i % 3:
#         print("FizzBuzz")
#     else:
#         print (i)


# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     if i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# for i in range(1, 17):
#     if i % 3 == 0:
#         if i % 5 == 0:
#             print("FizzBuzz")
#         else:
#             print("Fizzbuzz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)


'''



"=========== Тернарные операторы============"
#  условия в одну строку 
тело1 if условие else тело2

a = 5
res = "Hello" if a == 5 else "Bye"
print(res)
# Hello если а == 5 
# Bye если а != 5
