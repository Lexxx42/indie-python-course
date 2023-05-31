# На вход программе подается натуральное число n (n<=1000). При помощи list comprehension создайте список, состоящий из делителей введенного числа и выведите его на экран
#
# Sample Input 1:
#
# 4
# Sample Output 1:
#
# [1, 2, 4]
# Sample Input 2:
#
# 5
# Sample Output 2:
#
# [1, 5]
# Sample Input 3:
#
# 10
# Sample Output 3:
#
# [1, 2, 5, 10]

n = int(input())

print([i for i in range(1, n + 1) if not n % i])
