# Числа Трибоначчи
# Описать рекурсивную функцию tribonacci, которая принимает на вход целое число n - порядковый номер чисел Трибоначчи. Функция по параметру n должна вычислить и вернуть значение, стоящее на n-м месте в ряде чисел Трибоначчи
#
#
#
# Вот примере вызовов:
#
# tribonacci(0) => 0
# tribonacci(2) => 1
# tribonacci(4) => 2
# tribonacci(6) => 7
# tribonacci(7) => > 13

def fibonacci_of(n):
    cache = {0: 0, 1: 1}

    if n in cache:
        return cache[n]

    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)
    return cache[n]


count = int(input())
fib = [fibonacci_of(n) for n in range(count + 1)]
print(fib[count])
