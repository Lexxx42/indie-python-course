# Методы списков

# С методами мы уже с вами сталкивались при изучении строк,
# но строки были неизменяемые объекты, а списки наоборот.
# Поэтому использование практически каждого метода списка
# будет влиять на сам список без явного присваивания.
# Давай взглянем

# Метод append
# Первый метод с которым мы познакомимся называется .append.
# Он имеет следующий шаблон вызова:
# L.append(x)
# Метод .append обязательно принимает одно значение x
# и добавляет его в качестве нового элемента в конец списка L.
# Следовательно размер списка увеличивается на одно значение.
# Никакого присвоения в переменную, как в случае со строками, здесь не требуется.

a = [34, 23, 12, 28, 9, 15]
print(a)  # [34, 23, 12, 28, 9, 15]
a.append(1)
print(a)  # [34, 23, 12, 28, 9, 15, 1]

# Метод clear
# Следующий метод это .clear. У него следующий формат вызова:
# L.clear()
# Метод .clear не принимает никаких аргументов
# и делает список L пустым, удаляет все его элементы.

print('---')
a = [34, 23, 12, 28, 9, 15]
print(a)  # [34, 23, 12, 28, 9, 15]
a.clear()
print(a)  # []

# Метод copy
# Метод .copy имеет следующий формат:
# L.copy()
# Метод .copy не принимает аргументов,
# делает копию списка - создается совершенно новый объект в памяти,
# он тоже является списком и будет состоять из таких же элементов,
# как и оригинальный список, но у нового списка будет другой идентификатор.

# Копию списка также можно получить через полный срез.

print('+++')
a = [34, 23, 12, 28, 9, 15]
b = a.copy()
print(a)  # [34, 23, 12, 28, 9, 15]
print(b)  # [34, 23, 12, 28, 9, 15]

print('-' * 10)

a[0] = 3
print(a)  # [3, 23, 12, 28, 9, 15]
print(b)  # [34, 23, 12, 28, 9, 15]

# Метод count
# Метод .count имеет следующий формат:
# L.count(x)
# Принимает обязательно один аргумент.
# При помощи метода .count можно посчитать
# сколько раз встретилось в списке переданное значение.

print('@@@')
a = [34, 23, 12, 28, 9, 15, 23, 2, 23]
print(f'23 встречается {a.count(23)} раз')
print(f'12 встречается {a.count(12)} раз')
print(f'24 встречается {a.count(24)} раз')

# Метод extend
# Метод .extend имеет следующий формат:
# L.extend(iterable)
# Метод .extend принимает обязательно один аргумент - итерабельную последовательность.
# Здесь нам придется забежать немного вперед,
# потому что данную тему мы еще не разбирали.
# Итерабельную последовательность состоит из нескольких элементов,
# поэтому списки и строки являются такой последовательностью.
# При помощи метода .extend можно добавить сразу все элементы из итерируемой
# последовательности в конец списка L.
# Значит метод .extend позволяет добавлять много элементов за один раз,
# вот его отличие от метода .append

print('***')
a = [34, 23, 12, 28, 9, 15]
print(a)
a.extend([23, 12])
print(a)
a.extend('hello')
print(a)

# Метод index
# Метод .index имеет следующий формат:
# L.index(x, [start [, end]])
# Метод .index находит переданный элемент x в списке L
# и возвращает его индекс.
# Если в списке находится несколько элементов,
# равных значению x, то будет возвращен индекс первого из них.
# Если список не содержит переданный элемент x,
# будет вызвано исключение ValueError.
# У метода есть необязательные параметры start и end :

# * Если задан индекс start то первое вхождение значения x будет искаться начиная с индекса start.
# * Если заданы индексы start и end, то первое вхождение значения x будет искаться начиная
# с индекса start и перед индексом end. Индекс start включается, а индекс end не включается

print('%%%')
a = [34, 23, 12, 28, 23, 2, 23]
print(a.index(23))
print(a.index(12))
print(a.index(23, 1))
print(a.index(23, 2))
print(a.index(23, 2, 5))

# Метод insert
# Метод .insert имеет следующий формат:
# L.insert(index, value)
# Метод .insert выполняет вставку нового значения в список на определенную позицию.
# Метод .insert должен принимать два значения:
# index  - индекс куда вставляем новое значение и
# value - что нужно ставить, то есть само значение.

print('AAA')
a = [34, 23, 12, 28, 23]
a.insert(1, 99)
print(a)

# Метод pop
# Очень полезный метод .pop. У него следующий формат вызова:
# L.pop([index])
# Метод .pop возвращает значение элемента с индексом index,
# а также удаляет его из списка L.
# По сути метод выполняет изъятие из списка элемента, стоящего на позиции index
# Необязательный аргумент - индекс index по умолчанию равен -1.
# Так что по умолчанию эта операция производит действие с последним элементом последовательности.
# Вы можете передать значение индекса для изъятия элемента

print('===')
a = [34, 23, 12, 28, 23]

a.pop()
print(a)  # [34, 23, 12, 28]

b = a.pop()
print(b)  # 28
print(a)  # [34, 23, 12]

print(a.pop())  # 12
print(a)  # [34, 23]

print(a.pop(0))  # 34
print(a)  # [23]

# Метод .pop вызывает IndexError,
# когда передать несуществующий индекс или попытаться извлечь элемент из пустого списка.

# Метод remove
# Метод .remove имеет следующий формат:
# L.remove(x)
#  Слово remove переводится как «удалить»,
#  но этот метод, в отличие от метода .pop, удаляет по значению.
#  Вы должны обязательно передать одно значение x.
# Метод .remove производит удаление первого элемента,
# значение которого равно x из списка L.
# Длина списка уменьшается на единицу, элементы,
# стоящие справа от удаленного, смещаются влево на одну позицию.
# Если в списке L есть несколько элементов равных значению x,
# удалиться только первый найденный слева элемент.
# За один вызов метода удаляется один элемент,
# если нужно удалить несколько элементов, нужно несколько раз вызвать метод .remove

print('^^^')
a = [34, 23, 12, 28, 23, 34]
a.remove(34)
print(a)  # [23, 12, 28, 23, 34]
a.remove(34)
print(a)  # [23, 12, 28, 23]

# Метод .remove вызывает ValueError, когда значение x не найдено в списке L.

# Метод reverse
# Метод .reverse имеет следующий формат:
# L.reverse()
# Метод .reverse  не требует никаких аргументов и выполняет разворот
# списка - располагает элементы в противоположном порядке.
# При повторном вызове список вернётся в изначальное положение.

print('&&&')
a = [34, 23, 12, 28, 23]
a.reverse()
print(a)  # [23, 28, 12, 23, 34]
a.reverse()
print(a)  # [34, 23, 12, 28, 23]

# Метод sort
# Самый, наверное, популярный метод списков - это .sort.
# Он выполняет сортировку. Имеет следующий формат:
# L.sort(key=None, reverse=False)
# Если не передать никаких аргументов,
# то по умолчанию сортировка будет выполнена по возрастанию.
# После этого можете вызвать метод .reverse.
# Список отсортируется по убыванию.
# Если вы сразу хотите его отсортировать по убыванию,
# то вы можете вызвать метод .sort и в нём внутри скобок дополнительно прописать reverse=True.

print('###')
a = [34, 23, 12, 28, 23]
a.sort()
print(a)  # [12, 23, 23, 28, 34]
a.reverse()
print(a)  # [34, 28, 23, 23, 12]

b = [34, 23, 12, 28, 23]
b.sort(reverse=True)
print(b)  # [34, 28, 23, 23, 12]
