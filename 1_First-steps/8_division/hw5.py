# Дано целое положительное число, ваша задача вывести разряд сотен этого числа

# Sample Input 1:

# 123
# Sample Output 1:

# 1
# Sample Input 2:

# 56789
# Sample Output 2:

# 7
# Sample Input 3:

# 54
# Sample Output 3:

# 0

print(a[-3] if len(a := input()) >= 3 else "0")
