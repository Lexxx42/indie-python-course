# Напишите функцию find_lines_len_more_6,
# которая принимает имя файла и находит количество строк, превышающее 6 символов.
# Не забывайте исключать знак переноса на новую строку, стоящий в конце строки.
#
# Функция find_lines_len_more_6 должна возвращать найденное количество строк
#
# Ваша задача написать только определение функции find_lines_len_more_6


def find_lines_len_more_6(file_name: str) -> int:
    count = 0

    with open(file=file_name, mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            length = len(line.strip('\n'))

            if length > 6:
                count += 1

    return count


print(find_lines_len_more_6(file_name='test.txt'))
