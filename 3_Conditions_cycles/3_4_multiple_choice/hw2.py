# Даны три целых числа, записанных в отдельных строках. Определите, сколько среди них совпадающих.
#
# Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадают) или 0 (если все числа различны).
#
# Разбор решения Youtube Patreon Boosty
#
# Sample Input 1:
#
# 6
# 6
# 6
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# 7
# 8
# 7
# Sample Output 2:
#
# 2

numbers = {}

for _ in range(3):
    if (x := int(input())) in numbers:
        numbers[x] = numbers.get(x) + 1
    else:
        numbers[x] = 1

print(0 if sorted(numbers.items(), key=lambda item: item[1])[-1][1] == 1 else
      sorted(numbers.items(), key=lambda item: item[1])[-1][1])
