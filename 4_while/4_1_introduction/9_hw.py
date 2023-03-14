# Вася и носки

# У Васи есть n пар носков.
# Утром каждого дня, собираясь в школу, Вася должен надеть пару носков.
# Вечером, прийдя со школы, Вася снимает надетые носки и выбрасывает их.
# Каждый m-й день (в дни с номерами m,2m,3m,...) мама покупает Васе одну пару носков.
# Она делает это поздно вечером, поэтому Вася может надеть новые носки не раньше следующего дня.
# На сколько подряд идущих дней Васе хватит носков?

# Входные данные
# В единственной строке записано два целых числа n и m (1≤n≤100; 2≤m≤100), разделенные пробелом.

# Выходные данные
# Выведите единственное целое число — ответ на задачу.

# Разбор задачи Patreon  Boosty

# Примечание
# В первом примере первые два дня Вася будет носить носки,
# которые у него были изначально, затем на третий день будет носить носки,
# которые были куплены во второй день.

# Во втором примере первые девять дней он будет носить носки,
# которые у него были изначально,
# затем три дня будет носить носки, которые были куплены в третий,
# шестой и девятый дни.
# Затем еще день будет носить носки, которые были куплены в двенадцатый день.

# Sample Input 1:

# 2 2
# Sample Output 1:

# 3
# Sample Input 2:

# 9 3
# Sample Output 2:

# 13

n, m = map(int, input().split())
day = 0
while n >= 1:
    n -= 1
    if not (day + 1) % m:
        n += 1
    day += 1
print(day)