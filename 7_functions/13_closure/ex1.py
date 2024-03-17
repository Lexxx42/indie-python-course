# Ваша задача создать функцию-замыкание create_accumulator, она должна накапливать(суммировать) в себе все значения, которые ей будут переданы, при создании сумма должна быть равна нулю. Посмотрите пример ниже:
#
# summator_1 = create_accumulator()
# print(summator_1(1)) # печатает 1
# print(summator_1(5)) # печатает 6
# print(summator_1(2)) # печатает 8
#
# summator_2 = create_accumulator()
# print(summator_2(3)) # печатает 3
# print(summator_2(4)) # печатает 7
# При каждом вызове должна возвращаться накопленная сумма, которая хранится в замыкании.
#
# Обратите внимание, что объекты из примера summator_1 и summator_2 хранят и накапливают свои собственные суммы.
#
# Необходимо только определить функцию-замыкание create_accumulator, остальное мы сделаем за вас


# def create_accumulator(var: int = 0):
#     def _sum(a):
#         return var + a
#
#     return _sum
#
#
# summator_1 = create_accumulator()
# print(summator_1(1))  # печатает 1
# print(summator_1(5))  # печатает 6
# print(summator_1(2))  # печатает 8


def create_accumulator(value=0):
    _sum = 0

    def inner(a):
        nonlocal _sum
        _sum += a
        return _sum

    return inner


a2 = create_accumulator()
print(a2(5))
print(a2(57))
