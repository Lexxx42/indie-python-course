print('Сгенерировать список от 0 до 100 отсортированный на убывание, где числа нечётные и кратны 3')
result: list = None

result = list(filter(lambda x: x % 2 and not x % 3, [i for i in range(100, -1, -1)]))

print(f'Результат: {result}\n')

a = filter(lambda x: x % 2 and not x % 3, [*range(100, -1, -1)])

print(list(a))
