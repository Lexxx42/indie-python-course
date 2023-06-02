print('Сбросить дубликаты из списка')

c = [1, 1, 1, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7]
result: list = None

# result = list(set(c))
result = list(dict.fromkeys(c))

print(f'Результат: {result}\n')
