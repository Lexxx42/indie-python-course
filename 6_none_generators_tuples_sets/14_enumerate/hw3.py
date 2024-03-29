# А вы знали, что цифры на банковской карте выбираются не просто случайным образом?
#
#
#
# Сумма определенных цифр на карте должны проходить условия алгоритма Луна

# https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9B%D1%83%D0%BD%D0%B0

#
# Алгоритм Луна
# Упрощенная версия алгоритма выглядит так:
#
# Цифры проверяемой последовательности нумеруются справа налево.
# Цифры, оказавшиеся на нечётных местах, остаются без изменений.
# Цифры, стоящие на чётных местах, умножаются на 2.
# Если в результате такого умножения возникает число больше 9, оно уменьшается на значение 9
# Все полученные в результате преобразования 16 цифр складываются. Если сумма кратна 10, то исходные данные верны.
#
# Ваша задача проверить является ли введенный номер карты валидным в соответствии с алгоритмом Луны
#
# Входные данные
#
# Входные данные
# На вход программе поступает 16 цифр без пробелов и знаков разделителя
#
# Выходные данные
# Если номер карты валидный, выведите True, в противном случае - False
#
# Sample Input 1:
#
# 3942682966937054
# Sample Output 1:
#
# True
# Sample Input 2:
#
# 2553514623369426
# Sample Output 2:
#
# False
# Sample Input 3:
#
# 1217040151414995
# Sample Output 3:
#
# True
# Sample Input 4:
#
# 2146133934667114
# Sample Output 4:
#
# True
# Sample Input 5:
#
# 4111111111111111
# Sample Output 5:
#
# True
card = list(map(int, input()))

for i in range(0, len(card), 2):
    if (res := card[i] * 2) > 9:
        card[i] = res - 9
    else:
        card[i] = res

print(not sum(card) % 10)
