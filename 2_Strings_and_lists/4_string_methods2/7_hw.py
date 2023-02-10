# Напишите программу, которая проверяет,
# чтобы введенная фраза s одновременно начиналась
# со строки prefix и заканчивалась строкой postfix.

# Входные данные
# В отдельных строках вводится три значения: сперва строка s, затем строка prefix и потом postfix

# Выходные данные
# Нужно вывести True, если введенная строка s одновременно начинается со строки prefix
# и заканчивается строкой postfix.
# Во всех остальных случаях нужно вывести False. Регистр букв нужно учитывать

# Sample Input 1:

# translate russian to english
# translate
# english
# Sample Output 1:

# True
# Sample Input 2:

# translate russian to english
# translate
# SH
# Sample Output 2:

# False
# Sample Input 3:

# TRanSlate russian to english
# TRa
# lish
# Sample Output 3:

# True

print((s:=input()).startswith(input()) and s.endswith(input()))
