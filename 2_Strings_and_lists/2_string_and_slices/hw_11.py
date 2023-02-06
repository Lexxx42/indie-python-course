# На вход программе поступает строка, состоящая как из заглавных так из строчных букв.
# Ваша задача преобразовать строку так, чтобы первая буква у каждого слова стала маленькой,
# а остальные буквы превратились в заглавные. Символы пунктуации и цифры не нужно преобразовывать.

# В качестве ответа нужно вывести полученную строку

# 🚀>P.S.: Подсказка для решения 🚀
# Sample Input 1:

# Every You Every Me
# Sample Output 1:

# eVERY yOU eVERY mE
# Sample Input 2:

# RunnING up That HILL
# Sample Output 2:

# rUNNING uP tHAT hILL
# Sample Input 3:

# Sleeping with GHOSTS
# Sample Output 3:

# sLEEPING wITH gHOSTS

# print(input().title().swapcase())

print(" ".join((lambda *x: [j[0].lower() + j[1:].upper() for j in x])(*input().split())))
