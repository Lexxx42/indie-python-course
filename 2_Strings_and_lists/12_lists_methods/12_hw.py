# Напишите программу,
# которая выводит слова введённой строки
# (части, разделённые символами пустого пространства) в столбик.
# Нужно обойтись только методами split и join у строк,
# в программе должен быть всего один вызов print.

# Sample Input:

# Буря мглою небо кроет
# Sample Output:

# Буря
# мглою
# небо
# кроет

# [print(x) for x in input().split()]

print(*input().split(), sep='\n')
