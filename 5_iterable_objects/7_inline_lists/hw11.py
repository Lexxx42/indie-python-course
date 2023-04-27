# Состязания - 3
# В метании молота состязается n спортcменов.
# Каждый из них сделал m бросков.
# Побеждает спортсмен, у которого максимален наилучший бросок.
# Если таких несколько, то из них побеждает тот, у которого наилучшая сумма результатов по всем попыткам.
# Если и таких несколько, победителем считается спортсмен с минимальным номером.
# Определите номер победителя соревнований.
#
# Входные данные
#
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве.
# Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
#
# Выходные данные
#
# Программа должна вывести одно число - номер победителя соревнований.
# Не забудьте, что  строки  (спортсмены) нумеруются с 0.
#
# Решение задачи Youtube Patreon Boosty
#
# Sample Input 1:
#
# 3 3
# 1 2 7
# 1 3 5
# 4 1 6
# Sample Output 1:
#
# 0
# Sample Input 2:
#
# 2 3
# 1 2 7
# 1 7 5
# Sample Output 2:
#
# 1
# Sample Input 3:
#
# 2 3
# 7 5 7
# 7 7 5
# Sample Output 3:
#
# 0
# Sample Input 4:
#
# 4 4
# 9 9 9 9
# 8 8 8 8
# 1 1 10 1
# 7 7 7 7
# Sample Output 4:
#
# 2
# Sample Input 5:
#
# 4 4
# 5 5 5 5
# 7 7 7 7
# 4 4 4 4
# 7 7 7 7
# Sample Output 5:
#
# 1

"""
5 5 5 5
7 7 7 7
4 4 4 4
7 7 7 7
"""

# rows, columns = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(rows)]
#
# maximum = max([i for row in matrix for i in row])
# current_sum_of_scores = 0
# idx = 0
#
# for row in matrix:
#     if maximum in row and current_sum_of_scores < (row_sum := sum(row)):
#         current_sum_of_scores = row_sum
#         idx = matrix.index(row)
# print(idx)

n, m = map(int, input().split())
a = []
for i in range(n):
    b = []
    temp = list(map(int, input().split()))
    b.append(max(temp))
    b.append(sum(temp))
    a.append(b)
print(a.index(max(a)))
