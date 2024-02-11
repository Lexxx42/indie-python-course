# Хорошо постарались с прошлой задачей!
# Однако мы забыли, что скидка должна быть только для тех товаров,
# стоимость которых больше 50.
# Вам стоит внести это изменение в прошлый код
#
# Ваша задача только переопределить переменную sale_lambda
#
# Sample Input 1:
#
# 50.0
# Sample Output 1:
#
# 50.0
# Sample Input 2:
#
# 60.0
# Sample Output 2:
#
# 54.0
# Sample Input 3:
#
# 12.33
# Sample Output 3:
#
# 12.33

from typing import Callable

sale_lambda: Callable[[int | float], int | float] = lambda x: x * 0.9 if x > 50 else x
