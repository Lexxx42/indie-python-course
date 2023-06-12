# Анаграмма
# Cтрока S1 называется анаграммой строки S2, если она получается из S2 перестановкой символов.
#
# Программа получает на вход две строки S1 и S2. Если строка S1 является анаграммой строки S2 нужно вывести YES, в противном случае - NO
#
# Sample Input 1:
#
# abc
# cba
# Sample Output 1:
#
# YES

s1 = input()
s2 = input()

letters_s1 = {}
letters_s2 = {}

for letter in s1:
    letters_s1[letter] = letters_s1.get(letter, 0) + 1

for letter in s2:
    letters_s2[letter] = letters_s2.get(letter, 0) + 1

if letters_s1 == letters_s2:
    print('YES')
else:
    print('NO')
