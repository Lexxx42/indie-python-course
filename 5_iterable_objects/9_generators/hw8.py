# Давайте усовершенствуем предыдущую задачу так, чтобы получался следующий список букв:
#
# ['A', 'BB', 'CCC', 'DDDD', 'EEEEE', 'FFFFFF', ...]
# Входные данные
# На вход программе подается натуральное число n, n ≤ 26.
#
# Формат выходных данных
# Программа должна вывести список из первых n заглавных букв английского алфавита, причем каждая буква должна быть продублирована в зависимости от своего порядкового номера
#
# Sample Input 1:
#
# 3
# Sample Output 1:
#
# ['A', 'BB', 'CCC']
# Sample Input 2:
#
# 5
# Sample Output 2:
#
# ['A', 'BB', 'CCC', 'DDDD', 'EEEEE']
# Sample Input 3:
#
# 9
# Sample Output 3:
#
# ['A', 'BB', 'CCC', 'DDDD', 'EEEEE', 'FFFFFF', 'GGGGGGG', 'HHHHHHHH', 'IIIIIIIII']

from string import ascii_uppercase

n = int(input())
print([ascii_uppercase[i] * (i + 1) for i in range(n)])
