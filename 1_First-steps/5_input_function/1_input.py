# Функция input()

# Очень часто при написании программы нужно запрашивать какую-либо информацию у пользователя.
# И после того, как он введет необходимые данные, их нужно сохранить в программе.

# inputs -> process -> outputs

# На схеме под словом process понимается наша программа,
# она будет получать каким-то образам входные данные inputs
# и в зависимости от них вычислять выходные значения outputs.

# Для обработки пользовательского ввода в python существует функция input().

# a = input('a: ')
# print(a)
# print(type(a))
#
# b = int('2')
# print(b)
# # c = int('2.2')  # ValueError: invalid literal for int() with base 10: '2.2'
# # print(c)
# c = int(input('c: '))
# print(c)
#
# d = float(input('d: ').replace(',', '.'))
# print(d)


# Данные, введенные пользователем, попадают в программу в виде строки,
# поэтому и работать с ними можно так же, как и со строкой.
# Если требуется организовать ввод числа, то строку можно
# преобразовать в нужный формат с помощью функций явного преобразования типов.

# Если вам необходимо ввести целое число и сохранить его в переменную d,
# необходимо поступить следующим образом:

# >>> d=int(input())
# 123
# >>> type(d)
# class 'int'
# >>> d+2
# 125

# Оборачивая input() функцией int(), мы преобразуем введенную строку в целое число.
# Но будьте аккуратны! Если пользователь введет символы,
# которые нельзя преобразовать к целому числу, получите ошибку ValueError.

# d=int(input())
# 15sdf4
# Traceback (most recent call last):
#     d=int(input())
# ValueError: invalid literal for int() with base 10: '15sdf4'

# Если вам необходимо ввести вещественное число и сохранить его в переменную q,
# необходимо обернуть функцию input() в функцию float():
# >>> q=float(input())
# 4.5
# >>> q
# 4.5
# >>> type(q)
# class 'float'

# Задача: найти периметр треугольника

print('perimeter triangle')

a, b, c = map(int, input().split())
print(a + b + c)
