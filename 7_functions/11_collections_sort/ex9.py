# Дни рождения
# У Игоря N одноклассников. Игорь не смог запомнить их дни рождения и решил составить календарь дней рождений класса. По известному списку всех дней рождения научитесь определять, у кого день рождения в заданном месяце.
#
# Формат ввода
#
# В первой строчке записано целое число N (1 ≤ N ≤ 1000) — количество одноклассников Игоря. В следующих N строчках записана информация об их днях рождения. Каждая строчка состоит из трёх частей, разделённых пробелом — имени одноклассника, дня и месяца его рождения. Имя — это строка из русских букв, день — число от 1 до 31, а месяц — строка из набора «янв», «фев», «мар», «апр», «май», «июн», «июл», «авг», «сен», «окт», «ноя», «дек».
#
# Имена всех одноклассников Игоря различны.
#
# В следующей строчке записано целое число M (1 ≤ M ≤ 100) — количество вопросов, на которое надо ответить. В следующих M строках содержатся сами вопросы. Вопрос — это название месяца в том же формате, в котором они задаются выше.
#
# Формат вывода
# Для каждого вопроса в отдельной строчке через пробел выведите имена всех одноклассников, которые родились в указанном месяце. Имена упорядочьте в лексикографическом порядке.
#
# Если в заданном месяце никто не родился, выведите сообщение "Нет данных".
#
# Sample Input:
#
# 4
# Саша 20 янв
# Артем 15 июн
# Карл 10 янв
# Коля 20 июл
# 3
# июн
# дек
# янв
# Sample Output:
#
# Артем
# Нет данных
# Карл Саша


n = int(input())
birthdays: dict[str, list[str]] = {}

for _ in range(n):
    data = input().split()

    if birthdays.get(data[-1]):
        birthdays[data[-1]].append(data[0])

    else:
        birthdays[data[-1]] = [data[0]]

m = int(input())

for _ in range(m):
    month = input()
    friends = birthdays.get(month)

    if friends:
        friends.sort()
        print(' '.join(friends))
    else:
        print('Нет данных')
