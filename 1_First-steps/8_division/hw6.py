# Дано целое положительное трехзначное число, ваша задача найти сумму разрядов этого числа

# Sample Input 1:

# 123
# Sample Output 1:

# 6
# Sample Input 2:

# 109
# Sample Output 2:

# 10

# print(sum([int(i) for i in input()]))
print(sum(map(int, input())))
