# Программа принимает на вход два слова s и t.

# Если слово t является словом s, записанным наоборот, выведите YES, иначе выведите NO.

# Слова состоят из маленьких латинских букв.
# Входные данные не содержат лишних пробелов. Слова непустые, и их длины не превосходят 100 символов.

# 🚀Если не справляетесь, здесь подсказка🚀
# Sample Input 1:

# avtor
# rotva
# Sample Output 1:

# YES
# Sample Input 2:

# aba
# abb
# Sample Output 2:

# NO

# print('YES' if  (a:=[input() for _ in range(2)])[0][::-1] == a[-1] else 'NO')
# print(('YNEOS')[((s := input())[::-1] != (t := input()))::2])
print(('NO', 'YES')[(a := input()) == a[::-1]])