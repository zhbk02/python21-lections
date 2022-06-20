import random
guesses_made = 0

name = input('Привет! Как вас зовут?\n')


number = random.randint(1, 30)
print ('Круто, {0}, я загадала число между 1 и 30. Сможете угадать?'.format(name))


while guesses_made < 6:
   
    
    guess = int(input('Введите число: '))
   
    
    guesses_made += 1

    if guess < number:
        print ('Выше число меньше того, что я загадала.')

    if guess > number:
        print ('Ваше число больше того, что я загадала.')

    if guess == number:
        break

if guess == number:
    print ('Вау, {0}! Вы угадали мое число, использовав {1} попыток!'.format(name, guesses_made))
else:
    print ('А вот и не угадали \(._.)/ Я загадалf число {0}'.format(number))