# Снова НОД
# В этой задаче вам необходимо воспользоваться уже готовой функцией gcd(a, b), которая принимает два числа и находит наибольший общий делитель для них.
#
# Ваша задача при помощи функции gcd определить НОД произвольного количества чисел.
#
# Входные данные
# На первой строке вводится натуральное число n – количество чисел. Далее идут n строк, в каждой из которых натуральное число.
#
# Выходные данные
# НОД введенных чисел.
#
# Sample Input 1:
#
# 3
# 15
# 18
# 27
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# 4
# 24
# 60
# 48
# 12
# Sample Output 2:
#
# 12
# Sample Input 3:
#
# 3
# 5
# 7
# 13
# Sample Output 3:
#
# 1
# Sample Input 4:
#
# 4
# 3
# 5
# 9
# 18
# Sample Output 4:
#
# 1
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


numbers = [int(input()) for _ in range(int(input()))]
current = numbers[0]
for number in numbers[1:]:
    current = gcd(current, number)

print(current)
