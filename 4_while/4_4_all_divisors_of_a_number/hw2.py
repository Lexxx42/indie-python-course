# Программа получает на вход натуральное число N.
#
# Нужно найти сумму его делителей.
#
# Sample Input 1:
#
# 10
# Sample Output 1:
#
# 18
# Sample Input 2:
#
# 31
# Sample Output 2:
#
# 32

# a = int(input())
# i = 1
# res = 0
# while i <= a:
#     if a % i == 0:
#         res += i
#     i = i + 1
# print(res)

from sympy import divisors

print(sum(divisors(int(input()))))
