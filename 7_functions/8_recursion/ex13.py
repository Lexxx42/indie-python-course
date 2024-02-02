# # функция merge_two_list должна объединить два списка
# def merge_two_list(a, b):
#     pass
#
#
#
# # функция merge_sort должна выполнить сортировку
# def merge_sort(s):
#     pass

# 7
# 6 2 19 5 10 7 11

# 2 5 6 7 10 11 19

def merge_two_list(a: list, b: list):
    return merge_sort(a + b)


def merge_sort(arr: list):
    _merge_sort(arr=arr)
    return arr


def _merge_sort(arr: list):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        _merge_sort(L)
        _merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


print(merge_two_list([10, 18], [1, 2, 3, 4, 6, 8]))

#merge_sort([11, 15, 19, 20, 20, 6, 4, 16, 8])
