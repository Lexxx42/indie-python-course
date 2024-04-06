# Давайте напишем выражение-генератор, который будет генерировать кортеж состоящий из двух элементов: названия дня недели и номер дня в году.
#
# За начало отсчета возьмем наш «любимый» 2022 год. Он начался в субботу, потом воскресенье, понедельник, вторник, ..., пятница, суббота и далее по кругу
#
# Результат выражения-генератор сохраните в переменную days
#
# Названия дней недели должны совпадать с этими значениями:
#
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Значит при первой итерации генератор должен вернуть кортеж
#
# (1, 'Saturday')
# При второй итерации вернется значение
#
# (2, 'Sunday')
# Ваша задача распечатать на удачу 77 первых дней 2022 года. Выводить на экран нужно сами кортежи и первые десять значений в выводе должны выглядеть вот так:
#
# (1, 'Saturday')
# (2, 'Sunday')
# (3, 'Monday')
# (4, 'Tuesday')
# (5, 'Wednesday')
# (6, 'Thursday')
# (7, 'Friday')
# (8, 'Saturday')
# (9, 'Sunday')
# (10, 'Monday')

days_of_a_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

days = ((i + 1, days_of_a_week[(5 + i) % 7]) for i in range(365))

for j in range(77):
    print(next(days))
