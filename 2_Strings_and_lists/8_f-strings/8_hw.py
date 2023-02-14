# Нашей программе поступает на вход x, y, z - три целых числа,
# обозначающие координаты вектора А.
# Затем необходимо найти координаты вектора B,
# путем увеличения на 5 каждой из координаты вектора А.

# Оба вектора необходимо распечатать в определенном формате

# Sample Input 1:

# 1
# 2
# 3
# Sample Output 1:

# Vector A(1, 2, 3)
# Vector B(6, 7, 8)
# Sample Input 2:

# -5
# 0
# 15
# Sample Output 2:

# Vector A(-5, 0, 15)
# Vector B(0, 5, 20)

# (lambda a: print(f'Vector A({a[0]}, {a[1]}, {a[2]})\nVector B({a[0] + 5}, {a[1] + 5}, {a[2] + 5})'))([int(input())
#                                                                                                       for _ in
#                                                                                                       range(3)])

print(f'Vector A{(coords := tuple(int(input()) for _ in range(3)))}\nVector B{tuple(i + 5 for i in coords)}')
