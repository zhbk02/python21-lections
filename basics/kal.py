a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
s = input("Выберите операцию из следующих +-*/%**// : * ")

if s == "+":
    print(a + b)
elif s == "-":
    print(a - b)
elif s == "*":
    print(a * b)
elif s == "/":
        print(a / b)
elif s == "**":
    print(a ** b)
elif s == "//":
    print(a // b)
elif s == "%":
    print(a % b)
else:
    print("Данной операции нет в системе")