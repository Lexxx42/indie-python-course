# Побочная диагональ

# Дана матрица размером NxN, требуется найти максимальное значение среди элементов, расположенных на побочной диагонали.
#
# Под побочной диагональю матрицы подразумевается диагональ, проведённая из правого верхнего угла до левого нижнего угла.

# Входные данные
# Программа сперва принимает на вход число N (N<=15) - количество строк и столбцов в списке, а затем в N строках записаны элементы списка.
#
# Выходные данные
# Вывести самой большой элемент на побочной диагонали
#
# Sample Input 1:
#
# 2
# 1 2
# 3 4
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 2:
#
# 7
# Sample Input 3:
#
# 5
# 100 2 3 90 100
# 1 54 3 90 100
# 1 2 5 90 100
# 1 2 3 2 100
# 1 2 3 90 100
# Sample Output 3:
#
# 100

# rows = int(input())
# matrix = [[int(i) for i in input().split()] for i in range(rows)]
#
# diagonals = [matrix[i][j] for i in range(rows) for j in range(rows) if j == rows - 1 - i]
# print(max(diagonals))

print(max((input().split()[~i] for i in range(int(input()))), key=int))
