# Сформировать кортеж, содержащий натуральные числа в интервале [a; b] и вывести его на экран.
#
# Формат ввода
# Вводится два натуральных числа a и b в отдельных строках. Гарантируется, что a<b.
#
# Формат вывода
# Вывести кортеж, содержащий натуральные числа в интервале [a; b]
#
# Подсказка
# Sample Input:
#
# 8
# 11
# Sample Output:
#
# (8, 9, 10, 11)

a = int(input())
b = int(input())
print(tuple(range(a, b+1)))