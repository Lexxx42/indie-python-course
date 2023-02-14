# Ваша задача обязательно сохранить поступающие на вход значения в переменные x и y соответственно,
# и затем вывести строку вида Точка(x = {значение}, y = {значение})

# Sample Input 1:

# 5
# 9
# Sample Output 1:

# Точка(x = 5, y = 9)
# Sample Input 2:

# -3
# 100
# Sample Output 2:

# Точка(x = -3, y = 100)
# Sample Input 3:

# 87
# -9
# Sample Output 3:

# Точка(x = 87, y = -9)

#print(f'Точка(x = {(x := input())}, y = {(y := input())})')

print((lambda x, y: (f'Точка({x = },{ y = })'))(x := int(input()), int(input())))
