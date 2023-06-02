print('Объединить два списка в один (желательно несколько способов)')
a = [1, 2, 3]
b = [3, 4, 5]

result_1: list = None
result_2: list = None

result_1 = a + b


result_2 = []
for i in a:
    result_2.append(i)
for i in b:
    result_2.append(i)

result_3 = [j for i in [a, b] for j in i]

result_4 = []

result_4.extend(a)
result_4.extend(b)

result_5 = [*a, *b]

print(f'Результат 1-ый : {result_1}')
print(f'Результат 2-ой : {result_2}')
print(f'Результат 3-ой : {result_3}')
print(f'Результат 4-ой : {result_4}')
print(f'Результат 5-ой : {result_5}')
