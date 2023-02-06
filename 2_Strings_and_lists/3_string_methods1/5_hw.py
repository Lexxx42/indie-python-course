# На вход подается строка.
# Ваша задача отформатировать строку так,
# чтобы первые 3 и последние 3 символа были заглавными, а оставшиеся строчные.

# Примечание:
# Количество букв может быть различным, но гарантируется что их количество не меньше 6

# Sample Input 1:

# pyThon
# Sample Output 1:

# PYTHON
# Sample Input 2:

# прогРаммирОВАНИЕ
# Sample Output 2:

# ПРОграммироваНИЕ

print((s := input().lower())[:3].upper() + s[3:-3] + s[-3:].upper())
