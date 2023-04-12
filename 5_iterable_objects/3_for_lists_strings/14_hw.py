# Правильная скобочная последовательность 2

# Наша программа принимает на вход последовательность скобочных символов.
# Ваша задача определить является ли введенная скобочная последовательность правильной.

# Правильная скобочная последовательность (ПСП) называется строка,
# состоящая только из символов "скобки",
# где каждой закрывающей скобке найдётся соответствующая открывающая (причём того же типа).
# При этом учитывайте, что:

# Пустая последовательность является правильной.
# Если A – правильная скобочная последовательность,
# то (A), [A] и {A} – правильные скобочные последовательности.
# Если A и B – правильные скобочные последовательности,
# то AB – правильная скобочная последовательность.
# Если введенная строка является ПСП, выведите YES, в противном случае - NO.

# Sample Input 1:

# []
# Sample Output 1:

# YES
# Sample Input 2:

# [(])
# Sample Output 2:

# NO
# Sample Input 3:

# {[]}()
# Sample Output 3:

# YES

# {()}

# input_string = input()
#
# for _ in range(len(input_string) // 2):
#     open_br_index = input_string.find('(')
#     if ')' in input_string[open_br_index:] and input_string.rfind(')') > open_br_index and (input_string.rfind(
#             ')') - input_string.find('(')) % 2:
#         input_string = input_string.replace('(', '', 1)
#         input_string = input_string.replace(')', '', 1)
#     open_br_index = input_string.find('[')
#     if ']' in input_string[open_br_index:] and input_string.rfind(']') > open_br_index and (input_string.rfind(
#             ']') - input_string.find('[')) % 2:
#         input_string = input_string.replace('[', '', 1)
#         input_string = input_string.replace(']', '', 1)
#     open_br_index = input_string.find('{')
#     if '}' in input_string[open_br_index:] and input_string.rfind('}') > open_br_index and (input_string.rfind(
#             '}') - input_string.find('{')) % 2:
#         input_string = input_string.replace('{', '', 1)
#         input_string = input_string.replace('}', '', 1)
# print('YES' if not len(input_string) else 'NO')

# s = input()
# while ('()' in s) | ('{}' in s) | ('[]' in s):
#     s = s.replace('()', '')
#     s = s.replace('{}', '')
#     s = s.replace('[]', '')
# print('NO' if s else 'YES')

n = input()
while '()' in n or '{}' in n or '[]' in n:
    n = n.replace('()', '').replace('{}', '').replace('[]', '')
print("YES" if len(n) == 0 else "NO")
