# Выиграть в лотерею

# У Олега в банке есть n евро.
# Он хочет снять всю сумму наличными.
# Номиналы еврокупюр равны 1, 5, 10, 20, 100.
# Какое минимальное число купюр должен получить Олег после того,
# как снимет все деньги?

# На вход программе поступает одно положительные целое число n.

# Разбор YouTube   Patreon  Boosty

# Sample Input 1:

# 125
# Sample Output 1:

# 3
# Sample Input 2:

# 43
# Sample Output 2:

# 5
# Sample Input 3:

# 10000000
# Sample Output 3:

# 100000

print((n := int(input())) // 100 + n % 100 // 20 + n % 20 // 10 + n % 10 // 5 + n % 5 // 1)