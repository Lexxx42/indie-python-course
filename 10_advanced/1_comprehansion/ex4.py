# Перед вами список words
#
# Необходимо сохранить в переменной lens генератор-выражение, который генерирует длины слов списка words по порядку.
#
# Больше от вас в этой задаче ничего не требуется.


words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon', 'drop', 'produce', 'acquisition',
         'cheap', 'strength', 'master', 'perception', 'noise', 'strange', 'am']

lens = (len(word) for word in words)

for i in lens:
    print(i)
