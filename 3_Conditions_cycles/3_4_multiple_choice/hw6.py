# Напишите программу, которая имитирует проверку пароля, придуманного пользователем.
# Пользователь сперва вводит пароль, потом вводит подтверждение пароля.
# Вам нужно обработать следующие ситуации:
#
# если пароль, который ввёл пользователь (в первый раз) короче 7 символов, программа выводит Short
# если пароль достаточно длинный,
# но введённый во второй раз пароль не совпадает с первым, программа выводит Difference
# если же и эта проверка пройдена успешно, программа выводит латинскими буквами OK
# Sample Input 1:
#
# qwerty
# qwerty
# Sample Output 1:
#
# Short
# Sample Input 2:
#
# qwerty123
# qwerty
# Sample Output 2:
#
# Difference
# Sample Input 3:
#
# qwertyuio
# qwertyuio
# Sample Output 3:
#
# OK
# Sample Input 4:
#
# qwertyuio123
# qwertyuio
# Sample Output 4:
#
# Difference

paswd1 = input()
paswd2 = input()

if len(paswd1) < 7:
    print('Short')
elif len(paswd1) >= 7 and paswd1 not in paswd2:
    print('Difference')
else:
    print('OK')
