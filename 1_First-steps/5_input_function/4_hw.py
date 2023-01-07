# Вашей программе поступает на вход натуральное число.
# Ваша задача вывести в отдельных строках:

# число, увеличенное в 2 раза;
# число, уменьшенное в 2 раза

natural_number = int(input())
print(natural_number * 2, natural_number / 2, sep='\n')
print(f'{natural_number * 2}\n{natural_number / 2}')
