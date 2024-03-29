# Телефонная книга
# Петя очень популярный парень, у него много друзей и он хочет сохранить их контакты в телефонной книге. Известно, что у каждого друга может быть один или больше номеров телефонов. Напишите программу, которая поможет Пете находить все номера определённого друга.
#
# Формат ввода
# В первой строке задано одно целое число N (1 ≤ N ≤ 1000) — количество номеров телефонов, информацию о которых Петя  решил сохранить в телефонной книге. В следующих N строках заданы телефоны и имена их владельцев через пробел. Телефон — это несколько цифр, записанных подряд, имя же состоит только из русских букв. Записи не повторяются.
#
# В следующей строке записано целое число M (1 ≤ M ≤ 100) — количество запросов от Пети. В следующих M строках записаны сами запросы, по одному на строке. Каждый запрос — это имя какого-то друга, чьи телефоны Петя хочет сейчас найти, записанное в точности так, как в телефонной книге.
#
# Формат вывода
# Для каждого запроса от Пети выведите в отдельной строке все телефоны, принадлежащие человеку с этим именем. Телефоны одного человека выводите в одну строку через пробел в том порядке, в котором они были заданы во входных данных.
#
# Если в телефонной книге нет телефонов человека с таким именем, выведите в соответствующей строке «Неизвестный номер» (без кавычек).
#
# Sample Input 1:
#
# 3
# 444444 Женя
# 79129874521 Женя
# 79604845827 Оля
# 3
# Оля
# Олег
# Женя
# Sample Output 1:
#
# 79604845827
# Неизвестный номер
# 444444 79129874521
# Sample Input 2:
#
# 5
# 111111 Ж
# 1234 Женя
# 9797897 Оля
# 1234 Ж
# 543543 КОля
# 7
# ччч
# Олег
# КОля
# Оля
# КОля
# Ж
# Женя
# Sample Output 2:
#
# Неизвестный номер
# Неизвестный номер
# 543543
# 9797897
# 543543
# 111111 1234
# 1234

n = int(input())
tele_book: dict[str, list[str]] = {}

for _ in range(n):
    data = input().split()

    if tele_book.get(data[-1]):
        tele_book[data[-1]].append(data[0])

    else:
        tele_book[data[-1]] = [data[0]]

m = int(input())

for _ in range(m):
    who = input()
    phones = tele_book.get(who)

    if phones:
        print(' '.join(phones))
    else:
        print('Неизвестный номер')
