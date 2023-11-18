# Перед вами имеется список words

# Ваша задача на основании создать список кортежей words_with_position,
# каждый элемент-кортеж должен содержать два значения: само слово и его порядковый номер в списке words

# Порядковый номер слов необходимо считать с единицы. Вот к примеру, если бы список words был таким:

# words = ['variation', 'random', 'electronics', 'competence', 'collapse']
# то на выходите вы должны были получить такой ответ

# words_with_position = [('variation', 1),
#                        ('random', 2),
#                        ('electronics', 3),
#                        ('competence', 4),
#                        ('collapse', 5)]
# В качестве ответа необходимо вывести words_with_position

words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon',
         'drop', 'produce', 'acquisition', 'cheap', 'strength',
         'master', 'perception', 'noise', 'strange', 'am']

print(words_with_position := [(item, number) for number, item in enumerate(iterable=words, start=1)])
