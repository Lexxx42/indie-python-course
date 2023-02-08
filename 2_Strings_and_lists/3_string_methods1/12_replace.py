# Метод replace
# Метод .replace имеет следующий шаблон вызова:

# S.replace(old, new[, count])

# Возвращает копию исходной строки S,
# в которой все подстроки old заменены на подстроки new.
# Обратите внимание, что у метода .replace два обязательных параметра:
# old - это то, что мы будем менять, new - на что мы будем менять.
# Но можно передать третий необязательный параметр - максимальное количество замен,
# которое будет сделано.

s = 'hello world'
print(s.replace('e', 'a'))
print(s.replace(' ', ''))
print(s.replace('l', '?', 2))

# Метод .replace используется очень часто, его вы обязаны знать.

# Время практики
# Программа получает на вход фразу, состоящую из нескольких слов, разделенных пробелом.

# Ваша задача заменить все пробелы запятыми и вывести полученную строку.

# Sample Input 1:

# Smells Like Teen Spirit
# Sample Output 1:

# Smells,Like,Teen,Spirit
# Sample Input 2:

# a million little pieces
# Sample Output 2:

# a,million,little,pieces

print(input().replace(" ", ","))
