# Давайте теперь создадим функцию print_goods, которая печатает список покупок.
# На вход она будет принимать произвольное количество значений,
# а товаром мы будем считать любые непустые строки.
# То есть числа, списки, словари и другие нестроковые объекты вам нужно будет проигнорировать.
# Функция print_goods должна печатать список товаров в виде: <Порядковый номер товара>.
# <Название товара> (см. пример ниже).
# В случае, если в переданных значениях не встретится ни одного товара, необходимо распечатать текст "Нет товаров"
#
# print_goods('apple', 'banana', 'orange')
# # Программа должна вывести следующее:
# 1. apple
# 2. banana
# 3. orange
#
# print_goods(1, True, 'Грушечка', '', 'Pineapple')
# # Программа должна вывести следующее:
# 1. Грушечка
# 2. Pineapple
# print_goods([], {}, 1, 2)
# # Программа должна вывести следующее:
# Нет товаров
# Вам необходимо написать только определение функции print_goods

def print_goods(*args) -> None:
    goods: list[str] = []

    for arg in args:
        if isinstance(arg, str) and len(arg) > 0:
            goods.append(arg)

    if len(goods) < 1:
        print('Нет товаров')

    for idx, good in enumerate(goods):
        print(f'{idx + 1}. {good}')


print_goods('apple', 'banana', 'orange')
print()
print_goods(1, True, 'Грушечка', '', 'Pineapple')
print()
print_goods([], {}, 1, 2)
