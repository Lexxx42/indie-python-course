"""
Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше одного раза.

Входные данные
Входная строка может содержать цифры, пробелы и латинские буквы.

Выходные данные
Программа должна вывести в одну строчку в порядке возрастания все цифры, встречающиеся во входной строке больше одного раза. Если таких цифр нет, нужно вывести слово 'NO'.

Sample Input 1:

abc12cd34ef35
Sample Output 1:

3
Sample Input 2:

yrey424u3iou2315
Sample Output 2:

2 3 4
Sample Input 3:

qwerty123
Sample Output 3:

NO
Sample Input 4:

jfheuwoifuy89749204298462948hfdisf394823
Sample Output 4:

2 3 4 8 9
Sample Input 5:

84-05u340y5349054530593795tguiet783456395
Sample Output 5:

0 3 4 5 7 8 9
"""

s = input()
print(*sorted(set(i for i in s if i.isdigit() and s.count(i) > 1)) or ['NO'])
