# https://stepik.org/lesson/625516/step/6?auth=login&thread=solutions&unit=621274
"""
    Simple framework to measure code performance based on module time
    Author:   Alex Glozman
    Version:  1.4
    Modified: 27.10.2022
"""

from time import perf_counter as time


# Functions to test

def num_cubes_loop(n):
    i = k = 1
    while n >= i:
        n -= i
        k += 1
        i += k

    return k - 1


def num_cubes_cubic_eqv(n, prec=6):
    a, b, c, d = 1, 3, 2, -6 * n
    p = c / a - (b ** 2) / (3 * a ** 2)
    hq = 0.5 * (2 * b ** 3 / (27 * a ** 3) - (b * c) / (3 * a ** 2) + d / a)
    Q = (p / 3) ** 3 + hq ** 2
    sqrtQ = Q ** .5
    x = (-hq + sqrtQ) ** (1 / 3) + (-hq - sqrtQ) ** (1 / 3) - b / (3 * a)
    return (int(round(x, prec)))


def num_cubes_aproc(n):
    def num_cubes(h):
        return h * (h + 1) * (h + 2) // 6

    def aprox_height(n):
        return (6 * n) ** (1 / 3) - 1

    h = int(aprox_height(n))
    return h + (num_cubes(h + 1) == n)


# функция для замера времени
def run_test(func, nums, comment='', reps=1, average=True, prec=.6):
    total = 0
    for _ in range(reps):
        for e in nums:
            beg = time()
            res = func(e)
            end = time()
            total += (end - beg)
    t = total / reps if average else total
    print(f'{t:{prec}f} ({comment})')


#  генерируем кортеж чисел в интервале RANGE (выбираем кортеж для того, чтобы его нельзя было изменить в тестах)
RANGE = (1, 50_000)
nums = tuple(range(*RANGE))

#  число прогонов
REPETISIONS = 50

run_test(num_cubes_loop, nums, comment='решение с циклом while', reps=REPETISIONS)
run_test(num_cubes_cubic_eqv, nums, comment='аналитическое решение', reps=REPETISIONS)
run_test(num_cubes_aproc, nums, comment='аналитическое решение - метод проб', reps=REPETISIONS)
