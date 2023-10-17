# Рассмотрим ещё пару методов множеств

# Помните специфичные для множеств операции, такие например как пересечение, объединение и т.д.
# Вот для них тоже существуют методы.

# Метод union

# Метод .union() позволяет выполнить операцию объединения.
# Метод .union() может принимать произвольное количество любых объектов,
# поддерживающих итерацию по своим элементам.
# Это могут быть списки, кортежи, другое множество и т.д.
# Дублирующие элементы последовательностей игнорируются.
# Результатом вызова метода .union() будет новое множество, или, другими словами,
# новый объект множества.
# Метод не изменяет значения того множества, у которого метод вызывался

set_str = {'car', 'soup', 'bus'}
set_num = {1, 2, 3}
my_list = [True, 101, 'hello', 'soup', 2]
new_set = set_str.union(set_num)
print(set_str)
print(new_set)
print('-' * 15)
new_set_2 = set_num.union(my_list)
print(set_num)
print(new_set_2)
print('-' * 15)
print(set_num.union('abcd', (2, 3, 4, 5)))
print('-' * 15)
print(set_str.union(set_num, range(5)))

# Метод intersection

# Метод .intersection() позволяет выполнить операцию пересечения.
# Метод .intersection() может принимать произвольное количество любых объектов,
# поддерживающих итерацию по своим элементам.
# Результатом вызова метода .intersection() будет новое множество куда войдут только те элементы,
# которые встречаются во всех коллекциях.
# Старые объекты никак не изменятся в процессе работы этого метода

set_a = {'car', 'soup', 'bus'}
set_b = {'bus', 'soup'}
set_num = {1, 2, 3}
new_set = set_a.intersection(set_b)
print(set_a)
print(new_set)
print('-' * 15)
new_set_2 = set_a.intersection(('hello', 'car'), ['car', 'soup'])
print(set_a)
print(new_set_2)
print('-' * 15)
print(set_num.intersection(range(3), (2, 3, 4, 5)))

# Метод intersection_update

# Метод .intersection_update() позволяет выполнить операцию пересечения.
# Метод .intersection_update() может принимать произвольное количество любых объектов,
# поддерживающих итерацию по своим элементам.
# Результатом вызова метода .intersection_update() будет не создание нового множества,
# а изменение существующего.
# Присваивать ничего не нужно, автоматически после вызова изменится множество,
# у которого данный метод был вызван.
# При попытке сохранить результат вызова этого метода  в переменную, в ней сохранится значение None

set_a = {'car', 'soup', 'bus'}
set_b = {'bus', 'soup'}

set_a.intersection_update(set_b)
print(set_a)
print(set_b)
print('-' * 15)

set_num_1 = {1, 2, 3, 4}
set_num_2 = {2, 3, 4, 5, 6}
set_num_3 = {3, 4, 6}
res = set_num_2.intersection_update(set_num_1, set_num_3)
print(set_num_1)
print(set_num_2)
print(set_num_3)
print(res)

# Метод difference

# Метод .difference() позволяет выполнить операцию «разность множеств».
# Метод .difference() может принимать произвольное количество любых объектов,
# поддерживающих итерацию по своим элементам.
# Результатом вызова метода .difference() будет новое множество куда войдут только элементы
# из операции разности множеств.
# Старые объекты никак не изменятся в процессе работы этого метода

set_a = {'car', 'soup', 'bus'}
set_b = {'bus', 'soup'}

res_1 = set_a.difference(set_b)
res_2 = set_b.difference(set_a)
print(set_a)
print(set_b)
print(res_1, res_2)
print('-' * 15)

set_num_1 = {1, 2, 3, 4}
set_num_2 = {2, 3, 4, 5, 6}
set_num_3 = {3, 4, 6}
print(set_num_1.difference(set_num_2))
print(set_num_3.difference(set_num_1))
print(set_num_2.difference(set_num_1))
print(set_num_2.difference(set_num_1, set_num_3))
print(set_num_2)

# Метод difference_update

# Метод .difference_update() позволяет выполнить операцию «разность множеств».
# Метод .difference_update() может принимать произвольное количество любых объектов,
# поддерживающих итерацию по своим элементам.
# Результатом вызова метода .difference_update() будет не создание нового множества,
# а изменение существующего.
# Присваивать ничего не нужно, автоматически после вызова изменится множество,
# у которого данный метод был вызван.
# При попытке сохранить результат вызова этого метода  в переменную, в ней сохранится значение None

set_a = {'car', 'soup', 'bus'}
set_b = {'bus', 'soup', 'bro', 'lol'}

set_a.difference_update(set_b)
print(set_a)
set_b.difference_update(set_a)
print(set_b)
print('-' * 15)

set_num_1 = {1, 2, 3, 4}
set_num_2 = {2, 3, 4, 5, 6}
set_num_3 = {3, 4, 6}

res = set_num_2.difference_update(set_num_1, set_num_3)
print(set_num_2)
print(res)
print('-' * 15)

set_num_1.difference_update(set_num_3)

# Метод symmetric_difference

# Метод .symmetric_difference() позволяет выполнить операцию «симметрическая разность».
# Метод .symmetric_difference() может принимать только один объект,
# поддерживающих итерацию по своим элементам.
# Результатом вызова метода .symmetric_difference() будет новое множество,
# куда войдут только элементы из операции разности множеств.
# Старые объекты никак не изменятся в процессе работы этого метода

set_a = {'car', 'soup', 'bus'}
set_b = {'bus', 'soup'}

res = set_a.symmetric_difference(set_b)
print(set_a)
print(set_b)
print(res)
print('-' * 15)

set_num_1 = {1, 2, 3, 4}
set_num_2 = {2, 3, 4, 5, 6}
set_num_3 = {3, 4, 6}
print(set_num_1.symmetric_difference(set_num_2))
print(set_num_3.symmetric_difference(set_num_1))
print(set_num_2.symmetric_difference(set_num_3))

# Метод symmetric_difference_update

# Метод .symmetric_difference_update() позволяет выполнить операцию «симметрическая разность».
# Метод .symmetric_difference_update() может принимать только один любой объект,
# поддерживающий итерацию по своим элементам.
# Результатом вызова метода .symmetric_difference_update() будет не создание нового множества,
# а изменение существующего.
# Присваивать ничего не нужно, автоматически после вызова изменится множество,
# у которого данный метод был вызван.
# При попытке сохранить результат вызова этого метода в переменную, в ней сохранится значение None

set_a = {'car', 'soup', 'bus'}
set_b = {'bus', 'soup', 'bro', 'lol'}

set_a.symmetric_difference_update(set_b)
print(set_a)
set_b.symmetric_difference_update(set_a)
print(set_b)
print('-' * 15)

set_num_1 = {1, 2, 3, 4}
set_num_2 = {2, 3, 4, 5, 6}
set_num_3 = {3, 4, 6}

res = set_num_2.symmetric_difference_update(set_num_1)
print(set_num_2)
print(res)
print('-' * 15)
