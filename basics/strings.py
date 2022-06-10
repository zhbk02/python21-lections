"========Строки======"
# строки - неизменяемый тип данных , который предназначен для хранения текста или последовательности символлов, заключенного в одинарные или двойные кавычки
#  Синтаксиc:
from itertools import count


string1 ='строка с одинанрными ковычками'
string2 = "строка с двойными ковычками"
# error = 'не правильная строка"
string3 = "Don't" # внутри двойных кавычек все одинарные это просто символы
string4 = '"Makerss bootcapm"' # внутри одинарных кавычек все двойные - просто символы

string5 = '''
многострочный текст в 
одинарных кавычках
Тут можно оставить 'любые' "кавычки"
""""
''

'''
string6 = """
многострочный текст в 
одинарных кавычках
Тут можно оставить 'любые' "кавычки"
'''''
"""

"======Экранизация строк======="
# экранизакция спец-символов
'\n' # перенос на новую строку
'\t' #  табуляция
"\\" # отображение \ (потому что она является инструкцией, которая влияет на наш код)
'\'' # отображает '
"\""
'\r' # движение каретки (курсор) в начало строки
'\v' # перенос на новую строку со смещением вправо на длину предыдущей строки 
# пример:
'hello \nworld'
# hello
# world

# 'hello\tworld'
# hello    world
'чтобы экранировать нужен символ \\'
# 'чтобы экранировать нужен символ \'

'My website is Latracal \rSolution'
# Solutionte is Latracal

'hello \vworld'
# hello
#      world  

"==================Форматирование строк============"
title = "Плов"
price = 1500
format1 = f'Название: {title},  Цена:{price}: '
# Название: Плов, Цена: 1300

format2 = "Название: %s, Цена: %s"
print(format2 % ("Гуляш", "250"))
print(format2 % ("самсы", "70"))
# Название: Гуляш , Цена: 250
# Название: самсы , Цена: 70

format3 = -'Название: {}, Цена:{}'
print(format3.format('Шакарап', '35'))


"=========Методы строк========"
# методы типов данных - функции, к которым мы обращаемся через точку
dir(str) # позволяет посмотреть все методы класса (типа данных)

'HELLO'.lower() # 'hello'
'hello'.upper() # 'HELLO'
'Hello'.swapcase() #'hELLO' (меняет)
'hello'.title() # Hello
'heLLo'.title() # 'Hello'
'hello world'.title() # 'Hello World'
'hello world'.capitalize() # 'Hello world'
'hello'.centre(11) # '   hello   ' (всего 11 символов)
'hello'.count('l') # 2
'hello'.count('ll') # 1
'hello hello'.count('hello') # 2
'hello world'.startswith('hello') # True
'hello world'.startswith(H) # False
'hello world'.endswith('ld') # True

'hello world'.find(' ')  #5
'hello world'.find('o') # 4
'hello world'.find('hello') # 0

'hello world'.split() # ['hello', 'world']
'hello world'.split("o")  #  ['hell', ' w', ' rld']
'$'.join(["hello", "world"]) # "hello$world"
"".join(["hello", "world"]) # "helloworld"
" ".join(["hello world".split()]) # "hello world"

# конкатенация - склеивание строк
"hello" + "world" # "hello world"
"hello" + "world"




'=========Индексы========'
# индексы - порядковый номер символа в строке
'h e l l o   w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
string = 'hello world'
string[0] # 'h'
string[10] # 'd'
string[5] # ' '


# срез - это подстрока строки
# string [0:5] # 'hello'
# string [2;4] # 'll'
# string[0:5][2:4] # 'll'
# string[:5] # 'hello'
# string[6:] # 'world'
# string[:] # 'hello world'
# string[0:11:2]  # 'hlowrd'
# string[::3]  # 'hlwl'
# string[::-1] # "dlrow olleh"
# string[::-2] # 'drwolh




# # ДОП ИНФА
# a = 5
# b= 5
# print(id(a)
# print(id(b)))
# print(hash(a)) 