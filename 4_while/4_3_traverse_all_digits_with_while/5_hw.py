# Программа принимает на вход одно натуральное число
# и выводит на экран минимальную и максимальную цифры данного числа в отдельных строчках

# Sample Input 1:

# 480
# Sample Output 1:

# 0
# 8
# Sample Input 2:

# 123
# Sample Output 2:

# 1
# 3
# Sample Input 3:

# 99
# Sample Output 3:

# 9
# 9

# print(min(numbers := [*input()]), max(numbers), sep='\n')

print(min(n := input()), max(n), sep="\n")

# s = sorted(input())
# print(s[0], s[-1], sep = '\n')

# n = input()
# print(min(*n), max(*n), sep = '\n')
