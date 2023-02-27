# Вводятся два целых числа, каждое в отдельной строке.

# Ваша задача вывести наибольшее из данных чисел.

# Примечание: используйте только условный оператор, функцией max пользоваться нельзя

# Sample Input 1:

# 8
# 11
# Sample Output 1:

# 11
# Sample Input 2:

# 50
# 21
# Sample Output 2:

# 50

# print(max([int(input()) for _ in range(2)]))

print(lst[0] if (lst := [int(input()) for _ in range(2)])[0] >= lst[1] else lst[1])

# print(sorted([int(input()) for _ in range(2)])[-1])
