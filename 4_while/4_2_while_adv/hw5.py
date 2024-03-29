# Ваня и кубики

# Ване на день рождения подарили n кубиков.
# Он с друзьями решил построить из них пирамиду.
# Ваня хочет построить пирамиду следующим образом:
# на верхушке пирамиды должен находиться 1 кубик,
# на втором уровне — 1+2=3 кубика, на третьем — 1+2+3=6 кубиков, и так далее.

# Таким образом, на i-м уровне пирамиды должно располагаться 1+2+...+(i-1)+i кубиков.

# Ваня хочет узнать, пирамиду какой максимальной высоты
# он может создать с использованием имеющихся кубиков.

# Входные данные
# В первой строке записано целое число n (1≤n≤104) — количество кубиков,
# подаренных Ване.

# Выходные данные
# Выведите единственной строкой максимально возможную высоту пирамиды.

# Решение youtube patreon boosty

# Sample Input 1:

# 1
# Sample Output 1:

# 1
# Sample Input 2:

# 25
# Sample Output 2:

# 4
# Sample Input 3:

# 4
# Sample Output 3:

# 2
# Sample Input 4:

# 5
# Sample Output 4:

# 2
# Sample Input 5:

# 6560
# Sample Output 5:

# 33
# Sample Input 6:

# 3
# Sample Output 6:

# 1

# кол-во кубиков которое нужно отнимать = кол-во кубиков * (кол_во кубиков + 1) // 2

# кол-во кубиков 1->2->3->4

n_cubes, i, n_next_row = int(input()), 1, 0
while n_cubes >= (n_next_row := i + n_next_row):
    n_cubes -= n_next_row
    i += 1
print(i - 1)

# n, h, row = int(input()), 1, 1
# while n >= row:
#     n, row, h = n - row, row + h + 1, h + 1
# print(h - 1)
