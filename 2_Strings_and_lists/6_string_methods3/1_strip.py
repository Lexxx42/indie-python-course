# Метод strip
# Метод .strip имеет следующий шаблон вызова:

# S.strip([chars])
# Метод  .strip возвращает копию строки, удаляя как начальные,
# так и конечные символы (в зависимости от переданного строкового аргумента).
# Метод удаляет символы как слева, так и справа в зависимости от аргумента chars.
# Если аргумент chars не передан,
# то по умолчанию удаляться пробелы и символы переноса на новую строку \n.

q = '    hello    '
print(q)
print(q.strip())
print('\n\n\n_USB_\n\n\n\n'.strip())
print('123_USB_123'.strip('123'))

# Символы в параметре chars рассматриваются не как последовательность,
# а как набор символов, которые необходимо удалить:

print('321232321_USB_31121312'.strip('123'))

# Метод rstrip
#  Метод .rstrip имеет следующий шаблон вызова:
# S.rstrip([chars])

# Метод .rstrip возвращает копию строки,
# в которой справа удалены указанные символы
# (по умолчанию удаляются пробельные символы).

print("***")
q = '    hello    '
print(q)
print(q.rstrip())
print('\n\n\n_USB_\n\n\n\n'.rstrip())
print('123_USB_123'.rstrip('123'))
print('321232321_USB_31121312'.rstrip('123'))

# Метод lstrip
#  Метод .lstrip имеет следующий шаблон вызова:
# S.lstrip([chars])
# Метод .lstrip возвращает копию строки,
# в которой слева удалены указанные символы
# (по умолчанию удаляются пробельные символы).

print("---")
q = '    hello    '
print(q)
print(q.lstrip())
print('\n\n\n_USB_\n\n\n\n'.lstrip())
print('123_USB_123'.lstrip('123'))
print('321232321_USB_31121312'.lstrip('123'))