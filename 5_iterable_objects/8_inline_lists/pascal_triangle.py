# вводим глубину треугольника паскаля
n = int(input())
# строки треугольника паскаля
a = [[1] + [0] * n for _ in range(n + 1)]

for i in range(0, n + 1):
    for j in range(0, i + 1):
        a[i][j] = a[i - 1][j] + a[i - 1][j - 1]
        print(a[i][j], end=' ')
    print()
