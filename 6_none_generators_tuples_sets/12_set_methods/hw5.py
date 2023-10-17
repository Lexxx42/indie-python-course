"""
Даны два списка чисел.

Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.

Sample Input:

1 3 2 5
4 3 2 6
Sample Output:

2 3
"""

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

for number in sorted(set_a.intersection(set_b)):
    print(number, end=' ')
