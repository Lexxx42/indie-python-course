"""
Ваша программа получает на вход последовательность фраз, указанных через запятую.
Для каждой фразы выведите слово ДА (в отдельной строке), если эта фраза ранее встречалось в последовательности или НЕТ, если не встречалось.
Символы во фразах нужно рассматривать без учета регистра, это значит что фраза Hasta la vista BAby эквивалента фразе hasta La Vista baby

Sample Input 1:

Hello world,hi dude,hello world,qwerty
Sample Output 1:

НЕТ
НЕТ
ДА
НЕТ
Sample Input 2:

django,Django,djanGO,djAngo,django
Sample Output 2:

НЕТ
ДА
ДА
ДА
ДА
Sample Input 3:

californication,can’t stop,dani california,by the way,around the world,dani,Californication,give it away,can’t stop
Sample Output 3:

НЕТ
НЕТ
НЕТ
НЕТ
НЕТ
НЕТ
ДА
НЕТ
ДА
"""

set_count = set()
for phrase in input().split(','):
    if phrase.lower() in set_count:
        print('ДА')
    else:
        print('НЕТ')
    set_count.add(phrase.lower())
