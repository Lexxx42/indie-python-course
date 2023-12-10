# Сколько нулей на конце факториала N!
# В этой задаче вам необходимо воспользоваться уже готовой функцией factorial, которая принимает неотрицательное число, и возвращает значение факториала данного числа.
#
# Ваша задача создать функцию trailing_zeros, которая принимает неотрицательное число, находит его факториал и возвращает сколько нулей на конце этого факториала .
#
# trailing_zeros(6) =>  1, потому что 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720
# trailing_zeros(10) => 2, потому что 10! = 3 628 800
# trailing_zeros(20) => 4, потому что 20! = 2 432 902 008 176 640 000
#
# Нужно написать только определение функций trailing_zeros и factorial
#
# Про инструкцию assert можно прочитать здесь
#
# Sample Input:
#
# Sample Output:
#
# Проверки пройдены


def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


def trailing_zeros(n):
    x = str(factorial(n))
    return len(x) - len(x.rstrip('0'))


# код ниже не стоит удалять, он нужен для проверки
assert trailing_zeros(0) == 0
assert trailing_zeros(6) == 1
assert trailing_zeros(30) == 7
assert trailing_zeros(12) == 2
print('Проверки пройдены')
