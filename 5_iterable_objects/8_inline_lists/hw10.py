# A. Тортминатор
# Дан прямоугольный торт, который имеет вид таблицы размером r × c. Каждая ячейка таблицы содержит либо гадкую клубничку, либо является пустой. Например, торт размера 3 × 4 может выглядеть так:
#
#
#
# Тортминатор намерен съесть этот торт! Каждый раз, когда он ест, он выбирает строку или столбец, не содержащие гадкой клубнички, а содержащие по крайней мере одну несъеденную ячейку торта. Затем Тортминатор поедает все выбранные им ячейки торта. Тортминатор может есть сколько угодно раз. Вот пример того, как он это сделает
#
# .   .
#
# Пожалуйста, выведите максимальное количество ячеек, которые может съесть Тортминатор.
#
# Входные данные
# Первая строка содержит два целых числа r и c (2 ≤ r, c ≤ 10), обозначающих количество строк и количество столбцов в торте. Следующие r строк содержат по c символов — j-ый символ i-ой строки обозначает содержимое ячейки в строке i и столбце j, и имеет одно из следующих значений:
#
# символ '.' обозначает ячейку торта без гадкой клубнички;
# символ 'S' обозначает ячейку торта с гадкой клубничкой.
# Выходные данные
# Выведите максимальное количество ячеек торта, которые может съесть тортминатор.
#
# Разбор задачи Youtube Patreon Boosty
#
# Sample Input 1:
#
# 3 4
# S...
# ....
# ..S.
# Sample Output 1:
#
# 8
# Sample Input 2:
#
# 7 3
# S..
# S..
# S..
# S..
# S..
# S..
# S..
# Sample Output 2:
#
# 14
# Sample Input 3:
#
# 10 10
# SSSSSSSSSS
# SSSSSSSSSS
# SSSSSSSSSS
# SSSSSSSSSS
# SSSSSSSSSS
# SSSSSSSSSS
# SSSSSSSSSS
# SSSSSSSSSS
# SSSSSSSSSS
# SSSSSSSSSS
# Sample Output 3:
#
# 0
# Sample Input 4:
#
# 10 10
# .....SSSSS
# .....SSSSS
# .....SSSSS
# .....SSSSS
# .....SSSSS
# ..........
# ..........
# ..........
# ..........
# ..........
# Sample Output 4:
#
# 75
# Sample Input 5:
#
# 8 9
# .........
# .........
# .........
# .........
# .........
# .........
# SSSSSSSSS
# .........
# Sample Output 5:
#
# 63

"""
введи значения a и b ->

cобери матрицу ->

посчитай сколько строк без 'S' ->

сделай 2-ю матрицу через zip значений 1-й матрицы  mtx2 = list(zip(*mtx1))->

посчитай сколько столбцов без 'S' во 2 матрице ->

результат =  строк * b + столбцов * a - строк*столбцов

ВСЁ
"""

"""
3 4
S...
....
..S.
"""

rows, columns = map(int, input().split())
matrix1 = [[i for i in input()] for row in range(rows)]

number_of_rows_without_s = sum([1 for row in matrix1 if 'S' not in row])
matrix2 = list(zip(*matrix1))
number_of_columns_without_s = sum([1 for column in matrix2 if 'S' not in column])
number_of_pices_ated = number_of_rows_without_s * columns + number_of_columns_without_s * (
        rows - number_of_rows_without_s)
print(number_of_pices_ated)
