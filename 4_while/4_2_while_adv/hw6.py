# Слияние списков
# В вашем распоряжении имеется два отсортированных
# списка по не убыванию элементов, состоящих из n и m элементов

# Ваша задача слить их в один отсортированный список размером n + m

# Входные данные
# Программа получает на вход два числа n и m - количество элементов первого списка и второго списков

# Затем с новой строки поступают элементы первого отсортированного списка,
# а со следующей строки - второго списка

# Выходные данные
# Слить два списка в один в порядке не убывания и вывести элементы полученного списка

# P.S.: пользоваться встроенной сортировкой запрещено

# Примечание: для вывода результирующего списка вы можете использовать следующую конструкцию

# print(*result) # где result - итоговый список
# Разбор задачи

# Sample Input 1:

# 2 3
# 3 9
# 2 3 6
# Sample Output 1:

# 2 3 3 6 9
# Sample Input 2:

# 3 5
# 2 8 8
# 3 4 5 5 10
# Sample Output 2:

# 2 3 4 5 5 8 8 10
# Sample Input 3:

# 2 5
# 3 7
# 1 1 3 6 8
# Sample Output 3:

# 1 1 3 3 6 7 8
# Sample Input 4:

# 6 8
# 1 3 4 5 6 10
# 1 1 1 3 5 7 9 10
# Sample Output 4:

# 1 1 1 1 3 3 4 5 5 6 7 9 10 10
# Sample Input 5:

# 3 8
# 2 9 10
# 1 1 3 4 6 7 9 9
# Sample Output 5:

# 1 1 2 3 4 6 7 9 9 9 10
# Sample Input 6:

# 11 2
# 1 1 1 3 4 5 6 7 8 8 10
# 4 9
# Sample Output 6:

# 1 1 1 3 4 4 5 6 7 8 8 9 10

import itertools


def not_srted(array):
    """ Definitely not_srted(). """
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return not_srted(less) + equal + not_srted(greater)
    else:
        return array


input()
print(*not_srted(list(itertools.chain.from_iterable([list(map(int, input().split())) for _ in range(2)]))))
