# Состязания - 2
# В метании молота состязается n спортcменов.
# Каждый из них сделал m бросков. Победителем соревнований объявляется тот спортсмен,
# у которого максимален наилучший результат по всем броскам.
# Таким образом, программа должна найти значение максимального элемента в данном массиве,
# а также его индексы (то есть номер спортсмена и номер попытки).
#
# Входные данные
#
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве.
# Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
#
# Выходные данные
#
# Программа выводит значение максимального элемента,
# затем номер строки и номер столбца, в котором он встречается.
# Если в массиве несколько максимальных элементов, то нужно вывести минимальный номер строки,
# в которой встречается такой элемент, а если в этой строке таких элементов несколько,
# то нужно вывести минимальный номер столбца.
# Не забудьте, что все строки и столбцы нумеруются с 0.
#
# Разбор задачи Youtube Boosty Patreon
#
# Sample Input 1:
#
# 3 3
# 3 1 2
# 1 3 4
# 3 3 3
# Sample Output 1:
#
# 4
# 1 2
# Sample Input 2:
#
# 3 3
# 7 5 3
# 4 2 1
# 16 8 9
# Sample Output 2:
#
# 16
# 2 0
# Sample Input 3:
#
# 3 4
# 7 5 3 5
# 4 2 1 9
# 6 8 9 10
# Sample Output 3:
#
# 10
# 2 3
# Sample Input 4:
#
# 2 4
# 7 5 9 9
# 9 2 1 9
# Sample Output 4:
#
# 9
# 0 2
# Sample Input 5:
#
# 3 2
# 7 7
# 7 7
# 7 7
# Sample Output 5:
#
# 7
# 0 0

"""
3 1 2
1 3 4
3 3 3
"""

rows, columns = map(int, input().split())
matrix = [list(map(int, input().split())) for row in range(rows)]

current_max = matrix[0][0]
max_idx = (0, 0)
for i, row in enumerate(matrix):
    if max(row) > current_max:
        current_max = max(row)
        max_idx = (i, row.index(current_max))

print(f'{current_max}\n{max_idx[0]} {max_idx[1]}')