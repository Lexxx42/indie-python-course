# Операции над frozenset
# Все операции, которые можно применять над обычным множеством set, можно использовать и над frozenset
#
# Нахождение длины frozenset
# При помощи функции len() можем найти количество элементов неизменяемого множества

a = frozenset([1, 3, 2])
print(f'Длина {a} = {len(a)}')

b = frozenset()
print(f'Длина {b} = {len(b)}')

c = frozenset([1, 1, 2, 2, 1, 2, 1])
print(f'Длина {c} = {len(c)}')

# Проверка на нахождение
# Оператор in позволяет проверить имеется ли элемент во frozenset или нет.
# Если данный элемент присутствует, то результат будет  True, в обратном случае – False.

a = frozenset([1, 2, 3])
print(2 in a)
print(5 in a)
print(4 not in a)
print(1 not in a)

# Поиск максимума и минимума
# Функции min(), max() позволяют найти минимальный и максимальный элемент неизменяемого множества, если там хранятся элементы одного типа

a = frozenset([1, 2, 3])
print(min(a), max(a))

b = frozenset([11, 19, 22, 2, 13, 22, 10])
print(min(b), max(b))

# Функции min(), max() можно использовать только если frozenset состоит из однотипных элементов, которые можно сравнить между собой (целиком из чисел или целиком из строк). Если бы наше неизменяемое множество было бы таким:
#
# a =  frozenset({1, 2, 'hi', 4, 5})
# то получили бы ошибку TypeError: '>' not supported between instances of 'str' and 'int'.

# Суммирование элементов
# Просуммировать элементы frozenset(если оно состоит исключительно из чисел):

a = frozenset((2, 4, 5, 7, 8, 9))
print(sum(a))

# Сортировка frozenset
# При помощи функции sorted() можно отсортировать frozenset, если в нем содержатся однородные элементы.
#
# Результатом работы функции sorted() всегда будет являться список

my_set = frozenset([8, 4, 7, 5, 2, 3, 6])

sorted_list = sorted(my_set)
print(sorted_list)

my_string_set = frozenset([
    'profit', 'fare', 'thesis',
    'architecture', 'insurance',
    'hero', 'shrink', 'north',
    'drill', 'toast'])

print(sorted(my_string_set))

# Операции, которые нельзя выполнять над frozenset

# Индексация
# К элементам frozenset нельзя обращаться по индексу, это приведет к ошибке TypeError: 'frozenset' object is not subscriptable

# Функция reversed
# Функцию reversed() нельзя использовать для множество, так как множества это неупорядоченная коллекция.
# При попытке вызывать функцию reversed()  вы получите ошибку TypeError: 'frozenset' object is not reversible
