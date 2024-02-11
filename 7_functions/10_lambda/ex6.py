# Напишите lambda функцию, которая принимает произвольное количество числовых аргументов и выводит их среднее арифметическое.
# Для проверки решения присвойте вашу lambda функцию переменной average.
#
# Вводить и выводить ничего не нужно, только определить переменную average
#
# Sample Input 1:
#
# 4 5 6
# Sample Output 1:
#
# 5.0
# Sample Input 2:
#
# 2 6
# Sample Output 2:
#
# 4.0

from typing import Callable

average: Callable[[int, ...], float] = lambda *args: sum(args) / len(args)

