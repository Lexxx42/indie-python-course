# Перед вами список топовых сериалов по версии кинопоиска.
# Ваша задача заменить в нем сериал "Бригада" на "Сверхъестественное"
# и "Друзья" на "Настоящий детектив"

# В качестве ответа распечатайте на экран обновленный список.

top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']


def get_indices(lst: list[str], el: str) -> list[int]:
    return [i for i in range(len(lst)) if lst[i] == el]


def replace_values(lst: list[str], lst_indx: list[int], new_value: str) -> list[str]:
    for idx in lst_indx:
        lst[idx] = new_value
    return lst


upd_list = replace_values(top, get_indices(top, 'Бригада'), 'Сверхъестественное')
print(replace_values(upd_list, get_indices(upd_list, 'Друзья'), 'Настоящий детектив'))
