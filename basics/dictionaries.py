"========= Словари ============="
# Словарь (dict) - изменяемый, итерирумый, неиндексируемый и неупорядоченный
#  тип данных, в котором значения хранятся в парах (ключ:значение)

dict_ = {"a":1, "b":2, "c":3}
print(dict_["a"]) # Hello

# ключами в словаре могут являться все неизменяемые типы данных 
# значениями в словаре могут являться любые типы данных
# ключи должны быть уникальными 

dict_ = {
    1:"hello",
    "a":4,
    4.5:{"a":5},
    # {"s":5}: 44 # TypeError: unhashable type
}

"================Методы Словаря =================="
dict_clear() # чистить словарь
print(dict_ ) # {}

dict_ = dict.fromkeys([1,2,4])
print(dict_) # {1:None, 2:None, 4:None}

dict_ = dict.fromkeys([,2,4, "Hello"])
print(dict_) # {1:"hello", 2:"hello", 4:"hello"}

dict_ = {"a":1, "b":2}
dict_ ["a"] # 1
dict_{"c"} # KeyError

# МЕТОДЫ
# get нужен для только для получения значений
dict_.get("a") # 1
dict_.get("c") # None (то есть там пустоЭ нет такого ключа в словаре )
dict_.get("c", 5) # 5
dict_.get("a", 5) # 1

dict_.keys() # dict_keys(["a", "b"])
dict_.values() # dict_values([1, 2])
dict_.items() # dict_items(["a", 1 ]), ("b", 2)])

dict1 = {1:"a", 2:"b", 3:"c"}
dict2 = {3:"d", 4:"e"}
# метод update добавляет пары из второго словаря в первый
dict1.update(dict2)
print(dict1) # {1:"a", 2:"b", 3:"c" 4:"e"} 
print(dict2) # {3:"d", 4:"e"}

# метод pop удаляет ппару по ключу и возвращает значение 
print(dict1.pop(3)) # d
print(dict1) # {1:"a", 2:"b", 4:"e"}
print(popped) # d 

# метод popitem удаляет и возвращает последнюю пару 
print(dict1.popitem())