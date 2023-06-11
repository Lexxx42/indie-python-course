import random
from timeit import Timer

a = (random.choice('1234567890abcdefghijklmnopqrstuvwxyz') for x in range(1000000))


def f_1():
    s = {}
    for x in a:
        if x not in s:
            s[x] = 1
        else:
            s[x] = s[x] + 1


def f_2():
    s = {}
    for x in a:
        s[x] = s.get(x, 0) + 1


for x in range(1, 3):
    print(f'{Timer("func()", "from __main__ import f_%s as func" % x).timeit(5):.8f}')
