# Перед вами два списка
#
# employees содержит имена работников
#
# identifiers содержит уникальные идентификаторы работников
#
# Сейчас значения в каждом списке перемешаны и не понятно какому работнику какой идентификатор принадлежит. Отдел кадров просит вас создать словарь employees_data, в котором, ключами будут идентификаторы, а значениями - имена работников. При этом отдел кадров просит соотнести идентификатор работника с именем следующим образом:
#
# Выбирается самый маленький идентификатор из списка identifiers
# Выбирается первое имя по алфавиту из списка employees
# Создается пара ключ-значение. В нашем случае самый маленький идентификатор 5, первое имя по алфавиту будет Anfisa. Значит создаем пару 5: 'Anfisa'
# Процесс повторяется со следующими значениями. Берется второй по старшинству идентификатор и второе имя по алфавиту, создается пара в словаре и вновь повторяем процесс
# В итоге у вас должен получится словарь employees_data , его выводить не нужно!!! Только правильно заполнить


employees = [
    'Pankratiy', 'Innokentiy', 'Anfisa', 'Yaroslava', 'Veniamin',
    'Leonti', 'Daniil', 'Mishka', 'Lidochka',
    'Terenti', 'Vladik', 'Svetka', 'Maks', 'Yura', 'Sergei'
]

identifiers = [77, 48, 88, 85, 76, 81, 62, 43, 5, 56, 17, 20, 37, 32, 96]

employees_data = {k: v for k, v in zip(sorted(identifiers), sorted(employees))}

