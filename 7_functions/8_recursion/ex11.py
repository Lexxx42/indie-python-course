# Превращаем вложенный список в плоский
# Представьте, что у нас есть список целых чисел неограниченной вложенности. То есть наш список может состоять из списков, внутри которых также могут быть списки. Ваша задача превратить все это в линейный список при помощи функции flatten
#
# flatten([1, [2, 3, [4]], 5]) => [1, 2, 3, 4, 5]
# flatten([1, [2, 3], [[2], 5], 6]) => [1, 2, 3, 2, 5, 6]
# flatten([[[[9]]], [1, 2], [[8]]]) => [9, 1, 2, 8]
# Ваша задача только написать определение функции flatten
#
# Разбор Youtube Patreon Boosty
from typing import Iterable


def flatten_generator(items):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten_generator(x):
                yield sub_x
        else:
            yield x


def flatten(items):
    return list(flatten_generator(items=items))


print(list(flatten([1, [2, 3], [[2], 5], 6])))
