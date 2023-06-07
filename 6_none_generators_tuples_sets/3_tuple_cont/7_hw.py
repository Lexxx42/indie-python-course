# Перед вами кортеж words_tuple
#
# При помощи цикла for обойдите слова, хранящиеся в кортеже words_tuple, и для каждого элемента выведите строку вида
#
# Длина слова {word} = {len_word}
# Например, для кортежа words_tuple=('hi', 'world') ответ был бы таким:
#
# Длина слова hi = 2
# Длина слова world = 5

words_tuple = ('quaint', 'leftovers', 'thesis', 'density', 'retired', 'weak', 'tolerate',
               'sensitivity', 'primary', 'definition', 'determine', 'bring', 'monstrous',
               'hurl', 'timetable', 'month', 'advocate', 'provoke', 'stress', 'omission')

for word in words_tuple:
    print(f'Длина слова {word} = {len(word)}')
