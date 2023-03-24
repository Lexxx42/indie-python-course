# Даны два натуральных числа A и B. Требуется найти их наименьшее общее кратное (НОК).
#
# Sample Input 1:
#
# 6 15
# Sample Output 1:
#
# 30
# Sample Input 2:
#
# 14 21
# Sample Output 2:
#
# 42

from math import gcd

# НОК = ab / НОД(a, b)
a,b = tuple(map(int, input().split()))
print(int(a * b / gcd(a, b)))
