# В данной задаче необходимо сравнить два целых числа A и B.
# Они поступают на вход программе отдельно в каждой строке.

# Ваша задача вывести символ <, если A меньше B, >, если A больше B и =, если A=B.

# Sample Input 1:

# 5
# 9
# Sample Output 1:

# <
# Sample Input 2:

# 2
# 1
# Sample Output 2:

# >
# Sample Input 3:

# 7
# 7
# Sample Output 3:

# =

print('<' if (a := int(input())) < (b := int(input())) else '>' if a > b else '=')
