# Программа принимает на вход одно натуральное число и
# выводит его цифры в двоичной системе в столбик в обратном порядке.
#
# Sample Input 1:
#
# 8
# Sample Output 1:
#
# 0
# 0
# 0
# 1
# Sample Input 2:
#
# 18
# Sample Output 2:
#
# 0
# 1
# 0
# 0
# 1
# Sample Input 3:
#
# 435
# Sample Output 3:
#
# 1
# 1
# 0
# 0
# 1
# 1
# 0
# 1
# 1

n = int(input())
while n > 0:
    print(n % 2)
    n = n // 2
