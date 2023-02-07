# Метод count

# Данный метод переводится как количество.
# С помощью метода count вы можете посчитать сколько раз вам встретилась строка sub в строке S.

s = 'hello world'
print(s.count('l'))  # сколько раз встретится буква 'l' в строке

# Обратите внимание на следующее: когда вы пишете метод .count и открываете скобку,
# то появляется подсказка.
# В ней говорится о том сколько аргументов вам нужно передать.
# Sub обозначает подстроку и заметьте, что он стоит не в квадратных скобках,
# в отличие от start и end - он является обязательным аргументом.
# Следующий параметр start, так как находится квадратных скобках,
# является необязательным аргументом.
# А end вообще находится в двух квадратных скобках
# - он является еще более необязательным, чем start.

s = 'hello world'

# сколько раз встретится буква 'l' в строке
# со 2-го по 6-й символ включительно
print(s.count('l', 2, 7))

# Метод .count используется очень часто, его вы обязаны знать.

# Время практики
# На вход программе поступает строка,
# ваша задача подсчитать сколько раз в ней встречается латинская буква "e".
# При этом стоит учитывать как маленькие, так и заглавные буквы.

# Sample Input 1:

# Helen
# Sample Output 1:

# 2
# Sample Input 2:

# Everywhere
# Sample Output 2:

# 4

print(input().lower().count("e"))
