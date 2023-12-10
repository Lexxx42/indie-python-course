# Напишите функцию first_unique_char, которая принимает строку символов и возвращает целое число: позицию первого уникального символа в строке. В случае, если уникальных символов в переданной строке нет, верните -1. Регистр символов не учитывайте.
#
# Ваша задача написать только определение функции first_unique_char
#
# Sample Input 1:
#
# python
# Sample Output 1:
#
# 0
# Sample Input 2:
#
# abracadabra
# Sample Output 2:
#
# 4
# Sample Input 3:
#
# abcabc
# Sample Output 3:
#
# -1
# Sample Input 4:
#
# aasssddddddddq
# Sample Output 4:
#
# 13


def first_unique_char(s):
    uniq_index = -1
    for char in s:
        if s.count(char) == 1:
            return s.index(char)
    return uniq_index


s = 'abcabc'
print(first_unique_char(s))
