# Напишите функцию multiply, которая принимает произвольное количество числовых аргументов. Данная функция должна находить произведение всех переданных значений и возвращать его в качестве результата
#
# multiply(1, 2, 3) => 6
# multiply(1, 3) => 3
# multiply(2) => 2
# multiply() => 1
# Вам необходимо написать только определение функции multiply

def multiply(*args: int) -> int:
    result = 1
    for arg in args:
        result *= arg
    return result


assert multiply(1, 2, 3) == 6
assert multiply(1, 3) == 3
assert multiply(2) == 2
assert multiply() == 1