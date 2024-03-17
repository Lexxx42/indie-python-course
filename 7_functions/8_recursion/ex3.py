# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
#
# Входные данные
# Программа принимает на вход натуральное число N (N ≤ 103). Во второй строке через пробел идут N целых чисел, по модулю не превосходящих 103 - элементы последовательности.
#
# Выходные данные
# Ваша задача вывести заданную последовательность в обратном порядке.
#
# Sample Input 1:
#
# 3
# 1 2 3
# Sample Output 1:
#
# 3 2 1
# Sample Input 2:
#
# 5
# 5 9 3 2 7
# Sample Output 2:
#
# 7 2 3 9 5

n = int(input())
sequence = tuple(map(int, input().split()))
print(*sequence[::-1])