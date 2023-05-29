# Состязания
# В метании молота состязается n спортcменов. Каждый из них сделал m бросков.
# Победителем считается тот спортсмен, у которого сумма результатов по всем броскам максимальна.
# Если перенумеровать спортсменов числами от 0 до n-1, а попытки каждого из них – от 0 до m-1,
# то на вход программа получает массив A[n][m], состоящий из неотрицательных целых чисел.
# Программа должна определить максимальную сумму чисел в одной строке и вывести на экран эту сумму и номер строки,
# для которой достигается эта сумма.
#
# Входные данные
#
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве.
# Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
#
# Выходные данные
#
# Программа должна вывести  2 числа: сумму и номер строки, для которой эта сумма достигается.
# Если таких строк несколько, то выводится номер наименьшей из них.
# Не забудьте, что нумерация строк (спортсменов) начинается с 0.
#
# Sample Input 1:
#
# 2 2
# 5 4
# 3 5
# Sample Output 1:
#
# 9
# 0
# Sample Input 2:
#
# 3 4
# 1 2 3 4
# 9 10 11 12
# 5 6 7 8
# Sample Output 2:
#
# 42
# 1
# Sample Input 3:
#
# 1 1
# 5
# Sample Output 3:
#
# 5
# 0
# Sample Input 4:
#
# 3 5
# 1 2 3 4 5
# 3 3 3 3 3
# 5 4 3 2 1
# Sample Output 4:
#
# 15
# 0

# rows, cols = map(int, input().split())
# matrix = [list(map(int, input().split())) for row in range(rows)]

n, m = map(int, input().split())
matrix = []

for i in range(n):
    matrix.append([int(x) for x in input().split()])
column_sum = [sum(matrix[i]) for i in range(n)]

print(winner := max(column_sum), column_sum.index(winner), sep='\n')