# На вход программе поступают два целых числа в одной строке.
#
# Программа должна вывести True, если оба числа делятся на 7, в противном случае - False.
#
# Сделать задачу необходимо без использования условного оператора.
#
# Sample Input 1:
#
# 77 14
# Sample Output 1:
#
# True

# print((lambda x, y: x % 7 == y % 7)(*map(int, input().split())))

# print(all([not int(i) % 7 for i in a]))

#print(sum([int(i) % 7 for i in input().split()]) == 0)

# print(sum(map(lambda x: int(x) % 7, input().split())) == 0)

print(all(map(lambda x: int(x) % 7 == 0, input().split())))




