# В архитектуре компьютера важную роль играют числа,
# являющиеся степенями двойки: 1, 2, 4, 8 и так далее.
# Напишите программу, которая проверяет, является ли введённое натуральное число степенью двойки.
# Если да, то выводится сама эта степень; если нет, выводится «НЕТ»

# Разбор Youtube Patreon Boosty

# Sample Input 1:

# 8
# Sample Output 1:

# 3
# Sample Input 2:

# 9
# Sample Output 2:

# НЕТ

# import math
# n = int(input())
# result = math.log2(n)
# print("НЕТ" if result %1 != 0 else int(result))

n = int(input())
if not (n & (n - 1)):
    power = 0
    while n > 1:
        n //= 2
        power += 1
    print(power)
else:
    print('НЕТ')
