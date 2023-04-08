# На вход программе поступает список из целых чисел.
# Ваша задача найти в данном списке наименьшее положительное значение.
# В случае, если положительных значений нет, выведите строку "Empty"

# Sample Input 1:

# 8 11 -9 0 5 -20
# Sample Output 1:

# 5
# Sample Input 2:

# 5 -2 -1 18 4 -6
# Sample Output 2:

# 4
# Sample Input 3:

# -4 -7 0 -19
# Sample Output 3:

# Empty

# print(lst[0] if len(lst := sorted([c for c in map(int, input().split()) if c > 0])) > 0 else 'Empty')

# input_list = [int(i) for i in input().split()]
# print(min(elements) if len(elements := list(filter(lambda x: x > 0, input_list))) > 0 else "Empty")

lst = [int(i) for i in input().split() if int(i) > 0]
print(min(lst) if lst else 'Empty')
