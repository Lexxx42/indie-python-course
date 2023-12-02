# Напишите функцию is_between, которая принимает три аргумента и печатает True,
# если первое число находится между двумя вторыми включительно, и False в противном случае.
#
# Ваша задача дописать только тело функции is_between
#
# Sample Input 1:
#
# 5 3 6
# Sample Output 1:
#
# True
# Sample Input 2:
#
# 10 2 5
# Sample Output 2:
#
# False
# Sample Input 3:
#
# 9 9 9
# Sample Output 3:
#
# True
# Sample Input 4:
#
# 5 9 1
# Sample Output 4:
#
# True

def is_between(name, surname, middlename):
    print(any((surname <= name <= middlename, middlename <= name <= surname)))

is_between(1, 4, 1)
