# Перед вами кортеж english_words
#
# При помощи enumerate обойдите слова этой коллекции и для каждого элемента выведите строку вида
#
# Word № {number} = {word}
# Например, для кортежа english_words = ('hi', 'World') ответ был бы таким:
#
# Word № 1 = hi
# Word № 2 = World
# Обратите внимание, что нумерация слов начинается с единицы
#
# Sample Input:
#
# Sample Output:
#
# Word № 1 = attack
# Word № 2 = bless
# Word № 3 = look
# Word № 4 = reckless
# Word № 5 = short
# Word № 6 = monster
# Word № 7 = trolley
# Word № 8 = sound
# Word № 9 = ambiguity
# Word № 10 = researcher
# Word № 11 = trunk
# Word № 12 = coat
# Word № 13 = quantity
# Word № 14 = question
# Word № 15 = tenant
# Word № 16 = miner
# Word № 17 = definite
# Word № 18 = kit
# Word № 19 = spectrum
# Word № 20 = satisfied
# Word № 21 = selection
# Word № 22 = carve
# Word № 23 = ask
# Word № 24 = go
# Word № 25 = suggest

english_words = ('attack', 'bless', 'look', 'reckless', 'short', 'monster', 'trolley', 'sound',
                 'ambiguity', 'researcher', 'trunk', 'coat', 'quantity', 'question', 'tenant',
                 'miner', 'definite', 'kit', 'spectrum', 'satisfied', 'selection', 'carve',
                 'ask', 'go', 'suggest')

for i, word in enumerate(iterable=english_words, start=1):
    print(f'Word № {i} = {word}')
