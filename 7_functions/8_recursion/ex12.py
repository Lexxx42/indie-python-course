# Превращаем вложенный словарь в плоский
# Перед вами имеется вложенный словарь, уровень вложенности произвольный и заранее неизвестен. Ключами словаря на любом уровне могут быть только строки, значения - только числа.
#
# Учитывая указанные выше условия, ваша задача состоит в том, чтобы преобразовать этот вложенный словарь в плоский (состоящий только из одного уровня), где ключи формируются конкатенацией вложенных ключей, соединенных знаком _
#
# Для этого необходимо определить рекурсивную функцию flatten_dict. Она должна принимать вложенный словарь и возвращать плоский
#
# Ниже приведены несколько способов решения вышеуказанной задачи.
#
# nested = {'Germany': {'berlin': 7},
#           'Europe': {'italy': {'Rome': 3}},
#           'USA': {'washington': 1, 'New York': 4}}
#
# flatten_dict(nested) => {'Germany_berlin': 7,
#                          'Europe_italy_Rome': 3,
#                          'USA_washington': 1,
#                          'USA_New York': 4}
# nested = {'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}
#
# flatten_dict(nested) => {'Q_w_E_r_T_y': 123}
# not_nested = {'a': 100, 'b': 200}
#
# flatten_dict(not_nested) => {'a': 100, 'b': 200}
# Ваша задача только написать определение функции flatten_dict


from collections.abc import MutableMapping


def flatten_dict(dictionary, parent_key='', separator='_'):
    items = []
    for key, value in dictionary.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, MutableMapping):
            items.extend(flatten_dict(value, new_key, separator=separator).items())
        else:
            items.append((new_key, value))
    return dict(items)


nested = {
    'Germany': {'berlin': 7},
    'Europe': {'italy': {'Rome': 3}},
    'USA': {'washington': 1, 'New York': 4}
}

print(flatten_dict(nested))


def flatten_dict(d: dict) -> dict:
    # WOW
    res = {}
    for kp, vp in d.items():
        res.update({f'{kp}_{k}': v for k, v in flatten_dict(vp).items()} if type(vp) is dict else {kp: vp})
    return res


print(flatten_dict(nested))
