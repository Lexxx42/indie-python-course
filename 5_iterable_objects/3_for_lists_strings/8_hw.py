# Линейный поиск

# Линейный поиск, также известный как последовательный поиск,
# этот метод используется для поиска элемента в списке.
# Линейный поиск является одним из базовых алгоритмов,
# с которым вы должны познакомиться, изучая программирования.
# Суть алгоритма в следующем: вы должны проверять каждый элемент списка последовательно один за другим,
# пока не найдете интересующий вас элемент или пока не закончится весь список.

# Входные данные
# Программа получает на вход в одной строке элементы списка - целые числа,
# разделенные пробелом. Количество элементов произвольное

# И на следующей строке вводится одно число r - значение поиска

# Выходные данные
# Ваша задача реализовать линейный алгоритм поиска введенного значения r.
# В случае успеха - выведите порядковый номер(индекс) первого найденного элемента в списке при условии,
# что индексация начинается с единицы.
# Если данный элемент отсутствует - необходимо вывести строку ErrorValue

# Sample Input 1:

# 8 11 45 32 543 65
# 32
# Sample Output 1:

# 4
# Sample Input 2:

# 5 5 5 5
# 5
# Sample Output 2:

# 1
# Sample Input 3:

# 32 4 543 65 4 5 4 54 32 5 54 43 543 43
# 999
# Sample Output 3:

# ErrorValue

# input_list = input().split()
# print(input_list.index(element_to_find) + 1 if (element_to_find := input()) in input_list else 'ErrorValue')

input_list = input().split()
element_to_find = input()
for i, element in enumerate(input_list):
    if element == element_to_find:
        print(i + 1)
        break
else:
    print('ErrorValue')
