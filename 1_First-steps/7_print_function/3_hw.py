# Вам необходимо вывести три фразы, резделяя их тремя дефисами.
# Сами фразы вводятся с клавиатуры на трех разных строчках.

# Вход:
# Да пребудет
# с тобой
# Сила

# Выход:
# Да прибудет---с тобой---Сила

print("---".join([input() for _ in range(3)]))