# При помощи генератора-списков создайте список, состоящий из слов,  начинающихся с буквы 't' или 'T'. Слова возьмите из переменной phrase, также не забывайте про метод split()
#
# В качестве ответа выведите полученный список, слова в нем должны стоять в том же порядке, в котором они стояли в изначальной фразе

phrase = 'Take only the words that start with t in this sentence'

print([word for word in phrase.split() if word[0] in ['t', 'T']])
