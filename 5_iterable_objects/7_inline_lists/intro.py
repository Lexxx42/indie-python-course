# Вложенные списки

# Вложенный список – это список, элементами которого являются также списки. Например:

a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]

# Не забывайте расставлять пробелы между элементами согласно стандарту pep8,
# в pycharm для этого можно нажать комбинацию ctrl+alt+L и среда разработки все сделает за вас.

# Теперь найдём длину нашего списка:

a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]
print(len(a))  # 3
print(a[2])  # [3, 10, 17, 19]
print(a[2][1])  # 10

# еперь при вызове a[2] будем получать список:
# [3, 10, [14, 15, 16], 17, 19], а при вызове a[2][2] будем получать список: [14, 15, 16]
# Чтобы обратиться к числу 15 нам теперь нужно использовать тройную индексацию a[2][2][1]

# Так как строки представляют собой коллекцию из символов,
# то список из строк тоже можно считать вложенной структурой

b = ["hello", "hi", "world"]
print(b[2])  # world
print(b[2][0])  # w

# С виду наш список b не является вложенным,
# однако мы должны помнить, что у каждого символа строки есть номер,
# поэтому мы можем обратиться как к слову world целиком,
# так и к его любому символу, например, к букве w.

# Поэтому стоит запомнить, что строка внутри списка так же является вложенным элементом.

# Теперь рассмотрим вложенные списки, состоящие из чисел и у которых вложенность элементов равна 2.
# Такие списки также называют таблицами или матрицами(нет, речь идет не о фильме)

# Чтобы разглядеть в нашем списке a таблицу сделаем несколько переносов:

a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]

# Обход элементов вложенного списка

# Научимся обходить все элементы данного списка. Здесь, как и в обычных списках, существует 2 варианта обхода:
#
# обход по значению
# обход по индексу.

# Обход по значению:

a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]
for i in a:
    for j in i:
        print(j, end=" ")
    print()

# Для более подробного рассмотрения алгоритма выполнения данного кода можно запустить его в режиме отладки.
# Где мы увидим, что в переменную i записался первый вложенный список,
# а в переменную j по очереди передаются элементы списка i, после чего они выводятся.
# По завершению вывода всех элементов списка,
# переменная i принимает значение следующего списка и так до тех пор, пока не закончатся все элементы списка a.

# Но здесь присутствуют всё те же проблемы обхода списка по значениям: нельзя узнать номер элемента в списке,
# а также нельзя повлиять на значение списка.
# И так же, как и в обычных списках,
# эти проблемы можно решить при помощи обхода элементов списка по его индексам.

# Для этого обхода сначала представим наш список в виде таблицы,
# где прономеруем каждую строчку с 0 до 2, как и каждый столбец с 0 до 3.

# И нам нужно обойти элементы в порядке слева-направо, сверху-вниз.
# При обращении к каждому элементу перед выводом необходимо использовать две пары квадратных скобок,
# где первая указывает на строку, а вторая на столбец.,
# т.е. наш 0 лежит под индексом [0][0], следующая за ним 2 – под индексом [0][1],
# последнее число – 19 находится под индексом [2][3].
# Значит мы при таком подходе фиксируем номер строки и для неё перебираем каждый номер столбца.

a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]
for i in range(3):
    for j in range(4):
        print(a[i][j], end=" ")
    print()

# 0 2 4 6
# 1 5 9 13
# 3 10 17 19

# В итоге мы получили тот же результат,
# но при таком варианте обхода мы можем спокойно менять значения элементов.
# Например, увеличим все значения на 10 и после цикла выведем список a.

a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]
for i in range(3):
    for j in range(4):
        a[i][j] += 10
        print(a[i][j], end=" ")
    print()
print(a)

# 10 12 14 16
# 11 15 19 23
# 13 20 27 29
# [[10, 12, 14, 16], [11, 15, 19, 23], [13, 20, 27, 29]]

# Как мы видим, значения изменились как при обычном их выводе, так и при выводе списка, в котором они находятся.
# При обходе по индексам мы так же можем идти в другом направлении, например, можно двигаться сверху-вниз,
# а потом слева-направо, т.е. сначала будет выведено 0 1 3, потом 2 5 10 и т.д.

a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]
for j in range(4):
    for i in range(3):
        print(a[i][j], end=" ")
    print()

# 0 1 3
# 2 5 10
# 4 9 17
# 6 13 19

# Можно так же обходить элементы справа-налево,
# начиная снизу и двигаясь вверх, т.е. сначала получим 19 17 10 3,
# потом 13 9 5 1 и т.д.
# Для это в функции range нужно указать убывающую прогрессию до -1,
# т.к. -1 не учитывается и доходим только до 0.

a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]
for i in range(2, -1, -1):
    for j in range(3, -1, -1):
        print(a[i][j], end=" ")
    print()

# 19 17 10 3
# 13 9 5 1
# 6 4 2 0

# Таким образом, мы видим, что элементы матрицы можно обойти в любом порядке.
# Но самый часто используемый вариант обхода – обход слева-направо двигаясь сверху вниз.

# Нахождение суммы строк или столбцов матрицы

# Где это может пригодиться? Допустим, нам нужно посчитать сумму каждой строки и каждого столбца.
# Для нахождения суммы строк лучше добавить новую переменную для вычисления суммы,
# которая будет обнуляться при переходе к новой строке.
# Код будет иметь следующий вид:

a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]
for i in range(3):
    sum = 0
    for j in range(4):
        sum += a[i][j]
    print(sum)

# 12
# 28
# 49

# Мы можем проверить результат: 0+2+4+6 = 12, 1+5+9+13=28 и т.д.
# Для нахождения суммы по столбцам необходимо поменять два эти цикла местами и больше ничего менять не нужно:

a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]
for j in range(4):
    sum = 0
    for i in range(3):
        sum += a[i][j]
    print(sum)

# Мы можем проверить результат: 0+1+3 = 4, 2+5+10=17 и т.д.

# Заполнение вложенного списка

# Теперь рассмотрим, как можно заполнить вложенный список.
# Для этого необходимы две переменные, которые будут обозначать количество строк n и столбцов m.
# Если нужно заполнить конкретным значением, допустим 0,
# то для этого можно воспользоваться циклом, в котором будем n раз добавлять список [0] * m раз.
# И для проверки выведем элементы списка a через новый цикл for.

a = []
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
for i in range(n):
    a.append([0] * m)
for i in a:
    print(i)

# Также можно вместо нуля в список внести любое другое значение.
# Если же нужно в список вносить значения, вводимые с клавиатуры,
# то необходимо действовать иначе: нужно создать промежуточный список и во вложенном цикле добавлять то,
# что вводите с клавиатуры, после завершения внутреннего цикла,
# этот новый список добавляем в наш изначальный:

a = []
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
for i in range(n):
    b = []
    for i in range(m):
        b.append(int(input('Введите элемент: ')))
    a.append(b)
for i in a:
    print(i)

# Квадратная матрица

# Очень часто вы будете иметь дело именно с квадратными таблицами, т.е. размерностью n на n.
# В таких таблицах имеется главная диагональ,
# которая идёт из элемента [0][0] по пути [1][1], [2][2] и так до элемента [n][n].
# Следовательно, у элементов главной диагонали номер строки совпадает с номером столбца, т.е. [i] = [j]
#
# Эта диагональ делит матрицу на 2 треугольника.
# Первый треугольник состоит из элементов, расположенных выше главной диагонали:
# с элементами по индексу [0][1], [0][2], [1][2].
# Второй треугольник с элементами по индексу [1][0], [2][0], [2][1].

# В этих треугольниках наблюдается одна особенность:
# У верхнего треугольника i < j, т.е. номер строки меньше номера столбца,
# а у нижнего треугольника i > j, т.е. номер строки больше номера столбца.

# Теперь рассмотрим следующий пример: на главной диагонали будут лежать 10, ниже будут 3, а выше – 5.
# Для этого сначала заполним матрицу нулями и проверим правильность заполнения:

a = []
n = int(input('Введите размер квадратной матрицы: '))
for i in range(n):
    a.append([0] * n)
for i in a:
    print(i)

# Как мы видим, всё работает исправно.
# Теперь чтобы изменить значения в этой таблице необходимо обходить их по индексам:

a = []
n = int(input('Введите размер квадратной матрицы: '))
for i in range(n):
    a.append([0] * n)

for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 10
        elif i > j:
            a[i][j] = 3
        else:
            a[i][j] = 5
for i in a:
    print(i)

# Получаем нужный нам ответ.
# В этой программе у нас есть цикл для заполнения таблицы,
# затем вложенный цикл для обработки, и цикл для вывода.

# Как организовать считывание данных в матрицу

# Теперь давайте разберемся как нам считывать данные в виде матриц для решения задач.
# Вот посмотрите пример входных данных

# Здесь первое число представляет собой количество строк в матрицы,
# затем будут идти 5 строк, содержащие элементы каждой отдельной строки матрицы.
#
# Для обработки такого ввода нужно обратить внимание,
# что каждая отдельная строка представляет собой обычный список.
# Для считывания одномерного (невложенного) списка из чисел мы пользовались следующей инструкцией:

list(map(int, input().split()))

# Результат этого считывания мы можем складывать в цикле в отдельный список
# и тогда на выходе мы получим уже вложенную конструкцию, которая и будет представлять собой матрицу

matrix = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

print(matrix)

# В примере выше цикл повторяется 3 раза, значит на выходе мы получим матрицу, состоящую из трех рядов.
#
# Для считывания n-строк матрицы вместо вы можете воспользоваться следующим кодом

n = int(input('Введите количество строк матрицы: '))
matrix = []
for i in range(n):
    matrix.append(
        list(map(int, input(f"Введите элементы {i} строки: ").split()))
    )
print(matrix)

print('------Вывод матрицы построчно------')

for row in matrix:
    print(row)
