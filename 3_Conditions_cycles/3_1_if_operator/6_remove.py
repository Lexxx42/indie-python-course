# Метод remove
# Программа получает на вход список из целых чисел, при этом гарантируется,
# что числа в списке повторяться не будут.
# Ваша задача удалить из этого списка числа 3, 5, 7 и 9.

# Обратите внимание, что каждое из чисел 3, 5, 7 и 9
# необязательно должно присутствовать в введенном списке.

# В качестве ответа необходимо распечатать измененный список

# Примечание:

# Чтобы прочитать из ввода целые числа и сохранить их в виде списка в переменной a вам необходимо написать строчку

# a = list(map(int, input().split()))
# Sample Input 1:

# 1 2 3 4 5 6 7 8 9 10
# Sample Output 1:

# [1, 2, 4, 6, 8, 10]
# Sample Input 2:

# 4 3 65 32 43 5 2
# Sample Output 2:

# [4, 65, 32, 43, 2]
# Sample Input 3:

# 1 5 2
# Sample Output 3:

# [1, 2]

# print(input().translate({ord(i): None for i in '3579'}).split())

# print(list(map(int, input().translate({ord(i): None for i in '3579'}).split())))

# a = list(map(int, input().split()))
# [a.remove(item) if item in a else ... for item in [3, 5, 7, 9]]
# print(a)

print([int(i) for i in input().split() if i not in '3579'])
