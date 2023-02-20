# Выравнивание
# Существует несколько способов выравнивания переменных в f-строках.
# Различные варианты выравнивания следует:

# Символ	Значение
# <	Выравнивает выражение в фигурных скобках по левому краю. У строк такое поведение по умолчанию
# >	Выравнивает выражение в фигурных скобках по правому краю. У чисел такое поведение по умолчанию
# ^	Выравнивает выражение в фигурных скобках по центру
# Ниже приведен пример использования выравнивания как для чисел, так и для строк.

number = 12345.6789
print(f"Число {number = }")
print(f"|{number:25}|")
print(f"|{number:<25}|")
print(f"|{number:>25}|")
print(f"|{number:^25}|")
print('-' * 25)
text = "Python 3.10"
print(f"Строка {text = }")
print(f"|{text:25}|")
print(f"|{text:<25}|")
print(f"|{text:>25}|")
print(f"|{text:^25}|")

print('-----')

# Символы "|" используются в f-строке, чтобы помочь очертить интервал.
# Число после «:» указывает на количество символов в ширину.

# По умолчанию символом заполнителем является пробел, но можно его заменить на другое значение

number = 12345.6789
print(f"Число {number = }")
print(f"|{number:=<25}|")
print(f"|{number:=>25}|")
print(f"|{number:=^25}|")
print('-' * 25)
text = "Python 3.10"
print(f"Строка {text = }")
print(f"|{text:-<25}|")
print(f"|{text:!>25}|")
print(f"|{text:?^25}|")

print('-----')

# Практический пример выравнивания
# Давайте с вами смоделируем чек покупки. Пример ниже

APPLES = .50
BREAD = 1.50
CHEESE = 2.111
num_apples = 3
num_bread = 10
num_cheese = 6
price_apples = num_apples * APPLES
price_bread = num_bread * BREAD
price_cheese = num_cheese * CHEESE
str_apples = 'Яблоки'
str_bread = 'Хлеб'
str_cheese = 'Сыр'
total = price_bread + price_cheese + price_apples
print(f'{"Список покупок":^30s}')
print(f'{"=" * 30}')
print(f'{str_apples:10s}{num_apples:10d}\t${price_apples:>5.2f}')
print(f'{str_bread:10s}{num_bread:10d}\t${price_bread:>5.2f}')
print(f'{str_cheese:10s}{num_cheese:10d}\t${price_cheese:>5.2f}')
print(f'{"Total:":>20s}\t${total:>5.2f}')
# Это значит выровнять по правому краю на ширину 5 символов и отформатировать до сотых.
