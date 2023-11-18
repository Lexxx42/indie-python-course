# Функция enumerate

# Функция enumerate помогает обойти итерируемые коллекции
# с возможностью одновременно получать индекс элемента и его значение.

# Функция enumerate возвращает итератор, который можно легко преобразовать например к списку.

a = [10, 20, 30, 40]
print(enumerate(a))

print(list(enumerate(a)))

# В последнем print() мы видим, что функция enumerate возвращает кортежи из пары значений,
# на первом месте пары находится индекс элемента, на втором - значение.
# И результат функции enumerate легко можно обойти в цикле for.

a = [10, 20, 30, 40]

for para in enumerate(a):
    print(para)

# И так как enumerate возвращает пару значений,
# вы можете сразу внутри цикла for завести две переменные - index и value.

a = [10, 20, 30, 40]

for index, value in enumerate(a):
    print(index, value)

# Параметр start
# Функция по умолчанию считает индексы с нуля, но можно при помощи параметра start задать начальное значение отсчета.

words = ['variation', 'random', 'electronics', 'competence', 'collapse']

for index, value in enumerate(words):
    print(index, value)

print('-' * 15)

for index, value in enumerate(words, start=10):
    print(index, value)
