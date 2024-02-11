# Имеется функция sale, которая возвращает цену товара со скидкой 10%.
#
# def sale(x):
#     return x*0.9
# Однако мы изучаем анонимные функции, поэтому на основе данной функции создайте анонимную функцию и присвойте её переменной sale_lambda
from typing import Callable

sale_lambda: Callable[[int | float], float] = lambda x: x * 0.9
