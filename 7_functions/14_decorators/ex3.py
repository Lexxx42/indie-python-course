# Напишите декоратор double_it, который возвращает удвоенный результат вызова декорированной функции
#
# @double_it
# def multiply(num1, num2):
#     return num1 * num2
#
# res = multiply(9, 4) # произведение 9*4=36, но декоратор double_it удваивает это значение
# print(res)
# @double_it
# def get_sum(*args):
#     return sum(args)
#
# res = get_sum(1, 2, 3, 4, 5)
# print(res) # печатает 30
# Ваша задача написать только определение функции декоратора double_it
#
# Sample Input:
#
# Sample Output:
#
# Good

# Напишите определение декоратора double_it
def double_it(func, *args, **kwargs):
    def inner(*args, **kwargs):
        return func(*args, **kwargs) * 2

    return inner


# Код ниже не удаляйте, он нужен для проверки
@double_it
def multiply(num1, num2):
    return num1 * num2


@double_it
def some_func_return(a, b, c):
    return a ** b + c


@double_it
def get_sum(*args):
    return sum(args)


assert multiply(9, 4) == 72
assert multiply(100, 4) == 800

assert get_sum(1, 2, 3, 4, 5) == 30

assert some_func_return(4, 5, 4) == 2056
assert get_sum(14, 51, 34) == 198
assert get_sum(14) == 28
assert get_sum() == 0
assert get_sum(43, 5, 43, 43, 43, 43, 3, 2) == 450
print('Good')
