# Упражнение на строки

# Петя записался в кружок по программированию.
# На первом занятии Пете задали написать простую программу.
# Программа должна делать следующее:
# в заданной строке, которая состоит из прописных и строчных латинских букв, она:

# удаляет все гласные буквы,
# перед каждой согласной буквой ставит символ ".",
# все прописные согласные буквы заменяет на строчные.

# Гласными буквами считаются буквы A, O, Y, E, U, I,
# а согласными — все остальные.
# На вход программе подается ровно одна строка,
# она должна вернуть результат в виде одной строки, получившейся после обработки.

# Решение Youtube Patreon Boosty

# Sample Input 1:

# Codeforces
# Sample Output 1:

# .c.d.f.r.c.s
# Sample Input 2:

# g
# Sample Output 2:

# .g
# Sample Input 3:

# Ba
# Sample Output 3:

# .b
# Sample Input 4:

# baa
# Sample Output 4:

# .b
# Sample Input 5:

# aab
# Sample Output 5:

# .b


print(''.join('.' + ch for ch in input().lower() if ch not in 'aoyeui'))