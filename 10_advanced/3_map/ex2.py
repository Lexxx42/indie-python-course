# Перед вами имеется список numbers, состоящий из целых чисел. Ваша задача увеличить каждый элемент списка numbers втрое и сохранить полученный результат в новый список increase_3. Для преобразования используйте функцию map
#
# В качестве ответа выведите переменную increase_3
#
# Sample Input:
#
# Sample Output:
#
# [348, -1233, 1344, 1908, -762, -885, 660, 648, 561, -450, -1374, -1116, 1350, 423, -1878, -504, -1149, 1167, -552, 1827, 663, 933, 1578, 762, -1893, -522, -1665, -1014, 678, 2085, -48, 999, 36, -1800, -774, -1149, -303, 363, 120, 834, 354, -1386, -2013, 234, -207, -1704, -684, -1335, -141, -1695]


numbers = [116, -411, 448, 636, -254, -295, 220, 216, 187, -150, -458, -372, 450, 141, -626, -168, -383, 389, -184, 609,
           221, 311, 526, 254, -631, -174, -555, -338, 226, 695, -16, 333, 12, -600, -258, -383, -101, 121, 40, 278,
           118, -462, -671, 78, -69, -568, -228, -445, -47, -565]

print(increase_3 := [num * 3 for num in numbers])
