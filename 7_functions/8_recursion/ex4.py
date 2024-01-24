# Двойной факториал
# Описать рекурсивную функцию double_fact, которая принимает на вход целое число и вычисляет значение двойного факториала по формуле:
#
#
#
# double_fact(7) => 105
# double_fact(4) => 8
# double_fact(1) => 1
# double_fact(10) => 3840
# Ваша задача только написать определение функции double_fact

def double_fact(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    if n > 2:
        return n * double_fact(n - 2)

print(double_fact(7))
