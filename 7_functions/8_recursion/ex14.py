# Быстрая сортировка (quick sort) | Разбор
#
# Быстрая сортировка - еще один вид сортировки, который использует рекурсию.
#
# Ваша задача реализовать этот алгоритм.
# Для этого нужно будет создать функцию quick_sort,
# которая будет принимать исходный список и возвращать новый отсортированный в порядке неубывания список.
#
# Необходимо написать только определение функций quick_sort, при этом нельзя пользоваться встроенными сортировками в Python
#
# Sample Input 1:
#
# 5
# 19 4 5 17 1
# Sample Output 1:
#
# 1 4 5 17 19
# Sample Input 2:
#
# 8
# 16 19 2 12 20 15 20 15
# Sample Output 2:
#
# 2 12 15 15 16 19 20 20


def partition(array, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)

    _quicksort(array, begin, end)

    return array


arr = [12, 13, 13, 1, 13, 3, 19, 8, 4]

print(quick_sort(arr))
