#  Вид данных кортеж (tuple)

# Кортеж (tuple) – неизменяемая упорядоченная последовательность, обычно используемая для хранения разнотипных объектов.
# Кортеж очень напоминает список, но только кортеж является неизменяемым типом данных.

# Варианты создания кортежа
# 1) С помощью перечисления элементов в круглых скобках:

a = (1, 2, 3, 4, 5)
print(a, type(a))

b = ('hello', 45, True)
print(type(b))
print(b)

# 2) Пропустить круглые скобки и записать объекты через запятую:

a = 1, 2, 3, 4, 5
print(a, type(a))

b = 'hello', 45, True
print(type(b))
print(b)

# Это работает с любым количеством элементов,
# только если вам нужно создать кортеж из одного элемента,
# нужно обязательно не забыть указать запятую после этого элемента:

a = 1,
print(type(a))

b = 1
print(type(b))

# 3) При помощи функции tuple(). Ей надо передать итерируемый объект: например range(), список или строку

a = tuple(range(5))
print(a, type(a))

b = tuple('hello')
print(b, type(b))

my_list = [43, True, 'The Boys']
c = tuple(my_list)
print(c, type(b))

# Создание пустого кортежа
# Пустой кортеж можно создать следующими способами:

a = ()
print(a, type(a))

b = tuple()
print(b, type(b))

# Операции с кортежами
# Нахождение длины кортежа
# При помощи функции len() можем найти количество элементов кортежа

a = 1, 2, 3, 4, 5
print(len(a))

b = 'hello', 45, True
print(len(b))

empty = ()
print(len(empty))

# Проверка на нахождение
# Оператор in – позволяет проверить имеется ли элемент в кортеже.
# Если данный элемент присутствует, то результат будет  True, в обратном случае – False.

a = 1, 2, 3, 4, 5
print(2 in a)
print(7 in a)
print(6 not in a)

# Сложение кортежей
# Сложение (сцепление) кортежей. Порядок сложения имеет значение

a = 1, 2, 3, 4, 5
b = (6, 7, 8)

c = a + b
d = b + a
print(c)
print(d)

# Кортеж с другими типами данных не поддерживает операцию сложения
#
# Дублирование кортежей
# Чтобы продублировать кортеж необходимо его умножить на целое число:

a = 1, 2, 3, 4, 5

print(a * 2)

print((6, 7, 8) * 4)

# Поиск максимума и минимума
# Функции min(), max() позволяют узнать минимальный и максимальный элемент кортежа

a = 1, 2, 3, 4, 5

print(min(a), max(a))

# Функции min(), max() можно использовать только если кортеж состоит из однотипных элементов,
# которые можно сравнить между собой (целиком из чисел или целиком из строк).

# Если бы наш кортеж был бы таким:

# a = (1, 2, 'hi', 4, 5)
# то получили бы ошибку.

# Суммирование элементов кортежа
# Просуммировать элементы кортежа (если он состоит исключительно из чисел):

a = 1, 2, 3, 4, 5

print(sum(a))

b = tuple(range(200, 301))
print(sum(b))

# Функция sum() можно использовать только если кортеж состоит целиком из числовых элементов.
# Если бы наш кортеж был бы таким:

# a = (1, 2, 'hi', 4, 5)
# то получили бы ошибку.
