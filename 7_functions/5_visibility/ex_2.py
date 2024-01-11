# В этой задаче вам необходимо создать функцию get_word_indices,
# которая принимает список строк и возвращает словарь,
# где ключи - это уникальные слова из списка строк в нижнем регистре,
# а значения - это списки индексов строк, в которых эти слова встречаются.

def get_word_indices(strings: list[str]) -> dict:
    result = {}
    for idx, string in enumerate(strings):
        for word in string.split():
            if word.lower() not in result:
                result[word.lower()] = [idx]
            else:
                result[word.lower()].append(idx)
    return result


assert get_word_indices(['This is a string',
                         'test String',
                         'test',
                         'string']) == {'this': [0], 'is': [0], 'a': [0],
                                        'string': [0, 1, 3], 'test': [1, 2]}

assert get_word_indices(['Look at my horse',
                         'my horse',
                         'is amazing']) == {'look': [0], 'at': [0], 'my': [0, 1],
                                            'horse': [0, 1], 'is': [2], 'amazing': [2]}

assert get_word_indices([]) == {}

assert get_word_indices(
    ['Avada Kedavra',
     'avada kedavra',
     'AVADA KEDAVRA']
) == {'avada': [0, 1, 2], 'kedavra': [0, 1, 2]}
