# Программа принимает на вход одно натуральное число
# и выводит на экран произведение цифр данного числа

# Sample Input 1:

# 415
# Sample Output 1:

# 20
# Sample Input 2:

# 102
# Sample Output 2:

# 0

# import numpy
# print(numpy.prod(list(map(int, input()))))

# import math
# print(math.prod(list(map(int, input()))))

from functools import reduce

print(reduce((lambda x, y: x * y), list(map(int, input()))))
