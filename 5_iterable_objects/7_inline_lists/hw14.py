# Миша и негатив
# Миша уже научился хорошо фотографировать и недавно увлекся программированием. Первая программа, которую он написал, позволяет формировать негатив бинарного черно-белого изображения.
#
# Бинарное черно-белое изображение – это прямоугольник, состоящий из пикселей, каждый из которых может быть либо черным, либо белым. Негатив такого изображения получается путем замены каждого черного пикселя на белый, а каждого белого пикселя – на черный.
#
# Миша, как начинающий программист, написал свою программу с ошибкой, поэтому в результате ее исполнения мог получаться некорректный негатив. Для того чтобы оценить уровень несоответствия получаемого негатива исходному изображению, Миша начал тестировать свою программу.
#
# В качестве входных данных он использовал исходные изображения. Сформированные программой негативы он начал тщательно анализировать, каждый раз определяя число пикселей негатива, которые получены с ошибкой.
#
# Требуется написать программу, которая в качестве входных данных использует исходное бинарное черно-белое изображение и полученный Мишиной программой негатив, и на основе этого определяет количество пикселей, в которых допущена ошибка.
#
# Программа сперва считывает числа n и m (1 ≤ n, m ≤ 100) – высоту и ширину исходного изображения (в пикселях). Последующие n строк содержат описание исходного изображения. Каждая строка состоит из m символов «B» и «W». Символ «B» соответствует черному пикселю, а символ «W» – белому. Далее следует пустая строка, а после нее – описание выведенного Мишиной программой изображения в том же формате, что и исходное изображение.
#
# Необходимо вывести на экран число пикселей негатива, которые неправильно сформированы Мишиной программой.
#
# Решение задачи Youtube Patreon Boosty
#
# Sample Input 1:
#
# 3 4
# WBBW
# BBBB
# WBBW
#
# BWWW
# WWWB
# BWWB
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# 2 2
# BW
# BB
#
# WW
# BW
# Sample Output 2:
#
# 2

rows, columns = map(int, input().split())
matrix = [i for _ in range(rows) for i in input()]
_ = input()
negative = [i for _ in range(rows) for i in input()]
defects = 0

for i in range(len(matrix)):
    if matrix[i] == negative[i]:
        defects += 1
print(defects)