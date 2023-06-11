# Ситуации, где полезно использовать словарь

# Подсчет количества объектов

# Словари часто используются для подсчета значений.
# При таком использовании ключами словаря будут объекты подсчета,
# а значение ключа – количество появлений этих объектов.

# Пример подсчёта количества элементов в строке:
# подсчитаем сколько раз встретилась каждая буква в строке.

# s = input('Введите строку! Подсчитаем ее буквы: ')
# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)
# for letter, count in d.items():
#     print(letter, count)

# В данном алгоритме если в нашем словаре есть уже такой элемент,
# то мы увеличиваем счётчик на 1, а если этого элемента не было,
# то мы создавали его как ключ и ставим счётчик на 1 (поскольку это его первое появление)

# Давайте оптимизируем:

# при помощи метода isalpha() у строк оставим только буквы,
# тем самым исключим числа и знаки препинания
# вспомним о методе get у словаря: с помощью метода get() можно получить значение,
# которое лежало по данному ключу, а в случае, если ключа не было,
# возвращается 0 и добавляем единицу

# В итоге получим такой код

# s = input('Введите строку! Подсчитваем ее буквы: ')
# d = {}
# for i in s:
#     if i.isalpha():
#         d[i] = d.get(i, 0) + 1
# print(d)
# for letter, count in d.items():
#     print(letter, count)

# Словари помогают установить соответствие между объектами.
# Рассмотрим ситуацию,
# когда необходимо установить соответствие между английским словом и его русским переводом.

# words = {}
# while True:
#     s = input('Введите английское слово: ')
#     if s in words:
#         print("Слово", s, 'переводится как', words[s])
#     else:
#         print("Введите перевод слова", s)
#         words[s] = input()

# В итоге мы вводим слово, если оно есть в словаре,
# то мы выводим значение по заданному ключу (перевод слова),
# если же такого ключа нет,
# то мы просим ввести перевод и добавляем в словарь пару ключ-значение.

# Хранение данных об объектах.
# Рассмотрим вложенный словарь, хранящий данные об известных людях:

# contacts = {
#     'John Kennedy': {
#         'birthday': '29 may 1917', 'city': 'Brookline',
#         'phone': None, 'children': 3
#     },
#     'Arnold Schwarzenegger': {
#         'birthday': '30 july 1947', 'city': 'Gradec',
#         'phone': 555 - 555 - 555, 'children': 5
#     },
#     'Donald John Trump': {
#         'birthday': '14 july 1946', 'city': 'New York',
#         'phone': 777 - 777 - 777, 'children': 4
#     }
# }

# В этом словаре ключи – имена известных людей, а значения – словари.
# Внутри каждого из значений находятся одинаковые ключи:
# день рождения, город, телефон, количество детей.
# Это означает, что наш словарь contacts хранит соответствующую информацию о каждом человеке.
# Создадим список с именами людей, которые находятся в нашем словаре,
# и обойдем их при помощи цикла for и получим для каждого имени контактную информацию:

contacts = {
    'John Kennedy': {
        'birthday': '29 may 1917', 'city': 'Brookline',
        'phone': None, 'children': 3
    },
    'Arnold Schwarzenegger': {
        'birthday': '30 july 1947', 'city': 'Gradec',
        'phone': 555 - 555 - 555, 'children': 5
    },
    'Donald John Trump': {
        'birthday': '14 july 1946', 'city': 'New York',
        'phone': 777 - 777 - 777, 'children': 4
    }
}

persons = ['John Kennedy', 'Arnold Schwarzenegger', 'Donald John Trump']

for person in persons:
    print(person, contacts[person])
    print('-' * 15)
print('/' * 25)
for person in persons:
    print(person, contacts[person]['birthday'])

# Но поскольку вся эта контактная информация также является словарём
# мы можем достать из неё значения по соответствующему ключу,
# к примеру вывести только имя и день рождения:

# for person in persons:
#     print(person, contacts[person]['birthday'])

# Также у нас есть возможность с помощью цикла for так сказать
# достать все эти данные и создать для них переменные:

# persons = ['John Kennedy', 'Arnold Schwarzenegger', 'Donald John Trump']
# for person in persons:
#     birthday = contacts[person]['birthday']
#     city = contacts[person]['city']
#     phone = contacts[person]['phone']
#     children = contacts[person]['children']
#     print(person,  city, birthday)

# Есть ещё один способ обойти все элементы словаря при помощи вложенного цикла for:

persons = ['John Kennedy', 'Arnold Schwarzenegger', 'Donald John Trump']
for person in persons:
    print('-' * 15)
    print(person)
    for data in contacts[person]:
        print(data, contacts[person][data])
