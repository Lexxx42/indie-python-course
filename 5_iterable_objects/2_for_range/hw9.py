# Стандартная задача на нахождения факториала.
# Факториал числа n! обозначается и находится по формуле

# def factor(num: int) -> int:
#     if not num:
#         return 1
#     else:
#         answer = 1
#         for i in range(1, num + 1):
#             answer *= i
#         return answer
#
#
# print(factor(int(input())))
#
# from math import factorial
#
# print(factorial(int(input())))
for i in range(n := 1, int(input()) + 1):
    n *= i
print(n)
