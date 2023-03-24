# Даны два натуральных числа A и B. Требуется найти их наибольший общий делитель (НОД) методом вычитания
#
# Sample Input 1:
#
# 77 22
# Sample Output 1:
#
# 11
# Sample Input 2:
#
# 5 7
# Sample Output 2:
#
# 1

from math import gcd

print(gcd(*(map(int, input().split()))))
