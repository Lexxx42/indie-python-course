# Генераторы списков | List comprehension | Вложенные генераторы

# На этом занятии продолжим изучение генераторов списка и рассмотрим ряд примеров.

# Мы имеем список, элементами которого являются кортежи.
# У кортежей так же есть своя индексация.
# Теперь при помощи генератора списка будем доставать нужные нам значения:

a = [
    ("Sidorov", 1995),
    ("Lukov", 2002),
    ("Petrov", 1991),
    ("Gorbachev", 1984),
    ("Kostin", 2000),
    ("Isaev", 2005),
    ("Eliseev", 1999),
    ("Kozlov", 2004),
    ("Bukov", 1995),
    ("Gavrilov", 1980),
    ("Efremov", 2006),
]
print(a[4][0])
surnames = [elem[0] for elem in a]  # Получим только фамилии
years = [elem[1] for elem in a]  # Получим только год рождения
print(surnames)
print('-' * 20)
print(years)

# Но что, если нам нужно отфильтровать значения и взять только определенные данные.
# Тоже можем такое реализовать при помощи генератора списка. Давайте возьмём

# только те фамилии, которые начинаются с буквы E
# только тех людей, чей год рождения больше, чем 2000
# только первые буквы с каждой фамилии, год рождения которых больше 2000

a = [
    ("Sidorov", 1995),
    ("Lukov", 2002),
    ("Petrov", 1991),
    ("Gorbachev", 1984),
    ("Kostin", 2000),
    ("Isaev", 2005),
    ("Eliseev", 1999),
    ("Kozlov", 2004),
    ("Bukov", 1995),
    ("Gavrilov", 1980),
    ("Efremov", 2006),
]
name_start_e = [elem[0] for elem in a if elem[0].startswith("E")]
print(name_start_e)
more_2000 = [elem[0] for elem in a if elem[1] > 2000]
print(more_2000)
first_letter = [elem[0][0] for elem in a if elem[1] > 2000]
print(first_letter)

# А теперь попробуем при помощи генератора обработать данные,
# которые хранятся в словаре.
# Пусть у нас будет такой вложенный словарь:

a = {
    'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
    'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
    'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
    'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
    'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
    'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
}

# Рассмотрим один из его элементов: ключом является фамилия человека,
# а значением является словарь, состоящий из 3 ключей: возраст, хобби, автомобиль.
# Давайте получим какие-то данные при помощи генератора.

a = {
    'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
    'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
    'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
    'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
    'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
    'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
}
keys = [elem for elem in a]
print(keys)
print('-' * 30)
values = [a[elem] for elem in a]
print(values)

# В итоге, мы получили список из ключей (в нашем случае фамилий) и список словарей.
# Поскольку мы получаем словарь,
# то мы можем по двойной индексации обратиться к какому-либо значению вложенного словаря.

# Например, получим список, состоящий из:
# машин владельцев
# хобби владельцев
# машин, владельцы которых родились раньше 2000
# из кортежей (имя владельца, машина), где год рождения меньше 2000
# из кортежей (имя владельца, машина), где год рождения меньше 2000 и хобби футбол

a = {
    'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
    'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
    'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
    'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
    'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
    'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
}
cars = [a[elem]['car'] for elem in a]
print(cars)
print('-' * 30)
hobbies = [a[elem]['hobby'] for elem in a]
print(hobbies)
print('-' * 30)
cars_lt_2000 = [a[elem]['car'] for elem in a if a[elem]['age'] < 2000]
print(cars_lt_2000)
print('-' * 30)
name_with_car = [(elem, a[elem]['car']) for elem in a
                 if a[elem]['age'] < 2000]
print(name_with_car)
print('-' * 30)
less_2000_and_soccer = [(elem, a[elem]['car']) for elem in a
                        if a[elem]['age'] < 2000 and a[elem]['hobby'] == 'soccer']
print(less_2000_and_soccer)

# Разберём ещё один пример.
# У нас имеется строка, состоящая из различных символов,
# в которые входят буквы и цифры.
# Мы можем при помощи генератора списка сформировать два списка:
# в одном будут хранится только цифры, в другом - только буквы

s = 'gfdogjdf45i398gry74y543hgkgreiuYIUGd'
str_digits = [i for i in s if i.isdigit()]
print(str_digits)
print('-' * 30)

int_digits = [int(i) for i in str_digits if i.isdigit()]
print(int_digits)

print('-' * 30)
letters = [i for i in s if i.isalpha()]
print(letters)

# Рассмотрим ещё один пример.
# На предыдущем занятии мы составляли двумерный список
# m x n и заполняли его нулями при помощи генератора.
# А теперь напишем вложенный генератор
# и для заполнения используем случайные числа с помощью модуля рандом:

from random import randint

n = 5
m = 3
a = [[randint(1, 6) for j in range(m)] for i in range(n)]
for i in a:
    print(i)

# Принцип работы похож на тот, по которому работают вложенные циклы.
# Сделаем квадратную таблицу и в список b будем вносить лишь элементы главной диагонали,
# а в список c только элементы со строки с индексом 2,
# а в список d только элементы столбца с индексом 3.

from random import randint

n = 5
m = 5
a = [[randint(1, 6) for j in range(m)] for i in range(n)]
for i in a:
    print(i)

b = [a[i][j] for i in range(n) for j in range(m) if i == j]
print('main diagon', b)

с = [a[2][j] for j in range(m)]
print('2 row', с)

d = [a[i][3] for i in range(n)]
print('3 column', d)

# Теперь рассмотрим, как при помощи вложенных генераторов можно составить таблицу умножения.

n = 5
m = 5
a = [[i * j for j in range(m)] for i in range(n)]
for i in a:
    print(i)

# Он получается следующим образом:
# сначала у нас фиксируется значение i = 0,
# после чего он умножается на все значения j (от 0 до 4 включительно),
# умножая 0 на все эти числа получим 0.
# Потом i = 1 и она так же умножается на эти значения и получим 0, 1, 2, 3, 4, затем i=2 и т.д.
# Теперь уберём нули во всех этих обходах и сделаем, чтобы наше вводимое число включалось:

n = 5
m = 5
a = [[i * j for j in range(1, m + 1)] for i in range(1, n + 1)]
for i in a:
    print(i)

# В итоге получили таблицу умножения 5х5.
#
# Также вы можете спокойно обходить элементы матрицы внутри генератора списка по значениям,
# для этого достаточно во внутреннем цикле обращаться к итерируемой переменной внешнего цикла

from random import randint

n = 3
m = 4
matrix = [[randint(1, 10) for j in range(m)] for i in range(n)]
for current_row in matrix:
    print(current_row)

print('-' * 30)

squares = [num ** 2 for row in matrix for num in row]
print(squares)
