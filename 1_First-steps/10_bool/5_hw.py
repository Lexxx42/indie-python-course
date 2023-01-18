# На вход поступают три целых числа - стороны треугольника.
#
# Необходимо вывести True, если данные стороны образуют правильный треугольник, в противном случае - False.
#
# Сделать задачу необходимо без использования условного оператора.
#
# Sample Input 1:
#
# 5 5 5
# Sample Output 1:
#
# True
# Sample Input 2:
#
# 4 5 6
# Sample Output 2:
#
# False

print((lambda x, y, z: x==y==z)(*input().split()))

# print(len(set(input().split())) == 1)

