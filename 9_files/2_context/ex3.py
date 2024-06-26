# В вашем распоряжении имеется файл lorem.txt.
# Ваша задача посчитать сколько раз встретилось каждое слово в этом тексте.

# Для этого создайте словарь words, где ключом будет слово,
# а значением - количество раз появления этого слова в тексте.

# Регистр букв в словах учитывать не нужно, поэтому слова Hello и hEllO являются эквивалентными.
# Значения ключа в словаре words записывайте в верхнем регистре

# Например, если перед вами был бы такой текст:

# Привет как дела
# привет хорошо
# то словарь words выглядел бы так

# {'ПРИВЕТ': 2, 'КАК': 1, 'ДЕЛА': 1, 'ХОРОШО': 1}
# Между словами в файле стоят только пробелы и переносы строк, других разделителей нет.
# Сам файл вы можете скачать здесь

# Ваша задача только создать переменную-словарь words и подсчитать в нем количество повторений слов.
# Выводить ничего не нужно

def count_unique(file_name: str) -> dict[str, int]:
    w = {}

    with open(file=file_name, mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            for word in line.strip().split():
                word_name = word.upper()
                value = w.get(word_name, 0)

                w[word_name] = value + 1

    return w


words = count_unique(file_name='lorem.txt')



