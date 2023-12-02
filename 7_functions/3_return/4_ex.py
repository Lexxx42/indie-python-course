# Ваша задача написать функцию find_duplicate, которая принимает один аргумент - список чисел.
# Функция должна возвращать список из дублей,
# каждый дубль нужно брать только один раз в том порядке,
# в котором они встречаются в исходном списке.
# Под дублем будем подразумевать число, которое присутствовало в списке несколько раз.
#
# find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) => [1, 2]
# find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) => [2, 1]
# find_duplicate([1, 2, 3, 4]) => []
# find_duplicate([1, 2, 3, 4, 3]) => [3]

def find_duplicate(lst):
    dublicates = []
    for number in lst:
        if number not in dublicates and lst.count(number) > 1:
            dublicates.append(number)
    return dublicates


assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
assert find_duplicate([1, 2, 3, 4]) == []
assert find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]
print('Все успешно')
