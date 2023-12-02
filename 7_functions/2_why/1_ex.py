# Напишите функцию repeat_please_n_times, которая принимает один аргумент n - натуральное число.
# Функция repeat_please_n_times должна n раз распечатать фразу "Just do it" в отдельной строчке
#
# Ваша задача написать только определение функции repeat_please_n_times, вызывать ее не нужно


# объявление функции
def repeat_please_n_times(n):
    print("Just do it\n"*n, end='')


repeat_please_n_times(1)
