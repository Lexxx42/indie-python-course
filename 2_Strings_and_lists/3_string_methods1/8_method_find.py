# Методы для поиска элементов в строке

# Абсолютно все методы из этого раздела вы обязаны знать

# Метод find

# Метод .find имеет следующий шаблон вызова:
# S.find(sub[, start[, end]])
# Метод .find возвращает индекс первого слева вхождения строки sub в строке S.
# Подстрока sub ищется на всем срезе строки S.
# Но вы можете указать интервал поиска, передав второй и третий аргументы.
# Метод .find вернет значение -1, если ничего не будет найдено.

s = 'hello world'
print(s.find('o'))
print(s.find('ll'))
print(s.find('o', 5))
print(s.find('x'))

# Метод rfind

#  Метод .rfind имеет следующий шаблон вызова:
# S.rfind(sub[, start[, end]])
# Если вам необходимо искать с другого конца вашей строки
# то в таком случае можно использовать аналогичный метод rfind().
# Буква r обозначает слово right(справа) и, следовательно, поиск будет идти справа.
# Вы также можете ограничить интервал поиска, передав дополнительно параметры start и end

print("***")
s = 'hello world'
print(s.rfind('o'))
print(s.rfind('ll'))
print(s.rfind('o', 5))
print(s.rfind('x'))

# Метод index()

# Метод .index имеет следующий шаблон вызова:
# S.index(sub[, start[, end]])
# Метод  .index также возвращает индекс первой найденной подстроки, аналогично методу .find

print("===")
s = 'hello world'
print(s.index('o'))

# Но между ними есть разница: если вы будете искать подстроку,
# которой у вас нет, то метод index() вернет ошибку, то есть программа автоматически завершится.

print(s.index("W"))

# Traceback (most recent call last):
#   File "G:\indie-python\indie-course-of-python\2_Strings_and_lists\3_string_methods1\8_method_find.py", line 49, in <module>
#     print(s.index("W"))
#           ^^^^^^^^^^^^
# ValueError: substring not found
