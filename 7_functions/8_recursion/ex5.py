# исла Фибоначчи
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где число, стоящее на n-ой позиции можно вычислить по формуле:
#
#
#
# Требуется найти N-е число Фибоначчи.
#
# Входные данные
# Программе поступает на вход целое число N (0 ≤ N ≤ 30) - порядковый номер числа Фибоначчи.
#
# Выходные данные
# Вам необходимо вывести на экран N-е число Фибоначчи.
#
# Sample Input 1:
#
# 7
# Sample Output 1:
#
# 13
# Sample Input 2:
#
# 10
# Sample Output 2:
#
# 55


def fibonacci_of(n):
    cache = {0: 0, 1: 1}

    if n in cache:
        return cache[n]

    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)
    return cache[n]


count = int(input())
fib = [fibonacci_of(n) for n in range(count + 1)]
print(fib[count])
