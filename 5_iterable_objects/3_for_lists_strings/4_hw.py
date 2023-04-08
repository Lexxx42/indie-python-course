# Перед вами список words, состоящий из 100 строк

# Ваша задачи пройтись в цикле по элементам списка
# и вывести на экран только те элементы, длина которых больше 6.
#
# Выводить каждый элемент нужно на отдельной строке в том же порядке,
# в котором слова расположены в списке words

words = ['require', 'build', 'head', 'land', 'dark', 'seat', 'have', 'five', 'particularly', 'focus', 'moment',
         'visit', 'past', 'turn', 'bad', 'modern', 'once', 'future', 'pay', 'assume', 'himself', 'physical', 'chance',
         'remember', 'better', 'former', 'believe', 'explain', 'reduce', 'whatever', 'theory', 'during', 'enough',
         'wall', 'commercial', 'challenge', 'tell', 'actually', 'include', 'somebody', 'decade', 'by', 'better',
         'would', 'five', 'cost', 'kitchen', 'our', 'affect', 'board', 'practice', 'full', 'instead', 'apply', 'good',
         'past', 'clearly', 'special', 'both', 'analysis', 'peace', 'truth', 'cultural', 'light', 'answer', 'build',
         'each', 'watch', 'buy', 'theory', 'pretty', 'expect', 'account', 'music', 'sell', 'newspaper', 'reach',
         'fish', 'tax', 'employee', 'start', 'most', 'during', 'citizen', 'develop', 'carry', 'only', 'certainly',
         'rock', 'economy', 'risk', 'later', 'one', 'body', 'star', 'they', 'choice', 'appear', 'return', 'sometimes']

# for word in list(filter(lambda x: len(x) > 6, words)):
#     print(word)
for i in words:
    if len(i) > 6:
        print(i)
