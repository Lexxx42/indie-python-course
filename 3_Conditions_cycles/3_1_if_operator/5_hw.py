# Программа получает на вход три натуральных числа A, B и C через пробел.

# Вам необходимо вывести YES в том случае, если A + B = C и вывести NO в противном случае.

# Sample Input 1:

# 4 5 9
# Sample Output 1:

# YES
# Sample Input 2:

# 1 2 4
# Sample Output 2:

# NO

#print('YES' if (lambda x: sum(x[:2]) == x[-1])(list(map(int, input().split()))) else 'NO')

a, b, c = [int(i) for i in input().split()]
print(['NO', 'YES'][a+b==c])
