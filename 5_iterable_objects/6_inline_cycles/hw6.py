# Сортировка вставками
# Это еще один вид сортировки, который реализуется при помощи вложенных циклов

# Программа получает на вход число
# n - количество элементов в списке, и затем в следующей строке сам список.
#
# Ваша задача отсортировать список по возрастанию при помощи сортировки вставками,
# в случае если элементы соседние совпадают менять их ненужно.
#
# В качестве ответа нужно вывести отсортированный список.
#
# Sample Input 1:
#
# 6
# 5 4 2 15 6 6
# Sample Output 1:
#
# 2 4 5 6 6 15
# Sample Input 2:
#
# 5
# 11 2 8 1 5
# Sample Output 2:
#
# 1 2 5 8 11

# def insertion_sort(lst):
#     for i in range(1, len(lst)):
#         temp = lst[i]
#         j = i - 1
#         while (j >= 0 and temp < lst[j]):
#             lst[j + 1] = lst[j]
#             j = j - 1
#         lst[j + 1] = temp
#
# _ = input()
# input_list = [int(i) for i in input().split()]
#
# insertion_sort(input_list)
# print(' '.join([str(i) for i in input_list]))

# exec("input(); print(*sor""ted(map(int, input().split())))")

# Glozman
n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    j, e = i, a[i]
    while j > 0 and a[j - 1] > e:
        a[j] = a[j - 1]
        j -= 1
    a[j] = e
print(*a)
