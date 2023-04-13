# Удаляем слова-дубли
# На вход программе поступает строка, состоящая из нескольких слов,
# знаком разделителем между словами будем считать символ пробела.
# Ваша задача исключить из строки дублирующие слова:
# первое появление слова остается в строке, второе и все последующие появления исключаются.
# При сравнении на дубли строк регистр букв не учитывать,
# это значит слова python и PyThOn считаются одинаковыми.

# В качестве ответа необходимо вывести итоговую строку без дублей.

# Sample Input 1:

# Python is best I love python
# Sample Output 1:

# Python is best I love
# Sample Input 2:

# one one two two three four four five six six one two three four five six
# Sample Output 2:

# one two three four five six
# Sample Input 3:

# Two one One SIX two thrEE four four five SIX six one two three four five six ONE
# Sample Output 3:

# Two one SIX thrEE four five

# input_string = input()
#
# output_string = ''
# check_list = []
#
# for word in input_string.split():
#     if word.lower() not in check_list:
#         check_list.append(word.lower())
#         output_string += word + ' '
#
# print(output_string.strip())

s = set()
for i in input().split():
    if i.lower() not in s:
        s.add(i.lower())
        print(i, end=' ')
