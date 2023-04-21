# Обход элементов матрицы - 1
# Задана целочисленная квадратная матрица размером N x N.

# Необходимо обойти элементы этой матрицы сверху вниз слева направо
# и вывести элементы именно в таком порядке в виде таблицы.
#
# Программа принимает на вход натуральное число N – количество строк и столбцов матрицы.
# В каждой из последующих N строк записаны N целых чисел – элементы матрицы.
# Все числа во входных данных не превышают 100 по абсолютной величине.
#
# Sample Input 1:
#
# 5
# 3 4 9 1 2
# 8 2 0 5 1
# 4 7 4 8 7
# 7 1 3 3 8
# 5 6 3 7 0
# Sample Output 1:
#
# 3 8 4 7 5
# 4 2 7 1 6
# 9 0 4 3 3
# 1 5 8 3 7
# 2 1 7 8 0
#
# Sample Input 2:
#
# 2
# 6 7
# 9 0
# Sample Output 2:
#
# 6 9
# 7 0

# n = int(input())
# matrix = []
#
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# for i in range(n):
#     for j in range(n):
#         print(matrix[j][i], end=' ')
#     print()

'''Вот матрица m:
    a a b b
    a a b b
    c c d d
    c c d d 
Вложенный цикл с m[i][j] вернёт матрицу  как она есть:
a a b b 
a a b b
c c d d
c c d d 
Вложенный цикл с  m[j][i] отразит матрицу по главной диагонали:
a a c c
a a c c
b b d d
b b d d 
тот же код с m[~i][j] отразит верх и низ:
c c d d
c c d d
a a b b
a a b b
m[i][~j] отразит лево и право
b b a a
b b a a
d d c c
d d c c 
m[~j][~i] отразит лево и право относительно побочной диагонали:
d d b b
d d b b
c c a a
c c a a
'''

# a = [list(map(int, input().split())) for i in range(int(input()))]

#[print(*row) for row in zip(*(input().split() for i in range(int(input()))))]

print(*(' '.join(row) for row in zip(*(input().split() for i in range(int(input()))))), sep='\n')
