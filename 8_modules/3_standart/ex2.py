# Импортируйте имя Template из модуля string, чтобы код ниже заработал

from string import Template

values = {'one': 'Привет', 'copter': 'Квадракоптер'}

t = Template("""
Ну что, мои хорошие, всем $one
Это шаблонная строка
В нее можно вставлять значения по ключам
Хочу сюда вставлю слово $copter, хочу сюда $copter
""")

print(t.substitute(values))

# Импортируйте стандартный модуль sys и при помощи функции getrecursionlimit узнайте лимит предела рекурсии. Его необходимо вывести на экран

from sys import getrecursionlimit

print(getrecursionlimit())

# Из модуля string импортируйте следующие переменные:
#
# ascii_lowercase - строка, содержащая английский буквы англ. алфавита в нижнем регистре
# ascii_uppercase - строка, содержащая английский буквы англ. алфавита в верхнем регистре
# punctuation - строка, содержащая символы пунктуации
# Необходимо в отдельных строках вывести сперва все знаки пунктуации, затем заглавные символы и уже потом маленькие.

from string import ascii_lowercase, ascii_uppercase, punctuation

print(punctuation)
print(ascii_uppercase)
print(ascii_lowercase)


