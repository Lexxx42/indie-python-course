# Проверка на убывание
# На вход программе поступает список из целых чисел.

# Ваша задача вывести True, если элементы в списке отсортированы строго по убыванию.
# В противном случае выведите False
#
# Sample Input 1:
#
# 8 11 6 5 4 3
# Sample Output 1:
#
# False
# Sample Input 2:
#
# 9 9 9 9 9 9
# Sample Output 2:
#
# False
# Sample Input 3:
#
# 7 6 5 4 3 2 1
# Sample Output 3:
#
# True

inp = [int(num) for num in input().split()]
print(all([inp[i] > inp[i+1] for i in range(len(inp) - 1)]))


