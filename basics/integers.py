"==========Переменные========="
# переменные - это ссылки на ячейки памяти где хранятся какие то данные
a = 4 

"====== Ввод и Вывод данных======="
#  print  - функция Bывода данных в терминал
# input  - функция Bвода данных с терминала
b = input()
print("Введенное число", a, b)

"=======Числа=========="
# integers(int) -  целые числа (5, 10,  -36, 0 , 1)
# float - вещественные (с плавающей точчкой) (0.3, 0.345, 24.4758,)
# decimal - точное вещественное число (без погрешности)
# чтобы использовать  decimal нужно его импортировать 
# from decimal import Decimal 
c = Decimal(0.1)


#  complex - комплексные числа
b = complex(1, 5)

"========Операции над числами======="
5 + 5  #сложение
10 - 3 #  вычитание 
2 * 3 #  умножение
15 / 3 # деление 
15 // 3 # целочисленное деление (int 7)
5 % 2 # остаток от деления (int 1)
5 ** 2 # возведение в степень 
25 ** 0.5 (1/2) # квадратный корень


# модуль числа - из отриц числа сделает положительное 5
abs (10) #10
abs(-5) #5

#  pow: 
#  1. возводит число в определенную степень 
#  2.  возвращает остаток от деления результата 1 действия на третье число

pow (2, 3) # 8 = 2 **3
pow (2, 3, 4,) #8 % 4 - 0
# (2 ** 3) % 4 = 0 

#divmod  -  функция которая принимает 2 числа и возвращает 2 числа, где первое - это целая часть от делелния, а второе - остаток от деления 
divmod(15, 2) # 7, 1
givmod(9, 3) # 3, 0


# round - функция которая округляет число 
round(5.6) # 6
round(3.5) # 4
round (5.49)  #5 (берет первое число после точки)
# можно указать сколько цифр после запятой оставить
round(10.0475, 3) # 10 .048
round(10.0475, 4) # 10.047


# sqrt - фукнция для нахождения корня числа
#  для работы нужно ее импортировать из библиотеки math
from math import sqrt
sqrt(36) # 6
sqrt(25) # 5
