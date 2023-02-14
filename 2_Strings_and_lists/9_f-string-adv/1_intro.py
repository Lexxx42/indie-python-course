# Вывод переменных

# Мы знаем теперь как при помощи f-строки вывести имя переменной и ее значение.
# Вот можете полюбоваться примером ниже:
x = 14
y = 17
print(f"x = {x}, y = {y}")

# Но начиная с версии Python 3.8 функционал f-строк был дополнен
# новой возможностью по выводу имён переменных и их значений.
# Посмотрите как теперь это можно сделать:

x = 11
y = 98
print(f"{x=}, {y=}")
# пробелы будут учтены
print(f"{x  =}, {y= }")
