# 1. Функция trunc - является частью модуля math.
# Отсекает дробную часть от числа.
# Фактически, проще использовать встроенную функцию приведения типов int,
# так как её подгружать через модуль не нужно.

# Примеры:
from math import trunc

print(trunc(2.5))  # 2
print(trunc(3.5))  # 3
print(trunc(-2.5))  # -2

print(int(2.5))  # 2
print(int(3.5))  # 3
print(int(-2.5))  # -2

# 2. Функция floor - является частью модуля math.
# Округляет числа в сторону минус бесконечности (вниз).
# Примеры:
from math import floor

print(floor(2.5))  # 2
print(floor(3.5))  # 3
print(floor(-2.5))  # -3

# 3. Функция ceil - является частью модуля math.
# Округляет числа в сторону плюс бесконечности (вверх).
# Примеры:
from math import ceil

print(ceil(2.5))  # 3
print(ceil(3.5))  # 4
print(ceil(-2.5))  # -2

# 4. Функция round - является встроенной функцией, которую не нужно подгружать.
# Она похожа на "школьное округление", но у неё есть своя особенность:

# Числа с дробной частью от 0 до 0.5 (не включая 0.5) - round округляет вниз.
print(round(5.3))  # 5
# Числа с дробной частью от 0.5 (не включая 0.5) до 1 - round округляет вверх.
print(round(6.7))  # 7
# Числа с дробной частью 0.5 - round округляет до ближайшего целого чётного числа.
print(round(12.5))  # 12
print(round(13.5))  # 14

# П.с.: "школьное" округление (если дробная часть от 0 до 0.5 (не включая 0.5) - округление вниз,
# а если от 0.5 до 1 - округление вверх) - это Российский стандарт и в Питон его не закладывали,
# поэтому приходится самим его реализовывать, вот код:

from math import floor, ceil

N = float(input())
if N - int(N) < 0.5:
    print(floor(N))
else:
    print(ceil(N))
