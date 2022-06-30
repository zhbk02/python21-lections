"=================Работа с файлами ============================"
try:
    # open открывает файл для чтения
    file = open("file.txt")
    # Метод read() считает файл полностью
    # output = file.read()
    # readline() # читает только одну строку
    # output = readlines(1)
    # output2 = readlines(2)
    # readlines() читает все строки, возвращает список
    # output = file.readlines()
    # 

    output = file.read()
except:
    pass
finally:
    file.close

print(output)