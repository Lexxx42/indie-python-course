# Напишите программу, которая отфильтрует список numbers так, чтобы в нем остались только четные значения. Используйте при этом lambda функцию.
#
# Распечатайте получившийся список
#
# Sample Input:
#
#
# Sample Output:
#
# [2, 4, 6, 8, 10]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(lambda x: not x % 2, numbers)))
