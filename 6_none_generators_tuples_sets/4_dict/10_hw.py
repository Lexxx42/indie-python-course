# Напишите программу, которая печатает словарь alphabet,
# где ключи  - строчные английские символы,
# а значения - порядковые номера букв в алфавите начиная с 1.
#
# Начало вашего словаря должны быть таким {"a": 1, "b": 2 ... }
#
# В качестве ответа распечатайте полученный словарь alphabet
#
# Весь английский алфавит можно взять в переменной ascii_lowercase из модуля string:
#
from string import ascii_lowercase as a

print(alphabet := {a[i]: i + 1 for i in range(len(a))})
