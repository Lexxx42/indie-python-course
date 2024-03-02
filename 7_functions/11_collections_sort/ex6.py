# Премия Оскар
# Представьте, что мы с вами сами можем решать кому и сколько статуэток Оскара уйдет (Лео бы тогда давно купался в этих статуэтках)
#
# Ваша задача написать программу, которая находит информацию, кто из актеров получил наибольшее и наименьшее количество статуэток
#
# Входные данные
# Программа принимает на вход в первой строке натуральное число n - количество вручаемых сегодня наград. И затем в n следующих строках вводятся имена актеров - победителей.
#
# Выходные данные
# Нужно вывести в  отдельных строках имена актеров набравших наибольшее и наименьшее количество статуэток и через запятую их количество. Гарантируется, что всегда будет только один человек, набравший наибольшее и наименьшее количество статуэток.
#
# Sample Input:
#
# 6
# Леонардо Ди Каприо
# Джонни Депп
# Леонардо Ди Каприо
# Леонардо Ди Каприо
# Джонни Депп
# Мэтт Деймон
# Sample Output:
#
# Леонардо Ди Каприо, 3
# Мэтт Деймон, 1

n = int(input())

winners: dict[str, int] = {}

for _ in range(n):
    s = input()
    winners[s] = 1 if winners.get(s) is None else winners.get(s) + 1

win = sorted(winners.items(), key=lambda item: item[-1])
cool_print = lambda tuple_item: print(f'{tuple_item[0]}, {tuple_item[-1]}')

cool_print(win[-1])
cool_print(win[0])
