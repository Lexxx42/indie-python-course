# Метод подсчета. Сортировка подсчетом в Python

# Метод подсчета используется для нахождения количества элементов в списке,
# при условии если вам известно в каких пределах будут значения элементов списка.
# Зная сколько раз каждое значение встречается в списке, мы можем получить отсортированный список.
# Поэтому метод подсчета используется при одноименной сортировке

# Продемонстрируем метод подсчета на практике.
# Есть список из чисел от 0 до 5, в котором числа могут повторяться.
# Задача – подсчитать сколько раз встретилось каждое число в списке.
# При этом не используя методы списка.

a = [0, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]

# Поскольку у нас в этом списке могут быть только 6 значений из множества (0, 1, 2, 3, 4, 5),
# то создадим дополнительный список из 6 нулей.
# При этом, индексы этого списка совпадают с возможными значениями нашего первого списка.
# Поэтому элемент с нулевым индексом нового списка соответствует количеству нулей в первом списке,
# элемент с первым индексом второго списка отвечает за количество единиц в первом списке и т.д.
# И всё, что осталось – пройтись по первому списку и, например, если нам встречается 0,
# то увеличить число, стоящее на нулевом индексе второго списка, на 1.
# Наш код в итоге должен выглядеть следующим образом:

a = [0, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]
count = [0] * 6
for i in a:
    count[i] += 1
print(count)  # [1, 2, 5, 5, 1, 1]

# Чтобы было более понятно как это работает, можно запустить программу в режиме отладки.
# В нём видно, какие значения принимает i в определенном моменте
# и как выполняется count[i] += 1 по ходу работы всего кода.

# При этом может быть так, что какого-то из указанных чисел не будет и вовсе.
# Например в списке ниже отсутствует 0

a = [2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]
count = [0] * 6
for i in a:
    count[i] += 1
print(count)  # [0, 2, 6, 5, 1, 1]

# При запуске такого же кода, только с таким списком мы получим: [0, 2, 6, 5, 1, 1]
# Как мы видим, теперь нулевой элемент равен 0,
# что говорит о том, что нулей в этом списке нет.
# Так что программа работает так, как и должна.

# Результат программы можно использовать для простого вывода,
# т.е. вывести сколько раз встретилось каждое число.
# Это можно сделать с помощью второго цикла for после первого.
# Код будет выглядеть следующим образом:

print('qqqqqqq')
a = [2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]
count = [0] * 6
for i in a:
    count[i] += 1
for i in range(6):
    print(i, count[i])

# Где первое число в строке – число из списка,
# а второе число – в каком количестве это число встретилось в списке.

# Также можно сделать проверку, чтобы убрать вывод тех значений,
# которые не встретились в нашем списке.
# Для этого добавим условный оператор во второй цикл:

print('ooooooo')
a = [2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]
count = [0] * 6
for i in a:
    count[i] += 1
for i in range(6):
    if count[i] > 0:
        print(i, count[i])

# Также при помощи цикла мы можем раскрыть наш список и отсортировать его по возрастанию:

print('------')
a = [2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]
count = [0] * 6
for i in a:
    count[i] += 1
for i in range(6):
    if count[i] > 0:
        print((str(i) + " ") * count[i])

# Рассмотрим ещё одну задачу,
# где дана строка и нужно подсчитать сколько раз каждая буква встречалась в строке.
# При этом не имеет разницы большая буква или нет.

s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"

# Создадим список из такого же числа нулей, как и букв в английском алфавите:

letters = [0] * 26

# И здесь на нулевой позиции подсчитываем количество раз,
# когда встретилась буква a, на первой позиции – буква b и т.д.
# Для того, чтобы убрать разницу между большими и маленькими буквами воспользуемся методом lower(),
# а так же отсечём условным оператором все символы, которые не являются буквами.

# Код будет иметь вид:

print('+++++++')
s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
letters = [0] * 26
for i in s.lower():
    if i >= "a" and i <= "z":
        print(i)

# Этот код позволит вывести все те символы из строки, которые нам нужны.
# Нам осталось только установить соответствие: a = 0, b = 1 и т.д.

# Для этого нужно воспользоваться функцией ord,
# которая принимает символ и возвращает его порядковый номер в кодировке ASCII.
# Для проверки в каком диапазоне находятся наши символы
# мы можем ввести в эту функцию по очереди крайние наши символы:

print("\n================================")
print(ord("a"))
print(ord("z"))

# Получается, что наши символы букв имеют коды от 97 до 122,
# а индексы списка лежат в пределах от 0 до 25

# В итоге, чтобы получить нужные нам значения,
# нужно отнимать от получившихся значения число 97 (ord("a") = 97,
# чтобы получить 0 необходимо 97-97, ord("z") = 122,
# чтобы получить 25 необходимо 122-97).

# В итоге наш код будет иметь следующий вид:

print('________')
s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
letters = [0] * 26
for i in s.lower():
    if i >= "a" and i <= "z":
        nomer = ord(i) - 97
        letters[nomer] += 1
for i in range(26):
    if letters[i] > 0:
        print(i, letters[i])

# При выводе мы видим не буквы, а номера из-за того,
# что мы подстроили каждую букву под номер индекса.
# Теперь ввернём буквы, для этого существует схожая с ord() функция – chr(),
# которая из определенного номера выводит его символ в ASCII,
# стоит так же не забывать, что мы отнимали 97, так что мы теперь должны прибавить это число.
# В итоге наш код будет следующим:

print("\n================================")
s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
letters = [0] * 26
for i in s.lower():
    if i >= "a" and i <= "z":
        nomer = ord(i) - 97
        letters[nomer] += 1
for i in range(26):
    if letters[i] > 0:
        print(chr(i + 97), letters[i])

# Также мы можем отсортировать нашу строку:
print('_________')
s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
letters = [0] * 26
for i in s.lower():
    if i >= "a" and i <= "z":
        nomer = ord(i) - 97
        letters[nomer] += 1
for i in range(26):
    if letters[i] > 0:
        print(chr(i + 97) * letters[i], end="")

# Обратите внимание,
# что в этой задаче мы использовали смещение
# (сначала мы в ord() отнимали 97,
# а потом делали обратную операцию другим смещением - в chr() прибавляли 97).

# Смещение может понадобиться и в следующем примере.
# Заполним список случайными числами в пределах от -10 до 10.

print("\n================================")
import random

a = []
for i in range(10):
    a.append(random.randint(-10, 10))
print(a)

# В нашем списке присутствуют отрицательные значения, но индексы списка начинаются с нуля.
# Что в таком случае делать?
# Необходимо изначально посчитать сколько всего элементов может быть на данном промежутке.
# Их у нас 10 положительных, 10 отрицательных и 0 – в итоге 21.
# Создадим список count, состоящий из 21 нуля.

count = [0] * 21

# В итоге нулевой индекс отвечает за число -10,
# первый индекс за -9 … и 20 индекс отвечает за число 10.

# Значит нужно значение -10 превратить в индекс 0, -9 в 1 и т.д.
# Здесь мы видим, что необходимо сместить значение на +10.
# Таким образом код должен быть следующим:

import random

a = []
for i in range(10):
    a.append(random.randint(-10, 10))

count = [0] * 21
for i in a:
    count[i + 10] += 1
print(a)

for i in range(21):
    if count[i] > 0:
        print(i - 10, count[i])

# Здесь мы получили список из случайных элементов,
# а после идёт подсчёт сколько раз этот элемент встречался в списке.

# Таким образом, метод подсчёта позволяет найти сколько раз определенное значение встречалось в списке.
# Но у этого метода есть свои ограничения:

# необходимо знать в каких пределах элементы могут находиться
# (от этих пределов зависит размер побочного списка)
# даже если пределы известны, но они будут очень большими,
# то такой способ будет нецелесообразным, поскольку побочный список будет занимать слишком много памяти.