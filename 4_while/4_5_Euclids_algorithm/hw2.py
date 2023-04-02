# Та же самая задача, необходимо найти НОД двух чисел,
# только теперь нужно модернизировать свой код при помощи нахождения остатка от деления
#
# Sample Input 1:
#
# 200 30
# Sample Output 1:
#
# 10
# Sample Input 2:
#
# 10000 1
# Sample Output 2:
#
# 1

a, b = tuple(map(int, input().split()))
while b > 0:
    c = a % b
    a = b
    b = c
print(a)
