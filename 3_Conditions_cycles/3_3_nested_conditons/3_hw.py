# Даны три целых числа, каждое записано в отдельной строке.

# Нужно вывести значение наибольшего из данных чисел

# Примечание: используйте только условный оператор, функцией max пользоваться нельзя

# Sample Input 1:

# 5
# 7
# 21
# Sample Output 1:

# 21
# Sample Input 2:

# 81
# 75
# -65
# Sample Output 2:

# 81
# Sample Input 3:

# -41
# 7
# -79
# Sample Output 3:

# 7
# Sample Input 4:

# -66
# -21
# -78
# Sample Output 4:

# -21

print(sorted([int(input()) for _ in range(3)])[-1])
