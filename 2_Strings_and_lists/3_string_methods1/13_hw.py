# На вход программе поступает строка, ваша задача удалить из нее все символы w и z.

# Учитываем только маленькие буквы

# Sample Input:

# what's up?
# Sample Output:

# hat's up?

# print(*[ch for ch in input() if ch not in 'wz'], sep='')
# print(''.join(ch for ch in input() if ch not in 'wz'))
print(input().replace('w', '').replace('z', ''))
