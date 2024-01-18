# Напишите функцию check_sum, которая принимает произвольное количество аргументов типа int.
#
# Данная функция должна выводить not enough, если сумма всех элементов меньше 50, в противном случае выводить verification passed
#
# Вам необходимо написать только определение функции check_sum
#
# Sample Input 1:
#
# 8 11
# Sample Output 1:
#
# not enough
# Sample Input 2:
#
# 10 10 10 10 9
# Sample Output 2:
#
# not enough
# Sample Input 3:
#
# 20 20 10
# Sample Output 3:
#
# verification passed

def check_sum(*args: int):
    print('not enough') if sum(args) < 50 else print('verification passed')
