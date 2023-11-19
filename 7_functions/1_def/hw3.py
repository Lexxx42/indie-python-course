# Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.
#
# Сложным паролем будет считаться комбинация символов, в которой :
#
# Есть хотя бы 3 цифры
# Есть хотя бы одна заглавная буква
# Есть хотя бы один символ из следующего набора "!@#$%*"
# Общая длина не менее 10 символов
# Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy"
#
# Вам необходимо написать только определение функции check_password
#
# Разбор Youtube Patreon Boosty
#
# Sample Input 1:
#
# qwerty
# Sample Output 1:
#
# Easy peasy
# Sample Input 2:
#
# Qwerty1357!
# Sample Output 2:
#
# Perfect password
# Sample Input 3:
#
# Qwerty1357)
# Sample Output 3:
#
# Easy peasy
# Sample Input 4:
#
# Qwerty17!
# Sample Output 4:
#
# Easy peasy

def check_password(a):
    print("Perfect password" if len(set("!@#$%*") & set(a)) > 0 and len(set("0123456789") & set(a)) > 0 and len(
        a) >= 10 and a.islower() == False else "Easy peasy")
