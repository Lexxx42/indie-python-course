# Спираль
# Требуется вывести квадрат, состоящий из N×N клеток, заполненных числами от 1 до N2 по спирали (см. примеры).
#
# Входные данные
# Программа получает на вход одно число n.
#
# Выходные данные
# Программа должна вывести матрицу, заполненную числами от 1 до N2 по спирали, при этом между числами может быть любое количество пробелов. Не допускается начинать спираль в ином, кроме верхнего левого, углу, закручивать спираль против часовой стрелки или изнутри наружу.
#
# Разбор задачи
#
# Sample Input:
#
# 3
# Sample Output:
#
# 1 2 3
# 8 9 4
# 7 6 5


def print_spiral_matrix(rows):
    for i in range(rows):
        for j in range(rows):

            # x stores the layer in which (i, j)'th element lies
            # find minimum of four inputs
            x = min(min(i, j), min(rows - 1 - i, rows - 1 - j))

            # print upper right half
            if i <= j:
                print(abs((rows - 2 * x) * (rows - 2 * x) - (i - x) - (j - x) - (rows ** 2 + 1)), end='')

            # print lower left half
            else:
                print(abs((rows - 2 * x - 2) * (rows - 2 * x - 2) + (i - x) + (j - x) - (rows ** 2 + 1)), end='')

            print('\t', end='')
        print()


print_spiral_matrix(int(input()))
