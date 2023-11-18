# Методы frozenset
# frozenset является неизменяемым объектом, поэтому вызов метода множества не окажет влияние на состояние элементов неизменяемого множества,
# у которого вызывается метод. Если вы хотите изменить объект frozenset необходимо пользоваться присваиванием.
#
# Метод copy
# Метод .copy() выполняет поверхностное копирование элементов оригинального frozenset.
person = {"name": "Jack", "age": 21, "Country": "India"}

frozen_dict = frozenset(person)
print(f'{frozen_dict=}')

a = frozen_dict.copy()

print(f'{a=}')

# Метод difference
# Метод .difference() позволяет выполнить операцию «разность множеств».
# Результатом вызова метода .difference() будет новое неизменяемое множество куда войдут только элементы
# из операции разности множеств. Старые объекты никак не изменятся в процессе работы этого метода

frozen1 = frozenset([1, 2, 3, 4])

frozen2 = frozenset([3, 4, 5, 6])

frozen_diff = frozen1.difference(frozen2)

print(f'Разнцица между {frozen1} and {frozen2} = {frozen_diff}')

print(f'Разнцица между {frozen2} and {frozen1} = '
      f'{frozen2.difference(frozen1)}')

# Метод union
# Метод .union() позволяет выполнить операцию объединения.
# Результатом вызова метода .union() будет новое неизменяемое множество, или, другими словами, новый объект frozenset

frozen1 = frozenset([1, 2, 3, 4])

frozen2 = frozenset([3, 4, 5, 6])

frozen_union = frozen1.union(frozen2)

print(f'Объединение {frozen1} и {frozen2}={frozen_union}')

# Метод intersection
# Метод .intersection() позволяет выполнить операцию пересечения.
# Результатом вызова метода .intersection() будет новое неизменяемое множество,
# или, другими словами, новый объект frozenset

frozen1 = frozenset([1, 2, 3, 4])

frozen2 = frozenset([3, 4, 5, 6])

frozen_intersection = frozen1.intersection(frozen2)

print(f'Пересечение {frozen1} и {frozen2}={frozen_intersection}')

# Метод symmetric_difference
# Метод .symmetric_difference() позволяет выполнить операцию «симметрическая разность».
# Результатом вызова метода .symmetric_difference() будет новое неизменяемое множество
# куда войдут только элементы из операции разности множеств.
# Старые объекты никак не изменятся в процессе работы этого метода

frozen1 = frozenset([1, 2, 3, 4])

frozen2 = frozenset([3, 4, 5, 6])

frozen_symm_diff = frozen1.symmetric_difference(frozen2)

print(f'Симм. разница {frozen1} и {frozen2}={frozen_symm_diff}')
