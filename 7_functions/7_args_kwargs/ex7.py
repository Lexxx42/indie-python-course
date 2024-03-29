# Напишите функцию create_actor, которая принимает произвольное количество именованных аргументов и возвращает словарь с характеристиками актера. Если функции create_actor не передавать никаких аргументов, то она должна возвращать базовый словарь с ключами name, surname, age. Вот так он выглядит:
#
# create_actor() -> {
#         'name': 'Райан',
#         'surname': 'Рейнольдс',
#         'age': 46,
#     }
# Если передавать именованные параметры, которые отсутствуют в базовом словаре, они дополняются к этому словарю
#
# create_actor(height=190, movies=['Дедпул', 'Главный герой']) => {
#     'name': 'Райан',
#     'surname': 'Рейнольдс',
#     'age': 46,
#     'height': 190,
#     'movies': ['Дедпул', 'Главный герой']
# }
# Если передавать именованные параметры, которые совпадают с ключами базового словаря, то значения в словаре должны заменяться переданными значениями:
#
# create_actor(name='Jack', age=20) -> {
#         'name': 'Jack',
#         'surname': 'Рейнольдс',
#         'age': 20,
#     }
# Вам необходимо написать только определение функции create_actor

def create_actor(**kwargs):
    return {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 46,
    } | kwargs


print(create_actor())
print(create_actor(height=190, movies=['Дедпул', 'Главный герой']))
