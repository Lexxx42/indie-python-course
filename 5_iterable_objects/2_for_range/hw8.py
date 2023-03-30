# Кратные 3 или 5

# Если перечислить все натуральные числа ниже 10,
# которые кратны 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел 23.

# Напишите программу, которая принимает натуральное число n
# и находит сумму всех чисел ниже переданного числа n,
# которые делятся на 3 или на 5.

# Sample Input 1:
#
# 10
# Sample Output 1:
#
# 23
# Sample Input 2:
#
# 9
# Sample Output 2:
#
# 14

s = 0
for x in range(int(input())):
    if not x % 3 or not x % 5:
        s += x
print(s)

# print(sum(i for i in range(int(input())) if not i % 3 or not i % 5))
