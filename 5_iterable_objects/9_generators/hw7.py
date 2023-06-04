# При помощи list comprehension создайте список, состоящий из первых n заглавных букв английского алфавита ['A', 'B', 'C', 'D', ...]. Получить все заглавные буквы английского алфавита можно следующим образом:
#
# from string import ascii_uppercase
# print(ascii_uppercase) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Входные данные
# На вход программе подается натуральное число n, n≤26.
#
# Формат выходных данных
# Программа должна вывести список из первых n заглавных букв английского алфавита
#
# Sample Input 1:
#
# 3
# Sample Output 1:
#
# ['A', 'B', 'C']
# Sample Input 2:
#
# 5
# Sample Output 2:
#
# ['A', 'B', 'C', 'D', 'E']
# Sample Input 3:
#
# 9
# Sample Output 3:
#
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

from string import ascii_uppercase


print([*ascii_uppercase[:int(input())]])
