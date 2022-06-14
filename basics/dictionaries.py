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


"=================Создание словарей ======================="
dict1 = {"a":3}
dict2 = dict( [ ('key1', 'value1'), ('key2', 'value2') ] )
# dict2 = {'key1':'value1', 'key2':'value2'}
dict3 = dict( ( ['key1', 'value1'], ('key2', 'value2') ) )
# dict3 = {'key1':'value1', 'key2':'value2'}
dict4 = dict(['ab', 'cd', 'de'])
# dict4 = {"a":"b", 'c':'d', 'd':'e'}
key1, value1 = 'ab'
dict4[key1] = value1
key2, value2 = 'cd'
dict4[key2] = value2
key3, value3 = 'de'
dict4[key3] = value3


dict5 = dict(['abc']) # ValueError: dictionary update sequence element #0 has length 3; 2 is required
key1, value1 = 'abc' #
dict5[key1] = value1



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