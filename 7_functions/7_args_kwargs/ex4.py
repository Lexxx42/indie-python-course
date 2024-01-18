# Напишите функцию only_one_positive,
# которая принимает произвольное количество числовых аргументов и возвращает True,
# когда из всех переданных значений только одно положительное, в противном случае верните False
#
# Вам необходимо написать только определение функции only_one_positive
#
# Ниже примеры вызова
#
# only_one_positive(1, 2) -> False
# only_one_positive(-1, 0, -3, 5, -3) -> True
# only_one_positive() -> False

def only_one_positive(*args: int) -> bool:
    return len([arg for arg in args if arg > 0]) == 1


assert only_one_positive(1, 2) is False
assert only_one_positive(-1, 0, -3, 5, -3) is True
assert only_one_positive() is False
