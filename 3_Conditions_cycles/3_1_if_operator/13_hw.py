# Счастливый билет
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером (иногда и с незначащими нулями), где сумма первых трех цифр равна сумме последних трех. Т.е. билеты с номерами 385916 и 2011 – счастливые, т.к. 3+8+5=9+1+6 и 0+0+2=0+1+1. Вам требуется написать программу, которая проверяет «счастливость» билета.
#
# Программа получает на вход одно целое число N (0 ≤ N < 106) и должна вывести «YES», если билет с номером N счастливый и «NO» в противном случае.
#
# 🚀Если не справляетесь, здесь подсказка🚀
# Sample Input 1:
#
# 385916
# Sample Output 1:
#
# YES
# Sample Input 2:
#
# 123344
# Sample Output 2:
#
# NO
# Sample Input 3:
#
# 5203
# Sample Output 3:
#
# YES

print('YES' if sum((a := list(map(int, [i for i in input().rjust(6, '0')])))[:3]) == sum(a[3:]) else 'NO')
