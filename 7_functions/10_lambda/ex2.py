# В переменную starts_with присвойте lambda функцию, которая принимает строку и возвращает True, когда переданная строка начинается с буквы W. Во всех остальных случаях нужно возвращать False
#
# Ничего кроме создания переменной starts_with делать не нужно
#
# Sample Input 1:
#
# World
# Sample Output 1:
#
# True
# Sample Input 2:
#
# when
# Sample Output 2:
#
# False
# Sample Input 3:
#
# Сурикаты
# Sample Output 3:
#
# False
from typing import Callable

starts_with: Callable[[str], bool] = lambda words: words.startswith('W')
