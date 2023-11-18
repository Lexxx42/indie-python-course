# 1. a.intersection(b) или a & b - пересечение это когда надо отразить только те объекты, которые встречаются сразу в 2-ух множествах.
# a &= b или a.intersection_update(b)  - сразу присвоить пересечение в переменную а
#
# 2. a.union(b) или a | b - объединение создаст новое множество из всех элементов обоих множеств.
# a |= b или a.union_update(b) - сразу присвоить объединение в переменную а
#
# 3. a - b - вычитание. Удалит из множества а только те элементы которые присутствуют в множестве b. a -= bсразу изменит a
#
# 4. a ^ b  - симметричная разность. в множество войдут все значения кроме тех что присутстуют и в а и в b одновременно
#
# 5. a > b - True если все элементы из b входят в a, иначе False

# Знакомство со множеством

# Само понятие множество пришло из математики. Там под множеством понимается набор,
# совокупность каких-либо объектов, называемых элементами этого множества.
# Например, рассмотрим кириллицу, алфавит этого языка состоит из 33 букв.
# При помощи этих букв образованы все слова русского языка.
# И тогда мы можем сказать, что множество русского языка состоит из 33 элементов: букв от А до Я

# Множеством английского языка будет 26 элементов: буквы от A до Z

# Количество элементов в множестве арабских цифр равно 10: это цифры от 0 до 9.
# Именно при помощи этих цифр образованы все числа

# Множество в python
# Множество (тип данныхset) – это неупорядоченная коллекция уникальных элементов.
# Здесь стоит подчеркнуть слово уникальных, потому что тип данных set не допустит,
# чтобы в одной коллекции хранились повторяющиеся элементы.

# Способы создания множества

# 1) При помощи фигурных скобок:

a = {1, 2, 3}
print(a)
print(type(a))

b = {1, 2, 1, 2, 3, 1, 1, 4}
print(b)
print(type(b))

# Обращаю еще раз ваше внимание на то,
# что в полученных множествах находятся уникальные элементы в
# одном экземпляре и нету ни одного повторяющего значения.

# Также важно отметить, что множество является неупорядоченной коллекцией,
# то есть в предыдущем случае мы могли бы получить что-то из следующего:
# {1, 4, 3, 2} , {4, 3, 2, 1} или {4, 2, 1, 3} и т.д.

# 2) При помощи функции set() мы можем преобразовать другую коллекцию
# (список, строку и т.д.) в множество

a = set('abcdeabc')
b = set([1, 2, 3, 2, 3, 1, 3])
c = set(range(5))
print(a)
print(b)
print(c)

# Создание пустого множества
# Чтобы создать пустое множество необходимо воспользоваться функцией set() без указания аргументов.
# Стоит отметить, что нельзя создать множество с помощью пустых фигурных скобок {},
# т.к. при помощи пустых фигурных скобок создается словарь.

a = set()
print(a)
print(type(a))

print('-' * 15)

b = {}
print(b)
print(type(b))

# Словари и множества оба записываются в фигурных скобках, это создает небольшую путаницу.
# Не забывайте, что словари содержат пары ключ-значения,
# которые всегда записываются через двоеточие.
# Именно по наличию знака : в выводе объекта можно понять, что перед вами словарь.
# Также вы всегда можете проверить тип объекта.

# Ограничение на элементы множества
# Множество может состоять только из неизменяемых объектов.
# К примеру, множество можно сделать из списка чисел,
# но вот из вложенного списка уже нельзя, поскольку элементами такого списка являются списки,
# которые сами по себе являются изменяемыми объектами.

a = [1, 2, 3, 4, 3, 2, 3, 1, 3, 4, 2, 2, 2]
a = list(set(a))

print(a)

b = [[1, 2, 3, 4],
     [3, 2, 3, 1],
     [3, 4, 2, 2]]
b = set(b)
print(b)

# При попытки создать множество, содержащее изменяемый объектом, возникнет ошибка

# TypeError: unhashable type
# К неизменяемым объектам, напоминаю, относятся:

# строки
# числа int и float
# кортежи
# frozenset (изучаем далее)
# Все эти значения могут являться элементами множества