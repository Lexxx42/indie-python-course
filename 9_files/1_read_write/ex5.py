# В этой задаче вам необходимо скачать файл, в котором записаны натуральные числа. Ваша задача найти
#
# количество трехзначных чисел;
# сумму двухзначных чисел
# В качестве ответа укажите найденные два числа через запятую без других знаков и пробелов. Сперва количество, потом сумма


def count_and_sum(file_name: str) -> dict[str, int]:
    with open(file=file_name, mode='r', encoding='utf-8') as f:
        count_3 = 0
        sum_2 = 0

        for number in f.readlines():
            length = len(number.strip())

            if length == 2:
                sum_2 += int(number.strip())

            elif length == 3:
                count_3 += 1

    return {'count_3': count_3, 'sum_2': sum_2}


print(count_and_sum(file_name='numbers.txt'))
