# Ваша задача написать функцию format_name_list, которая принимает список словарей, у каждого словаря в этом списке есть только ключ name.
#
# Функция format_name_list должна вернуть строку, в которой все имена из списка разделяются запятой кроме последних двух имен, они должны быть разделены союзом "и". Если в списке нет ни одного имени, функция должна вернуть пустую строку. Ниже представлены примеры:
#
# format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) => 'Bart, Lisa и Maggie'
#
# format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) => 'Bart и Lisa'
#
# format_name_list([{'name': 'Bart'}]) => 'Bart'
#
# format_name_list([]) => ''
# Ваша задача написать только определение функции format_name_list


def format_name_list(names: list[dict[str, str]]):
    return ' и '.join(i['name'] for i in names).replace(' и', ',', len(names) - 2)


# код ниже не стоит удалять, он нужен для проверки

assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'},
                         {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer и Marge'

assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa и Maggie'

assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart и Lisa'

assert format_name_list([{'name': 'Bart'}]) == 'Bart'

assert format_name_list([]) == ''

assert format_name_list([{'name': 'Maggie'}, {'name': 'Lisa'}, {'name': 'Barney'}, {'name': 'Homer'}, {'name': 'Bart'},
                         {'name': 'Moe'}]) == 'Maggie, Lisa, Barney, Homer, Bart и Moe'

assert format_name_list([{'name': 'Marge'}, {'name': 'Maggie'}, {'name': 'Seymour'}]) == 'Marge, Maggie и Seymour'

assert format_name_list([{'name': 'Maude'}, {'name': 'Bart'}]) == 'Maude и Bart'

print('Проверки пройдены')
