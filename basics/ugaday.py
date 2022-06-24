# import random
# guesses_made = 0

# name = input('Привет! Как вас зовут?\n')


# number = random.randint(1, 30)
# print ('Круто, {0}, я загадала число между 1 и 30. Сможете угадать?'.format(name))


# while guesses_made < 6:
   
    
#     guess = int(input('Введите число: '))
   
    
#     guesses_made += 1

#     if guess < number:
#         print ('Выше число меньше того, что я загадала.')

#     if guess > number:
#         print ('Ваше число больше того, что я загадала.')

#     if guess == number:
#         break

# if guess == number:
#     print ('Вау, {0}! Вы угадали мое число, использовав {1} попыток!'.format(name, guesses_made))
# else:
#     print ('А вот и не угадали \(._.)/ Я загадалf число {0}'.format(number))








# big_matryoshka = 15

# def second_matryoshka():

#    matryoshka_second = 10

#    def third_matryoshka():

#        matryoshka_third = 5

#        return matryoshka_third + matryoshka_second

#    return third_matryoshka() + big_matryoshka

# print(second_matryoshka())




# gl = []

# def add(name):

#    global gl

#    gl += [name]

# def remove(inx):

#    del gl[inx]

# for _ in range(7):

#    add(input())

# for _ in range(2):

#    remove(int(input()))

# print(gl)


# from random import choice
 
# def add():
#     global c
#     c.append(input('Введите имя '))
#     return 1
 
# def remove():
#     global c
#     if not len(c): return
#     del c[int(input(f'Удалить имя от 0 до {len(c) - 1} '))]
#     return 1
 
# c = []
# i = 0
# while i < 10:
#     if choice([add, remove])():
#         i += 1
# print(c)


def check(n):
    p=n%10
    n=n//10
    while(n>0):
        c=n%10
        if c<p:
            return False
        p=c
        n=n//10
    return True
    
print(check(968754321))
