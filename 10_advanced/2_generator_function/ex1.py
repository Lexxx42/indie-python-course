# Генератор квадратов
# Ваша задача создать функцию-генератор gen_squares, которая принимает аргумент n и генерирует квадраты чисел от 1 до n включительно. Ниже несколько вариантов использования:
#
# for i in gen_squares(5):
#     print(i)
#
# # Будет напечатано
# # 1
# # 4
# # 9
# # 16
# # 25
# for i in gen_squares(3):
#     print(i)
#
# # Будет напечатано
# # 1
# # 4
# # 9


# Generator[yield_type, send_type, return_type]

from typing import Generator


def gen_squares(n) -> Generator[int, int, None]:
    for j in range(1, n + 1):
        yield j ** 2


for i in gen_squares(4):
    print(i)
