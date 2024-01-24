# Число сочетаний
# Описать рекурсивную функцию get_combin, которая принимает на вход два целых числа  и находит C(N,K) — число сочетаний из N элементов по K — с помощью рекуррентного соотношения:
#
#
#
# При этом гарантируется, что входные значения n и k будут удовлетворять следующим условиям:
#
# n > 0
# 0 ≤ k ≤ n
# Вот примеры вызовов:
#
# get_combin(5, 5) => 1
# get_combin(5, 2) => 10
# get_combin(3, 1) => 3
# get_combin(7, 0) => 1
# Ваша задача только написать определение функции get_combin


from functools import lru_cache


@lru_cache(maxsize=1000)
def get_combin(n, k):
    if k == 0:
        return 1

    elif n == k:
        return 1

    elif 0 < k < n:
        return get_combin(n - 1, k) + get_combin(n - 1, k - 1)

n = int(input())
k = int(input())

print(get_combin(n, k))
