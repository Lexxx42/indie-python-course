a = [4, -10, 43, -300, 54, 289, -34, -8, 749]
print(sorted(a, key=abs))  # [4, -8, -10, -34, 43, 54, 289, -300, 749]


def get_last_digit(num: int) -> int:
    return num % 10


a = [4, 10, 43, 300, 54, 289, 34, 8, 749]
print(sorted(a, key=get_last_digit))  # [10, 300, 43, 4, 54, 34, 8, 289, 749]


# Можно сделать двойной критерий сортировки.
# Первый критерий сортировки будет первичным: применяться в первую очередь,
# а при равенстве значений будет задействован второй критерий.
# Например, числа 10 и 300 оба заканчиваются на 0,
# но если сортировать ещё и по второй цифре, то значение 10 будет больше, чем 300, также с 54 и 34, 289 и 749.

# Для сортировки по ещё одному критерию в функции после указания первого параметра сортировки ставим запятую и вносим второе выражение:

def get_last_digit(num: int) -> int:
    return num % 10, num // 10 % 10


a = [4, 10, 43, 300, 54, 289, 34, 8, 749]
print(sorted(a, key=get_last_digit))  # [300, 10, 43, 4, 34, 54, 8, 749, 289]

a = ['ZZZ', 'aaa', 'eee', 'DDD', 'BBB', 'www']
print(sorted(a))  # ['BBB', 'DDD', 'ZZZ', 'aaa', 'eee', 'www']

a = ['ZZZ', 'aaa', 'eee', 'DDD', 'BBB', 'www']
print(sorted(a, key=str.lower))  # ['aaa', 'BBB', 'DDD', 'eee', 'www', 'ZZZ']

a = ['ZZZ 79', 'aaa 45', 'eee 43', 'DDD 800', 'BBB 5', 'www 14']
print(sorted(a, key=lambda x: int(x.split()[1])))  # ['BBB 5', 'www 14', 'eee 43', 'aaa 45', 'ZZZ 79', 'DDD 800']

a = ['ZZZ 800', 'aaa 45', 'eee 43', 'DDD 800', 'BBB 43', 'www 14']
print(
    sorted(a, key=lambda x: (int(x.split()[1]), x.split()[0]))
)  # ['www 14', 'BBB 43', 'eee 43', 'aaa 45', 'DDD 800', 'ZZZ 800']
