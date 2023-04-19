# Вот мы с вами и добрались до легендарной сортировки пузырьком.
# Все просто, вам поступает число
# n - количество элементов в списке, и затем сам список.
#
# Ваша задача отсортировать список по возрастанию при помощи пузырьковой сортировки,
# в случае если элементы соседние совпадают менять их ненужно.
#
# В качестве ответа нужно вывести отсортированный список
# и какое количество раз пришлось переставлять элементы в процессе сортировки
#
# Разбор
#
# Sample Input 1:
#
# 7
# 8 5 3 1 4 7 9
# Sample Output 1:
#
# 1 3 4 5 7 8 9
# 9
# Sample Input 2:
#
# 3
# 9 8 -4
# Sample Output 2:
#
# -4 8 9
# 3
# Sample Input 3:
#
# 7
# 7 13 -18 10 -14 4 -6
# Sample Output 3:
#
# -18 -14 -6 4 7 10 13
# 13

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    count = 0
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
        if not swapped:
            return
    return count

_ = input()
arr = [int(i) for i in input().split()]
count = bubbleSort(arr)

print(' '.join([str(i) for i in arr]), count, sep='\n')
