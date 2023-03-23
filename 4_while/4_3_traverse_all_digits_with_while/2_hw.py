# Программа принимает на вход одно натуральное число и
# выводит его цифры в столбик в обратном порядке.

# Sample Input 1:

# 412
# Sample Output 1:

# 2
# 1
# 4
# Sample Input 2:

# 8942
# Sample Output 2:

# 2
# 4
# 9
# 8


# for i in range(len(n := input()) - 1, -1, -1):
#     print(n[i])

# n = input()
# i = len(n) - 1
#
# while i >= 0:
#     print(n[i])
#     i -= 1

list(map(print, list(input())[::-1]))

print(*input().strip()[::-1], sep='\n')
