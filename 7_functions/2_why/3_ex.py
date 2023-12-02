# Считаем буквы
# Напишите функцию count_letter(text, letter), которая принимает два параметра:
#
# text – текст, в котором нужно посчитать сколько раз появилась буква letter, учитывая регистр буквы;
# letter – буква, количество которой мы должны посчитать в text.
# Функция count_letter должна выводить на экран найденное количество букв  letter в тексте text
#
# Ваша задача дописать только тело функции count_letter
#
# Sample Input 1:
#
# to be or not to be
# b
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# did you pray desdemona
# d
# Sample Output 2:
#
# 4
# Sample Input 3:
#
# did you pray desdemona
# D
# Sample Output 3:
#
# 0


# объявление функции
def count_letter(text, letter):
    print(text.count(letter))

# считываем данные
text = 'hello wOrld'
symbol = 'o'
# вызываем функцию
count_letter(text, symbol)