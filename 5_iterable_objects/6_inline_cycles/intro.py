# Вложенные циклы

# Цикл называется вложенным, если находится внутри другого цикла.
#
# Формат вложенных циклов:

# for <переменная> in <объект>:
#     for <переменная> in <объект>:
#         <действие>
#     <действие>

# В данном примере вложенным будет второй цикл,
# потому что он расположен внутри первого цикла, который будет называться внешним.

# Разберём принцип работы вложенных циклов на примере.
# Стоит сразу сказать, что для внутреннего цикла необходимо использовать другую переменную.
# Принято использовать букву j, однако это может быть и другая переменная.

for i in range(3):
    for j in range(5):
        print("*", end=" ")

# Если посчитать, то удостоверимся, что их 15,
# поскольку наш внешний цикл выполнился 3 раза
# и для каждого его обхода мы делали 5 раз внутренний цикл.
# Но можно сделать это в виде таблички,
# чтобы более детально видеть разницу в выполнении внутреннего и внешнего цикла.
# Для этого после внутреннего цикла сделаем перенос на новую строчку при помощи пустого принта.

print('================================================================')
for i in range(3):
    for j in range(5):
        print("*", end=" ")
    print()

# Здесь мы видим, как трижды выполнялся вложенный цикл, который должен 5 раз распечатать *.
# Также можно вместо звёздочки выводить что угодно, к примеру переменную i.
# При таком коде мы получим:

print("================================")
for i in range(3):
    for j in range(5):
        print(i, end=" ")
    print()

# Это говорит о том, что на протяжении выполнения внутреннего цикла,
# переменная внешнего цикла является неизменной.
# Когда мы изначально взяли значение 0 мы будем работать с нулём до тех пор,
# пока не выполнится всё тело внешнего цикла.
# Это означает, что мы будем выводить 5 раз подряд число 0
# и только после этого мы вернёмся в начало цикла и перейдём к 1.

# Если мы будем выводить переменную j, то получим уже другой результат:

print("================================")
for i in range(3):
    for j in range(5):
        print(j, end=" ")
    print()

# Как мы видим, мы выводим три раза числа в пределах от 0 до 5, т.е. переменную j.
# При этом в самом начале вложенного цикла в функцию range()
# можно подставить вместо переменной переменную i
# и посмотрим на то, какой будет результат при следующем коде.

print("================================")
for i in range(4):
    for j in range(i):
        print(j, end=" ")
    print()

# Обратите внимание на первую строчку:
# она пустая, поскольку переменная i была равна нулю, значит мы обходили в range(0),
# т.е. до нуля, что означает нисколько.
# Потом у нас был range(1) и делали цикл 1 раз, а потом в range(2) и делали его дважды.
# То есть если во внешнем цикле вместо 4 в range() вставить 10,
# то мы получим следующую лесенку из чисел:

print("\n================================")
for i in range(10):
    for j in range(i):
        print(j, end=" ")
    print()

# Этот цикл делается от 0 до 9 и выводить мы будем так же от 0 до 9, только не включая 9.
# Чтобы наши значения включались давайте начинать цикл с единицы по 10
# в первом цикле и с единицы по i+1 во втором цикле.

print("\n================================")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Теперь используем обе переменных, но сократим количество чисел:

print("\n================================")
for i in range(1, 4):
    for j in range(10, 13):
        print(i, j)

# Получается, что мы берём первое значение переменной i (1)
# и для него возьмутся все значения переменной j (10, 11, 12),
# потом берём следующее значение i (2) и для него опять все значения j (10, 11, 12) и т.д.

# Для более детального рассмотрения данного процесса можете запустить данную программу в отладчике,
# чтобы увидеть все шаги.
# Стоит запомнить, что общее количество повторений будет равняться
# произведению повторений внутреннего и внешнего цикла
# (например, в прошлом коде внешний цикл повторяется 3 раза, внутренний – так же 3, 3*3 = 9,
# как мы видим, у нас вывело 9 строк.
# Если увеличить количество повторения цикла внутри до 4 раз,
# то программа выведет уже 3*4 = 12 строчек.).

# Поэтому запомните, что каждое значение внутреннего цикла будет сочетаться
# с каждым значением внешнего цикла.
# То же самое будет, если перебирать строки:

print("################################")
for i in "ab":
    for j in "cde":
        print(i, j)

# Видим, что сначала буква a сочетается со всеми буквами со второй строки, а потом и буква b.

# Вложенные циклы часто используют для переборов всех возможных значений.
# Допустим, длина пароля – 3, состоит из маленьких и больших латинских букв,
# а также могут быть цифры и знаки пунктуации.
# Необходимо перебрать все возможные значения, которые могут являться паролем.

# Для решения подобной задачи импортируем из модуля string переменную printable.
# Для большего понимания посмотрим, что из себя представляет данная переменная:

print("\n================================")
from string import printable

print(printable)

# Теперь вернёмся к решению задачи:

# from string import printable
#
# for b1 in printable:
#     for b2 in printable:
#         for b3 in printable:
#             print(b1, b2, b3)

# После запуска программы получим все возможные сочетания этих символов.
# Ещё один пример: составим таблицу умножения.

for i in range(1, 11):
    for j in range(1, 10):
        print(i, "*", j, "=", i * j, end=" ")
    print()

# Как мы видим, в строке всё время первый множитель остаётся неизменным,
# меняется только второй.
# А в столбике наоборот – неизменным является второй множитель,
# а первый всё время меняется.
# Но в таблице умножения всё происходит иначе, а не как у нас:

# Нам нужен противоположный результат. Для этого немного изменим код:

print("123123123123123123")
for j in range(1, 10):
    for i in range(1, 11):
        print(i, "*", j, "=", i * j, end=" ")
    print()

# Рассмотрим пример из ЕГЭ по информатике:
# Сколько шестибуквенных слов, начинающихся и заканчивающихся согласной буквой
# и содержащих ровно 2 гласные можно составить из букв Т, Ы, К, В, А?
# Каждая из допустимых букв может входить в слово несколько раз.
# Эту задачу можно сделать при помощи цикла,
# и сразу переведём буквы в латиницу для более удобной работы.

for b1 in "tukva":
    for b2 in "tukva":
        for b3 in "tukva":
            for b4 in "tukva":
                for b5 in "tukva":
                    for b6 in "tukva":
                        rez = b1 + b2 + b3 + b4 + b5 + b6
                        if rez[0] in "tkv" and rez[-1] in "tkv":
                            if rez.count("a") + rez.count("u") == 2:
                                print(rez)

# Эта программа выведет все возможные комбинации,
# подходящие под условия задачи.
# Только осталось вместо вывода всех этих вариантов добавить счетчик и вывести его:

print("================================")
count = 0
for b1 in "tukva":
    for b2 in "tukva":
        for b3 in "tukva":
            for b4 in "tukva":
                for b5 in "tukva":
                    for b6 in "tukva":
                        rez = b1 + b2 + b3 + b4 + b5 + b6
                        if rez[0] in "tkv" and rez[-1] in "tkv":
                            if rez.count("a") + rez.count("u") == 2:
                                count += 1
print(count)  # Получим: 1944

# На ЕГЭ данную задачу нужно решить при помощи комбинаторики, но, как вы видите,
# в программировании можно это делать и при помощи перебора.
# Большим минусом такой программы является время исполнение этой программы,
# поскольку нужно произвести сочетание каждой буквы с каждой.
# А всего таких способов  в нашем случае 15625.

# Разберём ещё один пример, для которого нам нужен следующий код,
# который будет считать сумму цифр числа:

print("~!@#$%^&*()_")
# x = int(input())
x = 1944
s = 0
while x > 0:
    s += x % 10
    x //= 10
print(s)

# Например, если ввести 123, то получим 6
# В другом файле у нас есть цикл for,
# который перебирает значения в большом диапазоне
# и нам необходимо в таком диапазоне посчитать сумму цифр этих чисел.
# И раз у нас уже есть код для подсчёта суммы цифр числа, то можно его вставить в цикл for

print("================================")
for i in range(1, 100001):
    x = i
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    print(i, s)

# Получим число и сумму его цифр от 1 до 100000 включительно
# В этом примере мы так же видим, что вложенным циклом может быть не только цикл for, но и while
# У вложенных циклов так же есть очень хорошее
# применение – они используются при обходе элементов вложенных списков.
# Об этом мы поговорим в следующем видео.