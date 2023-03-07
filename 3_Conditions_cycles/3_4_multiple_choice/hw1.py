# FizzBuzz
# Классическая задача для начинающих.
#
# Ваша программа должна считать одно натуральное число, после чего вывести:
#
# “Fizz”, если это число делится на 3;
# “Buzz”, если это число делится на 5;
# “FizzBuzz”, если выполнены оба предыдущих условия;
# само это число в остальных случаях.
# Sample Input 1:
#
# 15
# Sample Output 1:
#
# FizzBuzz
# Sample Input 2:
#
# 10
# Sample Output 2:
#
# Buzz
# Sample Input 3:
#
# 12
# Sample Output 3:
#
# Fizz
# Sample Input 4:
#
# 13
# Sample Output 4:
#
# 13

# “Fizz”, если это число делится на 3;
# “Buzz”, если это число делится на 5;
# “FizzBuzz”, если выполнены оба предыдущих условия;
# само это число в остальных случаях.

if not (x := int(input())) % 3 and not x % 5:
    print('FizzBuzz')
elif not x % 3:
    print('Fizz')
elif not x % 5:
    print('Buzz')
else:
    print(x)
