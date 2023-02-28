# Напишите программу, которая на вход получает координаты двух клеток шахматной доски
# и выводит сообщение о том, являются ли эти клетки одного цвета.
# Столбцы на шахматной доске обозначаются английскими строчными буквами.

# Программа должна выводить YES, когда клетки одного цвета, NO - разного.
# Гарантируется, что значение колонок это латинские буквы abcdefgh,
# а строки это символы цифр от 1-8
#
# Разбор Youtube Patreon Boosty
#
# Sample Input 1:
#
# a1
# b2
# Sample Output 1:
#
# YES
# Sample Input 2:
#
# f5
# c3
# Sample Output 2:
#
# NO
# Sample Input 3:
#
# e5
# e4
# Sample Output 3:
#
# NO
# Sample Input 4:
#
# g7
# g8
# Sample Output 4:
#
# NO


# print('YES' if sum(*[map(ord, [i for i in input()])]) % 2 == sum(*[map(ord, [i for i in input()])]) % 2 else 'NO')
# print(('YES', 'NO')[int(input() + input(), 19) & 1])

print('YES' if not (sum(map(ord, input())) + sum(map(ord, input()))) % 2 else 'NO')