# На вход программе поступает список из целых чисел. Ваша задача вывести True, если элементы в списке отсортированы по неубыванию. В противном случае выведите False
#
# Sample Input 1:
#
# 8 11 13
# Sample Output 1:
#
# True
# Sample Input 2:
#
# 8 8 9
# Sample Output 2:
#
# True
# Sample Input 3:
#
# 8 19 6
# Sample Output 3:
#
# False

inp = [int(num) for num in input().split()]
print(inp == sorted(inp))
